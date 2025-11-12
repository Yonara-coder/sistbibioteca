# Sistema de Gerenciamento de Biblioteca

## Descrição

Sistema completo de gerenciamento de biblioteca desenvolvido com Django e Django Jazzmin. Este sistema permite o cadastro e gestão de livros, autores, editoras, gêneros, membros da biblioteca, empréstimos e devoluções através de um painel administrativo moderno e intuitivo.

## Tema Escolhido

O tema escolhido é um **Sistema de Gerenciamento de Biblioteca**. Este tema foi selecionado por ser um sistema completo que demonstra a capacidade de modelar relacionamentos complexos entre entidades (livros, autores, membros, empréstimos), além de permitir a implementação de funcionalidades administrativas avançadas com o Django Admin customizado através do Jazzmin.

## Modelagem de Dados

O sistema possui **8 models** interligados que representam todas as entidades necessárias para o funcionamento de uma biblioteca:

### 1. **Editora**
- **Finalidade**: Armazena informações sobre as editoras dos livros
- **Campos principais**: nome, endereço, telefone, email
- **Relacionamentos**: Relacionada com Livro através de ForeignKey (um-para-muitos)

### 2. **Autor**
- **Finalidade**: Gerencia informações sobre os autores dos livros
- **Campos principais**: nome, sobrenome, data_nascimento, nacionalidade, biografia
- **Relacionamentos**: Relacionado com Livro através de ManyToManyField (muitos-para-muitos), permitindo que um livro tenha múltiplos autores e um autor tenha múltiplos livros

### 3. **Genero**
- **Finalidade**: Categoriza os livros por gênero literário
- **Campos principais**: nome, descricao
- **Relacionamentos**: Relacionado com Livro através de ManyToManyField (muitos-para-muitos), permitindo que um livro pertença a múltiplos gêneros

### 4. **Livro**
- **Finalidade**: Representa os livros cadastrados na biblioteca
- **Campos principais**: título, ano_publicacao, isbn, descricao, capa (imagem)
- **Relacionamentos**: 
  - ForeignKey com Editora (muitos-para-um)
  - ManyToManyField com Autor (muitos-para-muitos)
  - ManyToManyField com Genero (muitos-para-muitos)
  - Relacionado com Exemplar através de ForeignKey (um-para-muitos)

### 5. **Membro**
- **Finalidade**: Gerencia os membros/usuários da biblioteca
- **Campos principais**: nome, sobrenome, email, telefone, endereço, data_adesao, ativo
- **Relacionamentos**: Relacionado com Emprestimo através de ForeignKey (um-para-muitos)

### 6. **Exemplar**
- **Finalidade**: Representa cópias físicas específicas de um livro (um livro pode ter vários exemplares)
- **Campos principais**: codigo_exemplar, disponivel, data_aquisicao, condicao
- **Relacionamentos**: 
  - ForeignKey com Livro (muitos-para-um)
  - Relacionado com Emprestimo através de ForeignKey (um-para-muitos)

### 7. **Emprestimo**
- **Finalidade**: Registra os empréstimos de livros para membros
- **Campos principais**: data_emprestimo, data_devolucao_prevista, devolvido
- **Relacionamentos**: 
  - ForeignKey com Exemplar (muitos-para-um)
  - ForeignKey com Membro (muitos-para-um)
  - Relacionado com Devolucao através de OneToOneField (um-para-um)

### 8. **Devolucao**
- **Finalidade**: Registra as devoluções de empréstimos
- **Campos principais**: data_devolucao_real, multa, observacoes
- **Relacionamentos**: OneToOneField com Emprestimo (um-para-um), garantindo que cada empréstimo tenha no máximo uma devolução

### Tipos de Relacionamentos Utilizados:

- **ForeignKey**: Usado para relacionamentos um-para-muitos
  - Livro → Editora
  - Exemplar → Livro
  - Emprestimo → Exemplar e Membro
  - Devolucao → Emprestimo (através de OneToOneField)

- **ManyToManyField**: Usado para relacionamentos muitos-para-muitos
  - Livro ↔ Autor
  - Livro ↔ Genero

