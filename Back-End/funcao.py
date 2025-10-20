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
                preco NUMERIC(10,2),
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

def listar_produtos():
    conexao,cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar os produtos {erro}")
        finally:
            cursor.close()
            conexao.close()
        
def atualizar_produto(id_produto, novo_preco, nova_quantidade):
    conexao,cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET preco = %s, quantidade = %s WHERE id = %s", 
                    (novo_preco,nova_quantidade,id_produto)
                
            )
            conexao.commit()
        except Exception as erro:
            print(f'Erro ao tentar atualizar o produto {erro}')
        finally:
            cursor.close()
            conexao.close()

def deletar_produtos(id_produto):
    conexao,cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM produtos WHERE id = %s", 
                    (id_produto,)    
            )
            conexao.commit()
        except Exception as erro:
            print(f'Erro ao tentar deletar o produto {erro}')
        finally:
            cursor.close()
            conexao.close()

def buscar_quantidade_e_preco(id_produto):
    conexao,cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT preco, quantidade FROM produtos WHERE id = %s",
                (id_produto,)
            )
            return cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao buscar o produto {erro}")
        finally:
            cursor.close()
            conexao.close()

print(buscar_quantidade_e_preco(1))