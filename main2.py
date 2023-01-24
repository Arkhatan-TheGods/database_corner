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

def create_table_paciente(cursor):
    columns = ["Nome","CPF","Data_Nascimento","Endereco"]
    query = """CREATE TABLE IF NOT EXISTS {}(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, {});
    """.format("Paciente", "Nome TEXT NOT NULL, CPF TEXT NOT NULL, Data_Nascimento TEXT NOT NULL, Endereco TEXT NOT NULL ")
    cursor.execute(query)

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

def find_paciente(cursor):
    paciente_nome = input("nome do paciente: ")
    query = f"SELECT * FROM Paciente WHERE LOWER(Nome) LIKE LOWER('%{paciente_nome}%');"
    cursor.execute(query)
    #print(cursor.fetchone())
    results =(cursor.fetchmany(1))
    #print(type(results))
    for c in results:
        print(c, end='\n')
    question = input('mostrar mais 5 resultados[S]? ').strip().upper()[0]
    while question == 'S':
        results =(cursor.fetchmany(1))
        for c in results:
            print(c, end='\n')
        question = input('mostrar mais 5 resultados[S]? ').strip().upper()[0]
        if results == []:
            print('sem mais resultados.')
            question = 'n'
    #print(cursor.fetchall())
    # if cursor.fetchmany(5) == () and []:
    #     print('nenhum cadastro encontrado.')
    # else:
    #     print(cursor.fetchmany(2))

    # question = input("para mostrar mais resultados digite S: ").strip().upper
    # if question == 'S':
    #     cursor.fetchmany(5)2

def update_paciente(cursor):
    ID = input("infome o ID do paciente:")
    column = input("Informe o campo a receber atualização:")
    valor = input("o novo valor: ")
    cursor.execute(f"UPDATE Paciente SET {column} = '{valor}' WHERE ID = {int(ID)};")
    print('valor atualizado', cursor.execute(f'SELECT * FROM Paciente WHERE ID = {int(ID)};'))

def del_paciente(cursor):
    ID = input('informe o ID a ser deletado: ')
    cursor.execute(f'SELECT * FROM Paciente WHERE ID = {int(ID)};')
    print('seguinte registro foi deletado: \n',cursor.fetchone())
    cursor.execute(f"DELETE FROM Paciente WHERE ID = {int(ID)}; ")

def main_menu():
    menu = """
    1 - criar registro na tabela
    2 - consultar registros na tabela
    3 - Atualizar registro na tabela
    4 - Deletar registro na tabela
    5 - Encerrar programa
    """
    print(menu)

def conn_close(conn):
    if conn:
        conn.close()


conn = connect_db("Hospital.db")
cur = conn.cursor()
create_table_paciente(cursor=cur)

while True:
    if __name__ == "__main__":

        try:
            
            conn = connect_db("Hospital.db")
            cur = conn.cursor()
            print("\nBem-Vindo ao controle de pacientes do hospital.")
            main_menu()
            option = input("digite sua opção: ")
            
            if option == '1':
                insert_values_into_paciente(cursor=cur)
            
            elif option == '2':
                find_paciente(cursor=cur)
             
            elif option == '3':
                update_paciente(cursor=cur)
                
            elif option == '4':
                del_paciente(cursor=cur)
                
            elif option == '5':
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
            print(ex)

        finally:
            conn_close(conn)