- **OneToOneField**: Usado para relacionamento um-para-um
  - Devolucao → Emprestimo

## Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. **Clone o repositório** (ou baixe os arquivos do projeto)

2. **Crie e ative um ambiente virtual**:

   ```bash
   # No Windows
   python -m venv venv
   venv\Scripts\activate

   # No Linux/macOS
   python -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário** para acessar o painel administrativo:

   ```bash
   python manage.py createsuperuser
   ```

6. **Colete os arquivos estáticos** (necessário para o CSS customizado):

   ```bash
   python manage.py collectstatic --noinput
   ```

   **Nota**: Em desenvolvimento, o Django serve arquivos estáticos automaticamente quando `DEBUG = True`. O comando acima é necessário apenas para produção.

7. **Inicie o servidor de desenvolvimento**:

   ```bash
   python manage.py runserver
   ```

8. **Acesse o painel administrativo**:

   Abra seu navegador e acesse: `http://127.0.0.1:8000/admin/`

   Faça login com as credenciais do superusuário criado no passo 5.

   **Observação**: Você verá o tema customizado de biblioteca aplicado em todas as páginas do admin, com cores que remetem a sabedoria e tranquilidade.

## Customizações do Django Admin

O sistema utiliza o **Django Jazzmin** para personalizar o painel administrativo do Django, proporcionando uma interface moderna e intuitiva.

### Configurações do Jazzmin

- **Tema**: United (com suporte a modo escuro)
- **Cores**: Navbar azul escuro com sidebar primária
- **Ícones personalizados**: Cada model possui um ícone Font Awesome específico
- **Menu de navegação**: Expandido por padrão com links personalizados

### ModelAdmin Customizados

Todos os 8 models possuem classes `ModelAdmin` customizadas com as seguintes funcionalidades:

#### **EditoraAdmin**
- `list_display`: nome, email, telefone
- `search_fields`: nome, email

#### **AutorAdmin**
- `list_display`: nome_completo (método customizado), data_nascimento, nacionalidade
- `search_fields`: nome, sobrenome, nacionalidade
- `list_filter`: nacionalidade

#### **GeneroAdmin**
- `list_display`: nome, descricao
- `search_fields`: nome

#### **LivroAdmin** (Customização Completa)
- `list_display`: título, ano_publicacao, editora, exibir_autores, exibir_generos, isbn
- `list_filter`: ano_publicacao, editora, generos
- `search_fields`: título, isbn, editora__nome, autores__nome, autores__sobrenome
- `filter_horizontal`: autores, generos (interface melhorada para ManyToManyField)
- `raw_id_fields`: editora (facilita seleção quando há muitos objetos)

#### **MembroAdmin** (Customização Completa)
- `list_display`: nome_completo, email, telefone, data_adesao, ativo
- `list_filter`: ativo, data_adesao
- `search_fields`: nome, sobrenome, email, telefone
- `list_editable`: ativo (permite editar diretamente na lista)
- `date_hierarchy`: data_adesao (navegação por data)

#### **ExemplarAdmin** (Customização Completa)
- `list_display`: codigo_exemplar, livro, disponivel, condicao, data_aquisicao
- `list_filter`: disponivel, condicao, livro__titulo
- `search_fields`: codigo_exemplar, livro__titulo, livro__isbn
- `list_editable`: disponivel, condicao
- `raw_id_fields`: livro

#### **EmprestimoAdmin** (Customização Completa)
- `list_display`: id, membro, exemplar, data_emprestimo, data_devolucao_prevista, devolvido
- `list_filter`: devolvido, data_emprestimo, data_devolucao_prevista
- `search_fields`: membro__nome, membro__sobrenome, exemplar__codigo_exemplar, exemplar__livro__titulo
- `raw_id_fields`: membro, exemplar
- `date_hierarchy`: data_emprestimo
- `readonly_fields`: data_emprestimo

#### **DevolucaoAdmin**
- `list_display`: emprestimo, data_devolucao_real, multa
- `list_filter`: data_devolucao_real, multa
- `search_fields`: emprestimo__membro__nome, emprestimo__exemplar__livro__titulo
- `raw_id_fields`: emprestimo
- `readonly_fields`: data_devolucao_real

