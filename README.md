# CRUD de Produtos | Django

Aplicação web para cadastro e gerenciamento de produtos, desenvolvida com Python e Django. Permite consultar, cadastrar, atualizar e excluir registros com persistência em banco de dados SQLite.

Projeto desenvolvido para consolidar fundamentos de desenvolvimento web e versionamento de código.

## Funcionalidades

| Recurso | Descrição |
|---|---|
| Cadastro | Inclusão de produtos com nome, preço e quantidade em estoque. |
| Listagem | Exibição dos produtos registrados no banco de dados. |
| Edição | Atualização das informações de um produto existente. |
| Exclusão | Remoção de produtos mediante confirmação. |
| Administração | Gerenciamento dos registros pelo Django Admin. |

Os formulários utilizam a validação do Django, e as operações de cadastro, edição e exclusão utilizam proteção CSRF.

## Tecnologias utilizadas

- **Python** — linguagem de programação.
- **Django** — framework web.
- **SQLite** — banco de dados utilizado no desenvolvimento.
- **HTML e Django Templates** — apresentação das páginas.
- **python-dotenv** — carregamento das configurações locais.
- **Git e GitHub** — versionamento e hospedagem do código.

As versões das dependências estão registradas em `requirements.txt`.

## Organização do projeto

| Caminho | Responsabilidade |
|---|---|
| `config/settings.py` | Configurações gerais da aplicação. |
| `config/urls.py` | Mapeamento das rotas. |
| `produtos/models.py` | Definição do modelo `Produto`. |
| `produtos/forms.py` | Formulário baseado no modelo. |
| `produtos/views.py` | Lógica das operações do CRUD. |
| `produtos/templates/produtos/` | Templates HTML. |
| `produtos/migrations/` | Histórico das alterações na estrutura do banco. |
| `manage.py` | Interface de comandos do projeto Django. |
| `requirements.txt` | Dependências do ambiente. |

## Executando localmente

### Pré-requisitos

- Git instalado.
- Python compatível com a versão do Django em `requirements.txt`.
- Terminal com acesso à pasta do projeto.

Os exemplos abaixo utilizam **Windows com PowerShell**.

### 1. Clonar o repositório

```powershell
git clone https://github.com/EdisonC-Dev/crud-produtos-django.git
cd crud-produtos-django
```

### 2. Criar e ativar o ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

Gere uma chave para o ambiente local:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

Na pasta que contém `manage.py`, crie um arquivo `.env`:

```dotenv
DJANGO_SECRET_KEY='substitua_pela_chave_gerada'
```

O arquivo `.env` é ignorado pelo Git. Cada ambiente deve utilizar sua própria chave.

### 5. Aplicar as migrations

```powershell
python manage.py migrate
```

Esse comando cria as tabelas necessárias. O banco local não acompanha o repositório, portanto a aplicação inicia sem os produtos e usuários do ambiente original.

### 6. Criar um administrador — opcional

```powershell
python manage.py createsuperuser
```

Esse usuário permite acessar o painel administrativo do Django.

### 7. Iniciar a aplicação

```powershell
python manage.py runserver
```

Acesse a aplicação em:

**http://127.0.0.1:8000/**

## Rotas da aplicação

| Endereço | Finalidade |
|---|---|
| `/` | Listar produtos. |
| `/produtos/novo/` | Cadastrar um produto. |
| `/produtos/<id>/editar/` | Editar o produto identificado pelo ID. |
| `/produtos/<id>/excluir/` | Confirmar a exclusão do produto identificado pelo ID. |
| `/admin/` | Acessar o painel administrativo. |

## Verificação manual

O fluxo funcional pode ser conferido pelos seguintes passos:

1. Cadastrar um produto e verificar sua presença na listagem.
2. Editar seu preço e confirmar a atualização sem duplicação do registro.
3. Abrir a exclusão e cancelar, verificando que o produto permanece cadastrado.
4. Confirmar a exclusão e verificar sua remoção da listagem.

## Escopo e limitações

Esta versão tem finalidade educacional e foi desenvolvida para execução local.

As páginas do CRUD ainda não possuem controle de acesso por usuário. O login do Django Admin protege apenas o painel administrativo.

A publicação em produção exige a implementação de autenticação e permissões nas páginas do CRUD, além da revisão das configurações de segurança e hospedagem.

## Melhorias planejadas

- [  :white_check_mark:  ] Aprimorar o layout e a adaptação para dispositivos móveis.
- [ :white_check_mark:  ] Adicionar pesquisa e paginação à listagem.
- [ ] Implementar autenticação e controle de acesso.
- [ ] Adicionar testes automatizados.
- [ ] Exibir mensagens de sucesso após as operações.

## Autor

**Edison Campos Cavalcante**  
Estudante de Ciência da Computação — UNINASSAU

[Perfil no GitHub](https://github.com/EdisonC-Dev)
