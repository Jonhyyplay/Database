# Gerenciador de Dados Pessoais em SQLite, em Python

## Sobre o Projeto

Estes códigos, composto por três scripts Python, permite a criação, inserção, deleção e atualização de registros em um banco de dados local. É uma ferramenta simples que ainda será melhorada.

## Como Funciona?

*   ### _Criação da Base_: Ao executar o `dataBank(INSERIR).py` pela primeira vez, o banco de dados `dataBank.db` e a tabela `pessoas` são criados automaticamente, caso ainda não existam.
*   ### _Inserção de Novos Registros_: Também com o `dataBank(INSERIR).py`, você pode adicionar novas entradas à tabela, fornecendo nome, idade e email.
*   ### _Remoção de Dados_: O script `dataBank(DELETE).py` permite a exclusão de registros com base na idade, oferecendo controle preciso sobre seus dados.
*   ### _Atualização de Dados_: O `dataBank(UPDATE).py` possibilita a modificação de informações existentes, como nome, idade ou email, com base em critérios de busca.

## Estrutura do Banco de Dados

O principal é o banco de dados `dataBank.db`, que contém a tabela `pessoas` com a seguinte estrutura:

*   `name`: Texto (nome da pessoa).
*   `age`: Inteiro (idade da pessoa).
*   `email`: Texto (email da pessoa).

## Tecnologias Utilizadas

*   ### _Python_: A linguagem de programação que dá vida ao projeto, com sua sintaxe clara e poderosa.
*   ### _SQLite_: O banco de dados leve e eficiente que armazena as informações de forma local.
