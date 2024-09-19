import os
import sys
from pprint import pprint

import dotenv
import requests
from requests.auth import HTTPBasicAuth  # Módulo para autenticação HTTP básica

# Carrega as variáveis de ambiente a partir do arquivo .env
dotenv.load_dotenv(dotenv.find_dotenv())

# Request de autenticação
url = "https://accounts.spotify.com/api/token"  # URL para obter o token de autenticação
body = {
    'grant_type': 'client_credentials',  # Tipo de grant para pegar token baseado nas credenciais do cliente
}
# Obtém as credenciais da API Spotify a partir do arquivo .env
usuario = os.environ['SPOTIFY_CLIENT_ID']
senha = os.environ['SPOTIFY_CLIENT_SECRET']
auth = HTTPBasicAuth(username=usuario, password=senha)  # Cria a autenticação básica com o usuário e senha
# Faz a requisição POST para obter o token de acesso
resposta = requests.post(url=url, data=body, auth=auth)

# Verifica se houve algum erro na requisição
try:
    resposta.raise_for_status()  # Levanta uma exceção se a requisição falhou
except requests.HTTPError as e:
    print(f"Erro no request: {e}")  # Mostra o erro ocorrido
    token = None  # Se houver erro, define o token como None
else:   # Se foi bem-sucedida, extrai o token de acesso do corpo da resposta    
    token = resposta.json()['access_token']
    print('Token obtido com sucesso!')
if not token:   # Se não for possível obter o token, encerra o programa
    sys.exit()  # Encerra a execução do programa

# Request de busca de dados do artista
id_artista = '246dkjvS1zLTtiykXe5h60'  # ID do artista no Spotify
url = f'https://api.spotify.com/v1/artists/{id_artista}'  # URL para buscar os dados do artista
headers = {
    'Authorization': f'Bearer {token}'  # Passa o token de autenticação no cabeçalho da requisição
}

# Faz a requisição GET para obter os dados do artista
resposta = requests.get(url=url, headers=headers)
# Exibe os dados retornados de forma legível no console
pprint(resposta.json())
