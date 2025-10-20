from conexao import conectar

def criar_tabela():
    conexao,cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                categoria VARCHAR(50),
                preco DECIMAL(10,2),
                quantidade INT           
                )""")
                           
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.close()
criar_tabela()
def inserir_produto(nome, categoria, preco, quantidade):
    conexao,cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome,categoria,preco,quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir o produto/item {erro}")
        finally:
            cursor.close()
            conexao.close()

