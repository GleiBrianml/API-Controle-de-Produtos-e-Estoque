import streamlit as st
import requests
import pandas as pd
#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

#python -m streamlit run app.py

st.set_page_config(page_title="Gerenciador de Estoque", page_icon="🚛")
st.title("📦 Gerenciador de Estoque")

#Menu lateral
menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar produto", "Atualizar produto","Buscar Estoque", "Deletar produto"])

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


elif menu == "Adicionar produto":
    st.subheader("➕ Adicionar produtos")
    nome = st.text_input("Nome do produto")
    categoria = st.text_input("Categoria do produto")
    preco = st.number_input("Preço do produto", step=0.1)
    quantidade = st.number_input("Quantidade", step=1)
    if st.button("Salvar Produto"):
        dados = {"nome": nome, "categoria":categoria, "preco":preco, "quantidade": quantidade}
        response = requests.post(f"{API_URL}/produto", params=dados)
        if response.status_code == 200:
            st.success("Produto adicionando com sucesso!")
        else:
            st.error("Erro ao adicionar o Produto")



elif menu == "Atualizar produto":
    st.subheader("🔁 Atualizar Produtos")
    id_produtos = st.number_input("Id do Produto", min_value=1, step=1)

    if id_produtos > 0:
        # Buscar dados do produto
        response = requests.get(f"{API_URL}/produto/{id_produtos}")
        if response.status_code == 200:
            produto = response.json()
            if "erro" not in produto:
                # Mostrar apenas o nome e o preço atual
                dados = {
                    "Nome": [produto["nome"]],
                    "Preço atual (R$)": [produto["preco"]]
                }
                df = pd.DataFrame(dados)
                st.dataframe(df)

                # Campo para novo preço
                preco = st.number_input("Novo preço do produto", step=0.5, value=produto["preco"])

                if st.button("Salvar Produto"):
                    response = requests.put(
                        f"{API_URL}/produtos/{id_produtos}",
                        params={"novo_preco": preco}
                    )
                    if response.status_code == 200:
                        st.success("Produto atualizado com sucesso!")
                    else:
                        st.error("Erro ao atualizar produto")
            else:
                st.warning("Produto não encontrado.")
        else:
            st.error("Erro ao consultar o produto.")

elif menu == "Buscar Estoque":
    st.subheader(" 🛒 Buscar no Estoque ")
    id_produto = st.number_input("Digite o ID do produto para busca-lo:", min_value=1, step=1)
    if st.button("Buscar produto"):
        if id_produto > 0:
            url = f"{API_URL}/buscar"
            response = requests.get(url, params={"id_produto": id_produto})
            if response.status_code == 200:
                produto = response.json().get("produto")  
                if produto:
                    st.write("Produto encontrado:")
                    st.dataframe(produto)
                    st.success("Produto encontrado com sucesso!")
                else:
                    st.warning("Produto não encontrado.")
        else:
            st.error("Digite um ID de produto válido (maior que 0).")



if menu == "Deletar produto":
    st.subheader("❌ Deletar produto")
    id_produto = st.number_input("Id do produto para deletar", min_value=1, step=1)

    if id_produto > 0:
        response = requests.get(f"{API_URL}/produto/{id_produto}")
        if response.status_code == 200:
            produto = response.json()
            if "erro" not in produto:
                dados = {
                    "Nome": [produto['nome']],
                    "Categoria": [produto['categoria']],
                    "Preço (R$)": [produto['preco']],
                    "Quantidade": [produto['quantidade']]
                }
                df_produto = pd.DataFrame(dados)
                st.dataframe(df_produto)

                if st.button("Deletar Produto"):
                    response_delete = requests.delete(f"{API_URL}/deletar/{id_produto}")
                    if response_delete.status_code == 200:
                        st.success("Produto deletado com sucesso!")
                    else:
                        st.error("Erro ao deletar o produto.")
            else:
                st.warning("Produto não encontrado.")
        else:
            st.error("Erro ao consultar o produto.")

