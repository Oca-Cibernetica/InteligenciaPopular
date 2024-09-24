# Inteligência Popular

Esta é uma biblioteca para acesso e análise de dados públicos do Brasil.

O objetivo é permitir que organizações populares possam extrair de bancos de dados públicos informações úteis tanto para seu planejamento interno quanto para a reivindicação de políticas públicas de seu interesse.

Os dados são convertidos para o tipo DataFrame, da biblioteca Pandas, para padronizar o formato dos dados e facilitar a análise.

## Participe também desse projeto!

Esse projeto é voltado para a organização popular portanto todas as pessoas, independente do nível de conhecimento das tecnologias envolvidas, são convidadas colaborar!

### Organize-se

Leve para a sua comunidade a ideia de se organizar com a tecnologia, talvez com a criação de um espaço hacker ou um telecentro. A ideia é criar um ambiente onde a troca criativa de conhecimentos possa se fundir com o debate crítico sobre as necessidades reais da sua comunidade!

### Use com a gente

Se você tem algum conhecimento de Python e análise de dados, você pode usar a Inteligência Popular para auxiliar no debate crítico e também na formulação de táticas de organização.

A partir disso, você pode contribuir diretamente com o projeto, nos contando na página de Issues do Github como podemos aprimorar continuamente a Inteligência Popular!

### Ponha as mãos da massa

Quer ir mais fundo? Que tal ajudar no desenvolvimento? Se você tem um pouco mais de conhecimento em Python, ciência de dados e machine learning, venha construir a Inteligência Popular com a gente!

## Preparando o ambiente

**TODO**

## Estado atual do desenvolvimento

Este projeto está apenas começando. Já é possível fazer consultas a duas APIs do IBGE: localidades e pesquisas agregadas. Na pasta `exemplos` existem alguns notebooks do Jupyter demonstrando e explicando as funcionalidades básicas:

* [Exemplo 1: Acessando a API de localidades do IBGE](exemplos/exemplo1_localidades.ipynb)
* [Exemplo 2: Acessando a API de pesquisas agregadas do IBGE](exemplos/exemplo2_agregados.ipynb)

Algumas funcionalidades são esperadas para a próxima versão:

* Configuração de outras APIs do IBGE
* Configuração de outras APIs públicas
* Funções para adicionar configurações de novas APIs
* Cache de requisições HTTP
* Testes unitários

Isso além, claro, de ouvir a comunidade sobre quais outras funcionalidades podemos incorporar.

Novos exemplos também estão nos planos, em especial demostrando o uso da biblioteca para:

* Selecionar e tratar os dados
* Fazer análises estatísticas e gerar gráficos
* Cruzar dados de diferentes APIs
* Predizer cenários com aprendizado de máquina
