# 🐍 Python & 🎲 SQLite

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-for-VSCode](https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg)](https://code.visualstudio.com/)
[![GitHub license](https://img.shields.io/github/license/devscie/PythonConnectDb)](https://github.com/devscie/PythonConnectDb/blob/master/LICENSE)

## 💻 Sobre o projeto

Utilizar um único arquivo, usando classes e métodos para realizar o CRUD num banco de dados SQLite3 usando o Python.

Tabela clientes
___

Campo     | Tipo       | Tipo
--------- | ---------- | ----------
id        | inteiro    | sim
nome      | texto      | sim
idade     | inteiro    | não
cpf       | texto (11) | sim
email     | texto      | sim
fone      | texto      | não
cidade    | texto      | não
uf        | texto (2)  | sim
criado_em | data       | sim
bloqueado | boleano    | não

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [SQLite](https://www.sqlite.org/)

Índice de conteúdos
=================
<!--ts-->
   * [Conectando e desconectando do banco](https://github.com/devscie/PythonConnectSQLite/blob/master/connect_db.py)
   * [Criando um banco de dados](https://github.com/devscie/PythonConnectSQLite/blob/master/manager_db.py)
   * [Inserindo valores randômicos](https://github.com/devscie/PythonConnectSQLite/blob/master/gen_random_values.py)
   * [gerar dados randômicos para novos clientes](https://github.com/devscie/PythonConnectSQLite/blob/master/gen_csv.py)
   * [Comandos]
      * [Create - Inserindo 1 registro com comando SQL]
      * [Create - Inserindo N registros com uma tupla de dados]
      * [Importando dados de um arquivo csv]
      * [Create - Inserindo 1 registro com parâmetros de entrada]
      * [Inserindo valores randômicos]
      * [Read - Lendo os dados]
      * [SELECT]
      * [SELECT Personalizado]
      * [Update - Alterando os dados]
      * [Delete - Deletando os dados]
      * [Alter - Adicionando uma nova coluna]
      * [Lendo as informações do banco de dados]
      * [Fazendo backup do banco de dados (exportando dados)]
      * [Recuperando backup do banco de dados (importando dados)]
   * [License](https://github.com/devscie/PythonConnectSQLite/blob/master/LICENSE)
<!--te-->

### Features

- [x] Cadastrar usuário
- [x] Visualizar usuário
- [x] Atualizar usuário
- [x] Deletar usuário
- [x] Módulo datetime - Retornar a data e hora local atual

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Python](https://www.python.org/). 
Além disso um bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

### 💻 Rodando

```bash
# Clone este repositório
$ git clone <https://github.com/devscie/PythonConnectSQLite>

# Crie o virtualenv com o nome python-sqlite
$ virtualenv PythonConnectSQLite

# Habilite o python3
$ $ virtualenv -p /usr/bin/python3 PythonConnectSQLite

# Acesse a pasta do projeto
$ cd PythonConnectSQLite

# Ative o ambiente
$ source bin/activate

# Instale as dependências
$ pip install -r requirements.txt

# Conectando e desconectando do banco
$ python3 connect_db.py
$ ls *.db

## Modo interativo
$ python3
>>> from connect_db import Connect
>>> dir(Connect)
>>> db = Connect('clientes.db')
>>> dir(db)
>>> db.close_db()
>>> exit()

# Criando um banco de dados
$ python3 manager_db.py
$ ls *.db

## Modo interativo
$ python3
>>> from manager_db import *
>>> c = ClientesDb()
>>> exit()

# Criando uma tabela
$ sqlite3 clientes.db .tables

## Modo interativo
$ python3
>>> from manager_db import *
>>> c = ClientesDb()
>>> c.criar_schema()

# Inserindo um registro com parâmetros de entrada definido pelo usuário
$ python3
>>> from manager_db import *
>>> c = ClientesDb()
>>> c.criar_schema()
>>> c.inserir_com_parametros()
Nome: xxxxxxxx
Idade: xx
CPF: xxxxxxxxxxx
Email: xxxxxxxx
Fone: xxxxxxxxx
Cidade: xxxxxxxx
UF: xx

# Chamada a função:

## Contar os clientes maiores que 18 anos de idade.
$ c.contar_cliente_por_idade(18)

## função atualizar para localizar o cliente(id)
$ c.atualizar(10)

## função deletar para deletar o cliente(id)
$ c.deletar(10)

## obter informações da tabela
$ c.table_info()

## obter lista de tabelas do db
$ c.table_list()

## exportando bando de dados
$ c.backup('sql/clientes_backup.sql')

## ler arquivo gravado
c.ler_arquivo('sql/clientes_maior18.sql')

# Chamando no modo interativo

>>> from manager_db import *
>>> p = PessoasDb()
>>> p.criar_schema()
>>> p.inserir_de_csv()
>>> p.gen_cidade()
>>> p.inserir_randomico(100)
>>> p.imprimir_todas_pessoas()
>>> p.meu_select()
>>> p.table_list()
>>> p.fechar_conexao()

```

###	🚧 Python & SQLite (Em construção) 🚧

### Como contribuir para o projeto

1. Faça um **fork** do projeto.
2. Crie uma nova branch com as suas alterações: `git checkout -b my-feature`
3. Salve as alterações e crie uma mensagem de commit contando o que você fez: `git commit -m "feature: My new feature"`
4. Envie as suas alterações: `git push origin my-feature`
>> Caso tenha alguma dúvida confira este [guia de como contribuir no GitHub](https://github.com/firstcontributions/first-contributions)


## Licença

Este projeto esta sobe a licença MIT.

## Autor

<img src="https://avatars3.githubusercontent.com/u/78492236" width="100px;" alt="Avatar" style="border-radius: 50%;">
<b>Vinicius George dos Santos</b>
<br /><br />

👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Vinicius-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/vinicius-george-dos-santos-932b29167/)](https://www.linkedin.com/in/vinicius-george-dos-santos-932b29167/) 
[![Gmail Badge](https://img.shields.io/badge/-devscient@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:devscient@gmail.com)](mailto:devscient@gmail.com)
