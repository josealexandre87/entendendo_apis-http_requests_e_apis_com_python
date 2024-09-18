import os

import dotenv
import requests
import streamlit as st

# Carrega as variáveis de ambiente do arquivo .env
dotenv.load_dotenv(dotenv.find_dotenv())

# Dicionário para tradução das descrições do clima retornadas pela API
dict_clima = {
    'céu limpo': 'Céu limpo ☀️',
    'algumas nuvens': 'Céu com algumas nuvens ⛅',
    'nublado': 'Nublado ☁️',
    'névoa': 'Névoa 🌫️',
}

# Função para fazer uma requisição HTTP e retornar os dados JSON
def fazer_request(url, params=None):
    resposta = requests.get(url=url, params=params)  # Realiza o GET request
    try:
        resposta.raise_for_status()  # Verifica se houve erro na requisição
    except requests.HTTPError as e:
        print(f"Erro no request: {e}")  # Log de erro em caso de falha
        resultado = None
    else:
        resultado = resposta.json()  # Converte a resposta para JSON
    return resultado  # Retorna o resultado da requisição
#---

# Função para pegar os dados do tempo para uma localidade específica
def pegar_tempo_para_local(local):
    app_id = os.environ['CHAVE_API_OPENWEATHER']  # Obtém a chave da API do OpenWeather do arquivo .env
    url = f"https://api.openweathermap.org/data/2.5/weather"  # URL da API
    params = {
        'q': local,        # Cidade/localidade
        'appid': app_id,   # Chave da API
        'units': 'metric', # Unidades métricas (Celsius)
        'lang': 'pt_br',   # Idioma (português)
    }
    dados_tempo = fazer_request(url=url, params=params)  # Faz a requisição e retorna os dados do tempo
    return dados_tempo
# ---

# Função principal para rodar o app Streamlit
def main():
    # Cabeçalho do Web App
    st.title('Web App Tempo ☀️')  # Título do aplicativo
    st.write('Dados do OpenWeather (fonte: https://openweathermap.org/current)')  # Fonte de dados

    # Campo de entrada de texto para o usuário digitar uma cidade
    local = st.text_input('Busque uma cidade:')
    if not local:  # Se o campo estiver vazio, para a execução
        st.stop()

    # Acessa dados do OpenWeather para a localidade inserida
    dados_tempo = pegar_tempo_para_local(local=local)
    if not dados_tempo:  # Se não houver dados para a localidade
        st.warning(f'Localidade "{local}" não foi encontrada no banco de dados da OpenWeather!')
        st.stop()

    # Extrai os dados retornados para variáveis
    clima_atual = dados_tempo['weather'][0]['description']  # Descrição do clima
    clima_atual = dict_clima.get(clima_atual, clima_atual)  # Traduz a descrição do clima
    temperatura = dados_tempo['main']['temp']  # Temperatura atual
    sensacao_termica = dados_tempo['main']['feels_like']  # Sensação térmica
    umidade = dados_tempo['main']['humidity']  # Umidade do ar
    cobertura_nuvens = dados_tempo['clouds']['all']  # Cobertura de nuvens

    # Exibe os dados no Web App
    st.metric(label='Tempo atual', value=clima_atual)  # Exibe o clima atual
    col1, col2 = st.columns(2)  # Cria duas colunas para exibir dados
    with col1:
        st.metric(label='Temperatura', value=f'{temperatura} °C')  # Exibe a temperatura
        st.metric(label='Sensação térmica', value=f'{sensacao_termica} °C')  # Exibe a sensação térmica
    with col2:
        st.metric(label='Umidade do ar', value=f'{umidade}%')  # Exibe a umidade do ar
        st.metric(label='Cobertura de nuvens', value=f'{cobertura_nuvens}%')  # Exibe a cobertura de nuvens
# ---

# Ponto de entrada do programa
if __name__ == '__main__':
    main()  # Executa a função principal