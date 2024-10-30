# HookLab
Desafio técnico para vaga de desenvolvedor na HookLab

# Desafio de Web Scraping e Análise de Dados com Python

Olá! Estou muito empolgado por ter a oportunidade de participar deste desafio. Este repositório contém minhas soluções para as questões propostas no teste de conhecimento em Web Scraping e Análise de Dados com Python. Cada etapa foi projetada para demonstrar minhas habilidades e a capacidade de desenvolver soluções eficazes e criativas.

## Introdução

Neste projeto, desenvolvi quatro scripts que abrangem diferentes aspectos de web scraping e análise de dados. Abaixo, você encontrará uma descrição de cada etapa, bem como as instruções para executar os scripts. Para baixar este reposióritio basta ter o GIT instalado e executar o comando:
```bash
git clone https://github.com/RafaelSteffens/HookLab.git
```

Para executar os scripts basta ter o python instalado e rodar o comando por script, segue exemplo de como executar o script 1:
```bash
python etapa1
```
## Etapas Desenvolvidas

1. **Web Scraping do Reddit**
   - Neste script, utilizei as bibliotecas `Requests`, `pandas` e `BeautifulSoup` para extrair o título, up votes e link das três primeiras postagens do subreddit `r/programming`. Os dados coletados são salvos em um arquivo CSV, permitindo uma fácil análise posterior.

2. **Extração de Ofertas de um E-commerce**
   - Aqui, li os dados de um arquivo `api_response.json`, que contém informações de ofertas de um e-commerce. O objetivo foi extrair atributos essenciais, como `offer_link`, `image_link`, `price` e `title`, estruturando tudo de forma clara.

3. **Captura de Informações de Produtos**
   - Este script utiliza a biblioteca Selenium e captura informações detalhadas de um produto específico no site `https://www.magazineluiza.com.br/`, extraindo os atributos `title`, `stock_availability` e `price`, e organizando-os em um formato JSON.

4. **Análise de Dados de Compras**
   - Neste desafio, realizei uma análise abrangente dos dados de compras a partir do arquivo `dados_compra.json`. Utilizando a biblioteca `Pandas`, explorei as informações, calculei métricas importantes e visualizei os dados de maneira a revelar insights valiosos sobre o comportamento de compra dos consumidores.

## Instruções para Execução

Para executar os scripts, você precisará ter o ambiente Python configurado com as bibliotecas necessárias instaladas. 

Você pode instalar as bibliotecas necessárias usando o comando:

```bash
pip install -r requirements.txt
