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

@app.get("/produto")
def listar_produto():
    produto = funcao.listar_produtos()
    lista = []
    for linha in produto:
        lista.append({
                "id": linha[0],
                "nome": linha[1],
                "categoria": linha[2],
                "preco": linha[3],
                "avaliacao": linha[4]
            })
    return {"produtos":lista}

@app.put("/produtos/{id_produtos}")
def update_produtos(id_produtos: int, novo_preco: float, nova_quantidade):
    produto = funcao.buscar_quantidade_e_preco(id_produtos)
    if produto:
        funcao.atualizar_produto(id_produtos, novo_preco, nova_quantidade)
        return {"mensagem": "Produto atualizado com sucesso!"}
    else:
        return { "erro":"Produto não encontrado"}
    
@app.delete("/deletar")
def deletar_produto(id_produto):
    deletar = funcao.deletar_produtos(id_produto)
    if deletar:
        return {"mensagem": "Produto deletado com sucesso!"}
    else:
        return {"erro": "Não foi possivel deletar o produto"}
