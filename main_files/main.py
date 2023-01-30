import sqlite3
from dotenv import dotenv_values
from time import sleep
import os

os.system('cls')

# cria conexão com o banco
def connect_db(path_db:str):
    "this connect to db that you want, inform the: .db"
    #print('conectado.')
    try:
        conn = sqlite3.connect(path_db)
    except Exception as ex:
        print(ex)
    return conn

# cria tabela paciente no banco 
def create_table_paciente(cursor):
    query = """CREATE TABLE IF NOT EXISTS {}(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, {});
    """.format("Paciente", "Nome TEXT NOT NULL, CPF TEXT NOT NULL UNIQUE, Data_Nascimento TEXT NOT NULL, Endereco TEXT NOT NULL ")
    cursor.execute(query)

# insere valores do paciente na tabela paciente dentro do banco
def insert_values_into_paciente(cursor):
    nome = input("nome do paciente: ")
    cpf = input("CPF: ")
    dt_nasc = input("Data de nascimento(xx/xx/xxxx): ")
    endereco = input("Endereço: ")
    values = (nome,cpf,dt_nasc,endereco)
    query = f"""INSERT INTO {'Paciente'}({'Nome,CPF,Data_Nascimento,Endereco'})
    VALUES('{values[0]}', '{values[1]}', '{values[2]}', '{values[3]}'); """
    #.format("Paciente","Nome, CPF, Data_Nascimento, Endereco",values)
    cursor.execute(query)

# procura pacientes que tenham o nome informado e tem a possiblidade de mostrar mais 5 resultados
def find_paciente(cursor):
    paciente_nome = input("nome do paciente: ")
    query = f"SELECT * FROM Paciente WHERE LOWER(Nome) LIKE LOWER('%{paciente_nome}%');"
    cursor.execute(query)
    question = 'S'
    while question == 'S':
        results = (cursor.fetchmany(5))
        for c in results:
            print(c, end='\n')
        if results == []:
            print('sem mais resultados.')
            question = 'n'
        else:
            question = input('mostrar mais 5 resultados[S]? ').strip().upper()[0]

# atualiza registro do paciente a partir do ID que é fixo e único
def update_paciente(cursor):
    ID = input("infome o ID do paciente:")
    column = input("Informe o campo a receber atualização:")
    valor = input("o novo valor: ")
    cursor.execute(f"UPDATE Paciente SET {column} = '{valor}' WHERE ID = {int(ID)};")
    print(f'o registro da coluna {column} foi atualizado para o novo valor {valor}.')

# deleta registro do paciente permanentemente
def del_paciente(cursor):
    ID = input('informe o ID a ser deletado: ')
    cursor.execute(f'SELECT * FROM Paciente WHERE ID = {int(ID)};')
    print('seguinte registro foi deletado: \n',cursor.fetchone())
    cursor.execute(f"DELETE FROM Paciente WHERE ID = {int(ID)}; ")

# mostra as opções disponíveis
def main_menu():
    menu = """
    1 - criar registro na tabela
    2 - consultar registros na tabela
    3 - Atualizar registro na tabela
    4 - Deletar registro na tabela
    5 - Mostrar todos os registros
    6 - Encerrar programa
    """
    print(menu)

# mostra todos os valores da tabela paciente
def show_all(cursor):
    cursor.execute('SELECT * FROM Paciente;')
    results = cursor.fetchall()
    #print(type(results))
    for d in results:
        sleep(0.5)
        print(d)
    if results == []:
        print('\nnenhum registro.')

# fecha a conexão com o banco
def conn_close(conn):
    if conn:
        conn.close()


conn = connect_db("Hospital.db")
cur = conn.cursor()
create_table_paciente(cursor=cur)
conn_close(conn)

while True:
    if __name__ == "__main__":

        try:
            
            conn = connect_db("Hospital.db")
            cur = conn.cursor()
            print("\nBem-Vindo ao controle de pacientes do hospital.")
            main_menu()
            option = input("digite sua opção: ").strip()
            
            if option == '1':
                insert_values_into_paciente(cursor=cur)
            
            elif option == '2':
                find_paciente(cursor=cur)
             
            elif option == '3':
                update_paciente(cursor=cur)
                
            elif option == '4':
                del_paciente(cursor=cur)
                
            elif option == '5':
                show_all(cursor=cur)

            elif option == '6':
                print('programa finalizado.')
                conn_close(conn)
                sleep(1)
                break
                #os.system('cls')
                exit()

            else:
                option = input("opção inválida, digite novamente: ")
            
            conn.commit()

        except Exception as ex:
            print(type(ex))
            if ex == 'UNIQUE constraint failed: Paciente.CPF':
                print('Erro, CPF já cadastrado.')

        finally:
            conn_close(conn)
