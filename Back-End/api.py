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
def inserir_produtos(nome:str, categoria:str , preco:float , quantidade:int):
    funcao.inserir_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adcionado com sucesso!"}


@app.get("/produto/{id_produto}")
def consultar_produto(id_produto: int):
    produto = funcao.buscar_produto_por_id(id_produto)
    if produto:
        return {"id": produto[0], "nome": produto[1], "categoria": produto[2], "preco": produto[3], "quantidade": produto[4]}
    else:
        return {"erro": "Produto não encontrado"}


@app.get("/produto")
def listar_produto():
    produto = funcao.listar_produtos()
    if produto:
        lista = []
        for linha in produto:
            lista.append({
                "id": linha[0],
                "nome": linha[1],
                "categoria": linha[2],
                "preco": linha[3],
                "quantidade": linha[4]
            })
        return {"produtos": lista}
    else:
        return {"mensagem": "Nenhum produto encontrado"}




@app.put("/produtos/{id_produtos}")
def update_produtos(id_produtos: int, novo_preco: float):
    produto = funcao.buscar_quantidade_e_preco(id_produtos)
    if produto:
        funcao.atualizar_produto(id_produtos, novo_preco)
        return {"mensagem": "Produto atualizado com sucesso!"}
    else:
        return { "erro":"Produto não encontrado"}
    
@app.delete("/deletar/{id_produto}")
def deletar_produto(id_produto: int):
    deletar = funcao.deletar_produtos(id_produto)
    if deletar:
        return {"mensagem": "Produto deletado com sucesso!"}
    else:
        return {"erro": "Não foi possível deletar o produto"}

