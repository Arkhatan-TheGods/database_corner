import sqlite3
from dotenv import dotenv_values
from time import sleep

# cria conexão com o banco
def connect_db(path_db:str):
    "this connect to db that you want, inform the: .db"
    print('conectado.')
    try:
        sqlite3.connect(path_db)
    except Exception as ex:
        print(ex)

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
    query = f"SELECT * FROM Paciente WHERE LOWER(Nome) LIKE LOWER(%{paciente_nome}%)"
    cursor.execute(query)
    print(cursor.fetchone())

    # question = input("para mostrar mais resultados digite S: ").strip().upper
    # if question == 'S':
    #     cursor.fetchmany(5)

def update_paciente(cursor):
    ID = input("infome o ID do paciente:")
    column = input("Informe o campo a receber atualização:")
    valor = input("o novo valor: ")
    cursor.execute(f"UPDATE Paciente SET {column} = '{valor}' WHERE ID = {ID};")
    print('valor atualizado')

def del_paciente(cursor):
    ID = input('informe o ID a ser deletado: ')
    cursor.execute(f"DELETE Paciente WHERE ID = {ID}; ")

def main_menu():
    return """
    1 - criar registro na tabela
    2 - consultar registro na tabela
    3 - Atualizar registro na tabela
    4 - Deletar registro na tabela
    5 - Encerrar programa
    """

conn = connect_db("Hospital.db")
cur = conn.cursor()
create_table_paciente(cursor=cur)

print("Bem-Vindo ao controle de pacientes do hospital.")

while True:
    if __name__ == "__main__":
                
        main_menu()
        option = "digite sua opção: "

        try:
            
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
                sleep(2) 
            else:
                while option not in ['1','2','3','4','5']:
                    option = input("opção inválida, digite novamente: ")
            conn.commit()

        except Exception as ex:
            print(ex)

        finally:
            if conn:
                conn.close()

exit()