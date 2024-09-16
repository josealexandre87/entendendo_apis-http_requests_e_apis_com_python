from pprint import pprint

import pandas as pd
import requests
import streamlit as st


# --- Requisição ---
def fazer_request(url, params=None):
    resposta = requests.get(url, params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro na requisição: {e}')
        resultado = None
    else:
        resultado = resposta.json()
    return resultado
# --- ---

# --- Acesso aos Dados do IBGE ---
def pegar_nome_por_decada(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    dados_decadas = fazer_request(url=url)
    if not dados_decadas:
        return {}
    dict_decadas = {}
    for dados in dados_decadas[0]['res']:
        decada = dados['periodo']
        quantidade = dados['frequencia']
        dict_decadas[decada] = quantidade
    return dict_decadas
# --- ---

# --- App ---
def main():
    st.title('Web App Nomes')
    st.write('Dados do IBGE (fonte: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2)')
    
    nome = st.text_input('Consulte um nome: ')
    if not nome:
        st.stop()
    
    dict_decadas = pegar_nome_por_decada(nome)
    if not dict_decadas:
        st.warning(f'Nenhum dado encontrado para o nome {nome}')
        st.stop()
        
    df = pd.DataFrame.from_dict(dict_decadas, orient="index")
    
    col1, col2 = st.columns([0.3, 0.7]) # a col1 30% e a col2 70% da página
    with col1:
        st.write('Frequência por Década')
        st.dataframe(df)
    with col2:
        st.write('Evolução no Tempo')
        st.line_chart(df)
# --- ---

# --- # executar no python --- 
if __name__ == '__main__':
    main()
    
# --- OU --- executar no terminal o comando: streamlit run {nome-do-arquivo} ---