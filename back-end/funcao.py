from conexao import conector

def criar_tabela():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS filmes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INT NOT NULL,
                nota FLOAT
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()

# def cadastrar_filme(titulo, genero, ano, nota):
#     conexao, cursor = conector()
#     if conexao:
#         try:
#             cursor.execute(
#                 "INSERT INTO filmes (titulo, genero, ano, nota) VALUES (%s,%s,%s,%s)",
#                 (titulo, genero, ano, nota)
#             )
#             conexao.commit()
#         except Exception as erro:
#             print(f"Erro ao cadastrar o filme {erro}")
#         finally:
#             cursor.close()
#             conexao.commit()
# cadastrar_filme("Era do gelo 3", "aventura","2009","9")

def listar_filmes():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
            "SELECT * FROM filmes ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar os filmes {erro}")
        finally:
            cursor.close()
            conexao.close()
        
print(listar_filmes())

def atualizar_filme(id_filme, nova_nota):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "UPDATE filmes SET nota = %s WHERE id = %s",
                (nova_nota, id_filme)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar nota do filme {erro}")
        finally:
            cursor.close()
            conexao.close()

print(atualizar_filme(10,2))

def deletar_filme(id_filme):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM filmes WHERE id = %s",
                (id_filme,)
            )
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"Filme removido com sucesso!")
            else:
                print("Nenhum filme foi encontrado com o ID fornecido.")
        except Exception as erro:
            print(f"Erro ao tentar deletar o filme {erro}")
        finally:
            cursor.close()
            conexao.close()

deletar_filme(3)