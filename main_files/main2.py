import sqlite3
from dotenv import dotenv_values
from time import sleep
from os import system
from datetime import date, datetime
from crud_paciente import create_table_paciente, insert_values_into_paciente, find_paciente, update_paciente, delete_paciente

system('cls')

# cria conexão com o banco
def connect_db(path_db:str) -> sqlite3.Connection :
    "this connect to db that you want, inform the: .db"
    #print('conectado.')
    try:
        conn = sqlite3.connect(path_db)
    except Exception as ex:
        print(ex)
    return conn

# caminho do banco 
def route_db():
    config = dotenv_values('.env.ambient')
    path_db = config.get('hospital')
    return path_db

# insere valores do medico na tabela medico dentro do banco
def insert_values_into_medico(cursor):
    nome = input("nome do médico: ")
    crm = input("número do CRM: ")
    query = f"""INSERT INTO {'Medico'}(Nome,CRM) VALUES('{nome}','{crm}');"""
    cursor.execute(query)

# insere valores do paciente na tabela historico clinico dentro do banco
def insert_values_into_historico_clinico(cursor):
    id_paciente = int(input('id paciente: '))
    doenca = input('doença(s): ')
    alergia = input('alergia(s): ')
    medicacao = input('remédios: ')
    values = (id_paciente,doenca,alergia,medicacao)
    query = f"""INSERT INTO {'Historico_Clinico'}(ID_Paciente,Doenca,Alergia,Medicacao)
    VALUES ('{values[0]}','{values[1]}','{values[2]}','{values[3]}'); """
    cursor.execute(query)

# insere valores do paciente na tabela prontuario dentro do banco
def insert_values_into_prontuario(cursor):
    id_paciente = int(input('id paciente: '))
    id_medico = int(input('id médico: '))
    id_h_clinico = int(input('id histórico clinico: '))
    descricao = input('descreva os sintomas que o paciente apresenta: ')
    data_atual = date.today()
    dt_atendimento = f"{str(data_atual.day)}/{str(data_atual.month)}/{str(data_atual.year)}"
    values = (id_paciente, id_medico, id_h_clinico, dt_atendimento)
    query = f"""INSERT INTO {'Prontuario'}(ID_Paciente, ID_Medico, ID_Historico_Clinico, Descricao, Data_Atendimento)
    VALUES ('{values[0]}','{values[1]}','{values[2]}','{values[3]}'); """
    cursor.execute(query)

# procura médicos que tenham o nome informado e com possibilidade de mostrar mais 5 resultados se existir
def find_medico(cursor):
    nome = input('nome do médico: ')
    query = f"SELECT * FROM Medico WHERE LOWER(Nome) like LOWER('%{nome}%');"
    question = 'S'
    while question == 'S':
        results = (cursor.fetchmany(5))
        for c in results:
            print(c, end='\n')
        if results == []:
            print('sem mais resultados.')
            question = 'n'
        question = input('mostrar mais 5 resultados[S]? ').strip().upper()[0]

def update_medico(cursor):
    ID = input('Informe o ID do médico: ')
    column = input("Informe o campo a receber atualização:")
    valor = input("o novo valor: ")
    cursor.execute(f"UPDATE Paciente SET {column} = '{valor}' WHERE ID = {int(ID)};")
    print(f'o registro da coluna {column} foi atualizado para o novo valor {valor}.')

# mostra tabelas disponíveis
def main_menu():
    menu = """
    1 - acessar registro de pacientes
    2 - acessar registro de médicos
    3 - acessar registro de histórico clínico
    4 - acessar registro de prontuário
    """
    print(menu)

# mostra as operações disponíveis
def options():
    menu = """
    1 - criar registro na tabela
    2 - consultar registros na tabela
    3 - Atualizar registro na tabela
    4 - Deletar registro na tabela
    5 - Mostrar todos os registros
    6 - Encerrar programa
    """
    print(menu)

# mostra todos os valores da tabela 
def show_all(cursor):
    cursor.execute('SELECT * FROM Paciente;')
    results = cursor.fetchall()
    if results == []:
        print('\nnenhum registro.')
    return results

# fecha a conexão com o banco
def conn_close(conn):
    if conn:
        conn.close()


if __name__ == "__main__":

    conn = connect_db("Hospital.db")
    cur = conn.cursor()
    fk = cur.execute('PRAGMA foreign_keys = ON;')
    create_table_paciente(cursor=cur)
    create_table_medico(cursor=cur)
    create_table_historico_clinico(cursor=cur)
    create_table_prontuario(cursor=cur)
    conn_close(conn)

    while True:        
        try:
            
            conn = connect_db("Hospital.db")
            cur = conn.cursor()
            print("\nBem-Vindo ao controle de registros do hospital.")
            #main_menu()
            options()
            option = input("digite sua opção: ").strip()
            
            if option == '1':
                sql = insert_values_into_paciente()
                cur.execute(sql)

            elif option == '2':
                pacientes = find_paciente(cursor=cur)
                for c in pacientes:
                    print(c)
            
            elif option == '3':
                paciente = update_paciente(cursor=cur)
                #for c in paciente:
                #    print(c)
                  

            elif option == '4':
                del_paciente(cursor=cur)
                
            elif option == '5':
               lista = show_all(cursor=cur)
               for c in lista:
                print(c)

            elif option == '6':
                print('programa finalizado.')
                conn_close(conn)
                sleep(1)
                break
                exit()

            else:
                option = input("opção inválida, digite novamente: ")
            
            conn.commit()

        except Exception as ex:
            print(ex)
            conn.rollback()
            
        finally:
            conn_close(conn)
