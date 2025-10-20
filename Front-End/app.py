import streamlit as st
import requests

#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

#python -m streamlit run app.py

st.set_page_config(page_title="Gerenciador de Estoque", page_icon="🚛")
st.title("📦 Gerenciador de Estoque")

#Menu lateral
menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar produtos", "Atualizar produtos"])

if menu == "Catalogo":
    st.subheader("Todos os produtos disponiveis")
    response = requests.get(f"{API_URL}/produto")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
    else:
        st.error("Erro ao acessar a API")

