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

elif menu == "Adicionar produto":
    st.subheader("➕ Adicionar produtos")
    nome = st.text_input("Nome do produto")
    categoria = st.text_input("Categoria do produto")
    preco = st.number_input("Preço do produto", step=0.5)
    quantidade = st.number_input("Quantidade", step=1)
    if st.button("Salvar Produto"):
        dados = {"nome": nome, "categoria":categoria, "preco":preco, "quantidade": quantidade}
        response = requests.post(f"{API_URL}/filmes", params=dados)
        if response.status_code == 200:
            st.success("Filme adicionando com sucesso!")
        else:
            st.error("Erro ao adicionar o filme")