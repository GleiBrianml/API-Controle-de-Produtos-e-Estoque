from fastapi import FastAPI
import funcao
# python -m uvicorn api:app --reload
#Testar api Fastapi
# /docs > Documentação Swagger 
# /redoc > Documentação
#inciar o fastapi
app = FastAPI(title="Gerenciador de Estoque e Produtos")


@app.get("/")
def home():
    return {"mensagem": "Bem-vindos ao gerenciador de estoque"}

@app.post("/produto")
def inserir_produtos(nome:str, categoria:str , preco:float , quantidade:float):
    funcao.inserir_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adcionado com sucesso!"}

