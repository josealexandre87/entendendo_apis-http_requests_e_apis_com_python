# ESSA NÃO É A FORMA MAI SEGURA DE SE FAZER AUTENTICAÇÃO, MAS É UM EXEMPLO SIMPLES PARA ENTENDER O QUE ESTÁ ACONTECENDO!

import base64
from pprint import pprint

import requests

usuario = "meu-usuario"
senha = "senha-secreta"

auth_strig = f"{usuario}:{senha}".encode() # .encode transforma em bits
auth_strig = base64.b64encode(auth_strig) # usa base64 para codificar (fica um b' na frente do código -> b'bWV1LXVzdWFyaW86c2VuaGEtc2VjcmV0YQ==')
auth_strig = auth_strig.decode() # destransforma em string para poder usar

url = "https://httpbin.org/basic-auth/meu-usuario/senha-secreta" # URL de Testes

# Parâmetros para a Autenticação
headers = {
    'Authorization': f'Basic {auth_strig}' # o servidor vai entender com essa autenticação Basic.
}

#Bloco de Requisição + Parâmetros
resposta = requests.get(url=url, headers=headers)
#---

# Bloco de Tratamento de Erro
try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(F'Erro na requisição:{e}')
    resultado = None
else:
    resultado = resposta.json() # Converte a resposta para um dicionário Python
# ---

# Se não houver erros, extrai a resposta JSON e exibe com pprint.
# O pprint é útil para exibir a resposta de forma estruturada e legível.
# Exibe os dados de forma mais legível com pprint
pprint(resultado) # RESPOSTA ESPERADA: {'authenticated': True, 'user': 'meu-usuario'}