## Estilização e Tema Visual

O sistema possui uma estilização customizada com tema de biblioteca, utilizando cores que remetem a sabedoria e tranquilidade:

### Paleta de Cores

- **Marrom Sienna (#8B4513)**: Cor principal, remetendo a livros antigos e couro
- **Bege Dourado (#D4A574)**: Cor secundária, lembrando páginas envelhecidas
- **Verde Floresta (#2F4F2F)**: Cor terciária, representando conhecimento e crescimento
- **Marrom Escuro (#6B4423)**: Cor de destaque, evocando couro de livros
- **Bege Claro (#F5E6D3)**: Cor de fundo, lembrando papel envelhecido

### Características Visuais

- **Fonte**: Georgia e Times New Roman (fontes serifadas clássicas)
- **Gradientes**: Aplicados em navbar, sidebar e botões para profundidade visual
- **Sombras suaves**: Box-shadows que dão profundidade aos elementos
- **Animações**: Transições suaves em hover e interações
- **Scrollbar customizada**: Estilizada com as cores do tema

### Templates Customizados

Todos os templates do Django Admin foram customizados para incluir o CSS personalizado:

- `templates/admin/base.html` - Template base
- `templates/admin/base_site.html` - Branding customizado
- `templates/admin/index.html` - Página inicial com mensagem de boas-vindas
- `templates/admin/change_list.html` - Listagem de objetos
- `templates/admin/change_form.html` - Formulários de edição
- `templates/admin/delete_confirmation.html` - Confirmação de exclusão
- `templates/admin/login.html` - Página de login

### CSS Customizado

O arquivo `static/admin/css/biblioteca_custom.css` contém toda a estilização customizada, incluindo:

- Estilos para navbar e sidebar
- Customização de tabelas, cards e boxes
- Estilização de botões e formulários
- Personalização de links, badges e alertas
- Responsividade para dispositivos móveis
- Animações e transições suaves

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **Django**: Framework web utilizado para desenvolvimento
- **Django Jazzmin**: Tema administrativo moderno para Django Admin
- **Pillow**: Biblioteca para manipulação de imagens (necessária para o campo de capa dos livros)
- **SQLite**: Banco de dados padrão (pode ser alterado para PostgreSQL, MySQL, etc. em produção)
- **HTML/CSS**: Templates e estilização customizada com tema de biblioteca

## Estrutura do Projeto

```
biblioteca/
├── biblioteca_projeto/          # Configurações do projeto Django
│   ├── __init__.py
│   ├── settings.py              # Configurações incluindo Jazzmin
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── biblioteca_app/              # Aplicação principal
│   ├── __init__.py
│   ├── admin.py                # Customizações do Admin
│   ├── apps.py
│   ├── models.py               # 8 models do sistema
│   ├── views.py
│   └── tests.py
├── templates/                   # Templates HTML customizados
│   └── admin/                  # Templates do Django Admin
│       ├── base.html
│       ├── base_site.html
│       ├── index.html
│       ├── change_list.html
│       ├── change_form.html
│       ├── delete_confirmation.html
│       └── login.html
├── static/                     # Arquivos estáticos (CSS, JS, imagens)
│   └── admin/
│       └── css/
│           └── biblioteca_custom.css  # CSS customizado com tema de biblioteca
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Funcionalidades Principais

- ✅ Cadastro de Editoras
- ✅ Cadastro de Autores
- ✅ Cadastro de Gêneros Literários
- ✅ Cadastro de Livros (com suporte a múltiplos autores e gêneros)
- ✅ Cadastro de Membros da Biblioteca
- ✅ Gerenciamento de Exemplares (cópias físicas dos livros)
- ✅ Controle de Empréstimos
- ✅ Registro de Devoluções (com cálculo de multas)
- ✅ Interface administrativa moderna com Jazzmin
- ✅ Busca e filtros avançados em todas as entidades
- ✅ Suporte a upload de imagens para capas dos livros

## Como Contribuir

Este é um projeto acadêmico desenvolvido por Yonara. Para contribuições futuras:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## Autor

**Yonara** - 2024

---

Desenvolvido com ❤️ usando Django e Django Jazzmin

