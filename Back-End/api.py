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



