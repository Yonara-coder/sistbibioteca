# biblioteca_app/admin.py
from django.contrib import admin
from .models import (
    Editora, Autor, Genero, Livro,
    Membro, Exemplar, Emprestimo, Devolucao
)


# 1. Editora
@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)  # Embora possa não ter muitas opções, demonstra a funcionalidade


# 2. Autor
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'data_nascimento', 'nacionalidade')
    search_fields = ('nome', 'sobrenome', 'nacionalidade')
    list_filter = ('nacionalidade',)

    def nome_completo(self, obj):
        return f"{obj.nome} {obj.sobrenome}"
    nome_completo.short_description = "Nome Completo"


# 3. Genero
@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)


# 4. Livro (Customização Completa)
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano_publicacao', 'editora', 'exibir_autores', 'exibir_generos', 'isbn')
    list_filter = ('ano_publicacao', 'editora', 'generos')
    search_fields = ('titulo', 'isbn', 'editora__nome', 'autores__nome', 'autores__sobrenome')
    filter_horizontal = ('autores', 'generos')  # Melhora a interface para ManyToManyField
    raw_id_fields = ('editora',)  # Útil para muitos objetos em ForeignKey

    def exibir_autores(self, obj):
        return ", ".join([str(autor) for autor in obj.autores.all()])
    exibir_autores.short_description = "Autores"

    def exibir_generos(self, obj):
        return ", ".join([genero.nome for genero in obj.generos.all()])
    exibir_generos.short_description = "Gêneros"


# 5. Membro (Customização Completa)
@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email', 'telefone', 'data_adesao', 'ativo')
    list_filter = ('ativo', 'data_adesao')
    search_fields = ('nome', 'sobrenome', 'email', 'telefone')
    list_editable = ('ativo',)  # Permite editar 'ativo' diretamente na lista
    date_hierarchy = 'data_adesao'  # Adiciona uma navegação por data

    def nome_completo(self, obj):
        return f"{obj.nome} {obj.sobrenome}"
    nome_completo.short_description = "Nome Completo do Membro"


# 6. Exemplar (Customização Completa)
@admin.register(Exemplar)
class ExemplarAdmin(admin.ModelAdmin):
    list_display = ('codigo_exemplar', 'livro', 'disponivel', 'condicao', 'data_aquisicao')
    list_filter = ('disponivel', 'condicao', 'livro__titulo')
    search_fields = ('codigo_exemplar', 'livro__titulo', 'livro__isbn')
    list_editable = ('disponivel', 'condicao')
    raw_id_fields = ('livro',)


# 7. Emprestimo (Customização Completa)
@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('id', 'membro', 'exemplar', 'data_emprestimo', 'data_devolucao_prevista', 'devolvido')
    list_filter = ('devolvido', 'data_emprestimo', 'data_devolucao_prevista')
    search_fields = ('membro__nome', 'membro__sobrenome', 'exemplar__codigo_exemplar', 'exemplar__livro__titulo')
    raw_id_fields = ('membro', 'exemplar')  # Para facilitar a seleção de muitos membros/exemplares
    date_hierarchy = 'data_emprestimo'
    # Campos que só podem ser visualizados, não editados após a criação
    readonly_fields = ('data_emprestimo',)


# 8. Devolucao
@admin.register(Devolucao)
class DevolucaoAdmin(admin.ModelAdmin):
    list_display = ('emprestimo', 'data_devolucao_real', 'multa')
    list_filter = ('data_devolucao_real', 'multa')
    search_fields = ('emprestimo__membro__nome', 'emprestimo__exemplar__livro__titulo')
    raw_id_fields = ('emprestimo',)
    readonly_fields = ('data_devolucao_real',)

