# Raspador de Dados - Prefeitura de Rio Claro

Um projeto de automação desenvolvido em Python para facilitar o acesso à informação pública. Este script realiza web scraping no portal oficial da [Prefeitura Municipal de Rio Claro - SP](https://www.rioclaro.sp.gov.br/) e extrai as principais manchetes, avisos e links em destaque, entregando ao cidadão um arquivo PDF limpo e formatado.

## Objetivo
Evitar que o usuário se perca no excesso de informações do site institucional. O código compila os dados mais recentes diretamente da página inicial e gera um relatório "mastigado" em PDF.

## Tecnologias Utilizadas
* **Python 3**
* **Requests:** Para realizar as requisições HTTP e baixar o conteúdo da página.
* **BeautifulSoup4:** Para analisar e extrair as informações relevantes da estrutura HTML do site.
* **ReportLab:** Para a montagem e geração do documento PDF final.

## Como executar o projeto

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/pedroab1/trabalhoweb.git
   cd trabalhoweb
2. **Crie e ative um ambiente virtual**

   **No Windows:**
    ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   **No Linux/Mac:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
4. **Execute o script**
   ```bash
   python raspador_rioclaro.py
   ```
