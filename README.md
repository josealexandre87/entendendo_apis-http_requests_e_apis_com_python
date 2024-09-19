# Entendendo APIs - HTTP, Requests e APIs com Python

Bem-vindo ao repositório do curso "Entendendo APIs - HTTP, Requests e APIs com Python" da Asimov Academy. Este curso é voltado para iniciantes que desejam aprender a interagir com APIs utilizando Python, compreendendo o protocolo HTTP, criando requisições (Requests) e desenvolvendo Web Apps baseados em dados de APIs abertas e privadas.

## O que você vai aprender:
- Conceitos básicos sobre o funcionamento da Internet.
- Como funciona o protocolo HTTP e a anatomia de uma requisição.
- Compreensão dos códigos de status HTTP.
- O que são APIs e como acessá-las (REST).
- Utilização de parâmetros de URL e autenticação via chave ou token.
- Desenvolvimento de Web Apps utilizando dados reais, como popularidade de nomes e informações climáticas.
- Autenticação avançada usando JSON Web Tokens (JWTs).
  
## Projetos práticos incluídos:
- **Web App de Popularidade de Nomes do IBGE**: Acessa a API do IBGE para buscar a popularidade de nomes brasileiros.
- **Web App de Previsão do Tempo com OpenWeather**: Acessa a API OpenWeather para exibir informações climáticas de cidades.
- **Web App de Músicas Populares do Spotify**: Acessa a API do Spotify para listar as principais músicas de um artista.

## Estrutura do Curso:

### Módulo 1: Como a Internet Funciona
- Introdução ao curso e conceitos sobre HTTP.
- Primeiro Request HTTP utilizando Python.

### Módulo 2: Entendendo HTTP e Requests
- Anatomia de um Request.
- Análise de códigos de status HTTP.

### Módulo 3: Interfaces e APIs
- O que são interfaces e APIs.
- Introdução ao conceito de API REST.

### Módulo 4: Acessando APIs Abertas
- Como acessar APIs públicas.
- Introdução aos schemas de resposta e parâmetros de URL.
- [Miniprojeto] Web App de Popularidade de Nomes (IBGE).

### Módulo 5: Acessando APIs com Autenticação
- Autenticação básica em APIs privadas.
- Autenticação via chave API.
- [Miniprojeto] Web App de Previsão do Tempo (OpenWeather).

### Módulo 6: Autenticação via Token e Documentação
- Uso de tokens de autenticação.
- Documentação de APIs e uso de JWTs.
- [Miniprojeto] Web App com dados do Spotify.

## Como rodar os projetos

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/entendendo_apis-http_requests_e_apis_com_python.git
    ```

2. Adicione suas chaves de API em um arquivo `.env` com os seguintes parâmetros:
    ```
    SPOTIFY_CLIENT_ID=<sua-chave>
    SPOTIFY_CLIENT_SECRET=<sua-chave>
    OPENWEATHER_KEY=<sua-chave>
    ```

3. Execute os projetos em sua máquina:
    ```bash
    streamlit run web_app_ibge.py
    streamlit run web_app_open_weather.py
    streamlit run web_app_spotify.py
    ```

## Requisitos

- Python 3.12.x
- Streamlit
- Requests
- dotenv
