# biblioteca_app/models.py
from django.db import models
from django.core.validators import MinValueValidator


class Editora(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Editora")
    endereco = models.CharField(max_length=255, blank=True, null=True, verbose_name="Endereço")
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Primeiro Nome")
    sobrenome = models.CharField(max_length=100, verbose_name="Sobrenome")
    data_nascimento = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    nacionalidade = models.CharField(max_length=100, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True, verbose_name="Biografia")

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        unique_together = ('nome', 'sobrenome')  # Garante que não haja autores com o mesmo nome e sobrenome
        ordering = ['sobrenome', 'nome']

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Genero(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name="Nome do Gênero")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    ano_publicacao = models.IntegerField(
        validators=[MinValueValidator(1000)], verbose_name="Ano de Publicação"
    )
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL, null=True, verbose_name="Editora")
    autores = models.ManyToManyField(Autor, verbose_name="Autores")
    generos = models.ManyToManyField(Genero, verbose_name="Gêneros")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN", help_text="13 Caracteres ISBN")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    # Temporariamente usando FileField até Pillow ser instalado corretamente
    # capa = models.ImageField(upload_to='capas/', blank=True, null=True, verbose_name="Capa do Livro")
    capa = models.FileField(upload_to='capas/', blank=True, null=True, verbose_name="Capa do Livro")

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ['titulo']

    def __str__(self):
        return f"{self.titulo} ({self.ano_publicacao})"


class Membro(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    sobrenome = models.CharField(max_length=100, verbose_name="Sobrenome")
    data_adesao = models.DateField(auto_now_add=True, verbose_name="Data de Adesão")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(unique=True, verbose_name="Email")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"
        ordering = ['sobrenome', 'nome']

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Exemplar(models.Model):
    CONDICAO_CHOICES = [
        ('EX', 'Excelente'),
        ('BO', 'Boa'),
        ('RE', 'Regular'),
        ('DE', 'Desgastada'),
    ]
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro")
    codigo_exemplar = models.CharField(max_length=50, unique=True, verbose_name="Código do Exemplar")
    disponivel = models.BooleanField(default=True, verbose_name="Disponível para Empréstimo")
    data_aquisicao = models.DateField(verbose_name="Data de Aquisição")
    condicao = models.CharField(max_length=2, choices=CONDICAO_CHOICES, default='BO', verbose_name="Condição")

    class Meta:
        verbose_name = "Exemplar"
        verbose_name_plural = "Exemplares"
        ordering = ['livro__titulo', 'codigo_exemplar']

    def __str__(self):
        return f"Exemplar {self.codigo_exemplar} de {self.livro.titulo}"


class Emprestimo(models.Model):
    exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE, verbose_name="Exemplar Emprestado")
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE, verbose_name="Membro")
    data_emprestimo = models.DateTimeField(auto_now_add=True, verbose_name="Data do Empréstimo")
    data_devolucao_prevista = models.DateField(verbose_name="Data de Devolução Prevista")
    devolvido = models.BooleanField(default=False, verbose_name="Devolvido")

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
        ordering = ['-data_emprestimo']

    def __str__(self):
        return f"Empréstimo de '{self.exemplar.livro.titulo}' para {self.membro.nome} ({'Devolvido' if self.devolvido else 'Pendente'})"


class Devolucao(models.Model):
    emprestimo = models.OneToOneField(Emprestimo, on_delete=models.CASCADE, verbose_name="Empréstimo Referente")
    data_devolucao_real = models.DateTimeField(auto_now_add=True, verbose_name="Data da Devolução Real")
    multa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Valor da Multa")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")

    class Meta:
        verbose_name = "Devolução"
        verbose_name_plural = "Devoluções"
        ordering = ['-data_devolucao_real']

    def __str__(self):
        return f"Devolução de '{self.emprestimo.exemplar.livro.titulo}' por {self.emprestimo.membro.nome}"

