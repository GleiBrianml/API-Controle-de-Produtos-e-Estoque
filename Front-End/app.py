import streamlit as st
import requests

#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

#python -m streamlit run app.py

st.set_page_config(page_title="Gerenciador de Estoque", page_icon="🚛")
st.title("📦 Gerenciador de Estoque")

#Menu lateral
menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar produto", "Atualizar produto", "Deletar produto"])

if menu == "Catalogo":
    st.subheader("Todos os produtos disponiveis")
    response = requests.get(f"{API_URL}/produto")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nenhum produto cadastrado no momento.")
    else:
        st.error("Erro ao acessar a API")


if menu == "Adicionar produto":
    st.subheader("➕ Adicionar produtos")
    nome = st.text_input("Nome do produto")
    categoria = st.text_input("Categoria do produto")
    preco = st.number_input("Preço do produto", step=0.5)
    quantidade = st.number_input("Quantidade", step=1)
    if st.button("Salvar Produto"):
        dados = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        response = requests.post(f"{API_URL}/produto", json=dados)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar o produto")



if menu == "Atualizar produto":
    st.subheader("🔁 Atualizar produtos")
    id_produto = st.number_input("Id do produto", min_value=0, step=1)

    if id_produto > 0:
        # Consulta o produto para verificar se existe
        response = requests.get(f"{API_URL}/produto/{id_produto}")
        if response.status_code == 200:
            produto = response.json()
            if produto:
                st.write(f"Produto: {produto.get('nome')} - Categoria: {produto.get('categoria')}")
                preco = st.number_input("Preço em R$", min_value=0.0, value=produto.get('preco', 0.0), step=0.1)
                quantidade = st.number_input("Quantidade desse produto", min_value=1, value=produto.get('quantidade', 1), step=1)
                if st.button("Salvar Produto"):
                    dados = {"preco": preco, "quantidade": quantidade}
                    response_update = requests.put(f"{API_URL}/produto/{id_produto}", json=dados)
                    if response_update.status_code == 200:
                        st.success("Produto atualizado com sucesso!")
                    else:
                        st.error("Erro ao atualizar o produto.")
            else:
                st.warning("Produto não encontrado.")
        else:
            st.error("Erro ao consultar o produto.")
    else:
        st.info("Informe um ID válido para buscar o produto.")


if menu == "Deletar produto":
    st.subheader("❌ Deletar produto")
    id_produto = st.number_input("Id do produto para deletar", min_value=1, step=1)

    if id_produto > 0:
        # Consulta o produto para verificar se existe
        response = requests.get(f"{API_URL}/produto/{id_produto}")
        if response.status_code == 200:
            produto = response.json()
            if produto:
                st.write(f"Produto: {produto.get('nome')} - Categoria: {produto.get('categoria')} - Preço: R$ {produto.get('preco')} - Quantidade: {produto.get('quantidade')}")
                if st.button("Deletar Produto"):
                    response_delete = requests.delete(f"{API_URL}/produto/{id_produto}")
                    if response_delete.status_code == 200:
                        st.success("Produto deletado com sucesso!")
                    else:
                        st.error("Erro ao deletar o produto.")
            else:
                st.warning("Produto não encontrado.")
        else:
            st.error("Erro ao consultar o produto.")
