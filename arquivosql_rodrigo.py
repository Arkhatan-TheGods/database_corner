import sqlite3
from sqlite3 import Error, Connection
from dotenv import dotenv_values


def connect_db(path_db: str): return sqlite3.connect(path_db)

def create_table(conn, table, columns):
    
    query = f"CREATE TABLE {table}(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,{columns}) ;"
    
    conn.execute(query)
    
    print('tabela criada.')

def insert_values(cursor, table, columns, values):

    select_all = f"SELECT * FROM Paciente; "

    cursor.execute(select_all)

    row_total = len(cursor.fetchall())

    query = f"INSERT INTO {table}({columns}) VALUES({values}); "

    cursor.execute(query)

    #conn.commit()

    cursor.execute(select_all)

    # len(cursor.fetchall()) == (row_total+1)
    
    #print(len(cursor.fetchall()) == (row_total+1))
    print('valores inseridos na tabela.')



if __name__ == "__main__":

    conn = None
    
    #PATH_DATABASE = "/home/rodrigo/python_projects/3.11.1/labpython/teste_lab.db"
    # config = dotenv_values('.env.ambient')
    # PATH__DATABASE = config.get('PATH_DATABASE')

    try:

        # config = dotenv_values('.env.ambient')
        
        # path_db = config.get(config)
    
        conn = connect_db('Hospital.db')

        cur = conn.cursor()

        create_table(cur,
                     "IF NOT EXISTS Paciente", "NOME TEXT NOT NULL, CPF TEXT NOT NULL, DATA_NASCIMENTO TEXT NOT NULL, ENDEREÇO TEXT NOT NULL")

        insert_values(cursor=cur,
                      table="Paciente",
                      columns="NOME,CPF,DATA_NASCIMENTO,ENDEREÇO",
                      values="'José Carlos', '987.654.321-00', '20/10/1990', 'Av. Paulista, São Paulo'")

        insert_values(cursor=cur,
                      table="Paciente",
                      columns="NOME,CPF,DATA_NASCIMENTO,ENDEREÇO",
                      values="'Jessica Santana', '123.456.789-12', '12/12/1999', 'Av. Brigadeiro, São Paulo'")


        conn.commit()

    except Exception as e:
    
        print("ERRO>>", e)
    
    finally:
        
        if conn:
            conn.close()

