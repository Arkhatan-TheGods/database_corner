import sqlite3
from sqlite3 import Error
from dotenv import dotenv_values

def connect_db():
    config = dotenv_values('.env.ambient')
    path_db = config.get("PATH_DATABASE")
    conn = None
    try:
        conn = sqlite3.connect(path_db)
        print('conectado')
    except Error() as er:
        print('>>>>>', er)
    return conn
    #conn.close()

# def cur():
#     cursor = connect_db().cursor()
#     return cursor

def create_table(table, columns):
    conn = connect_db()
    query = f"""CREATE TABLE {table}(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,{columns}) ;"""
    conn.cursor().execute(query)
    print('tabela criada.')

#create_table("IF NOT EXISTS Paciente", "NOME TEXT NOT NULL, CPF TEXT NOT NULL, DATA_NASCIMENTO TEXT NOT NULL, ENDEREÇO TEXT NOT NULL")

def insert_values(table, columns, values):
    select_all = f"SELECT * FROM Paciente; "
    #conn = connect_db()
    cursor = connect_db().cursor()
    cursor.execute(select_all)
    row_total = len(cursor.fetchall())
    #print(row_total)
    query = f"INSERT INTO {table}({columns}) VALUES({values}); "
    cursor.execute(query)
    #conn.commit()
    cursor.execute(select_all)
    len(cursor.fetchall()) == (row_total+1)
    #print(len(cursor.fetchall()) == (row_total+1))
    print('valores inseridos na tabela.')

connect_db()

insert_values("Paciente", "NOME,CPF,DATA_NASCIMENTO,ENDEREÇO", "'José Carlos', '987.654.321-00', '20/10/1990', 'Av. Paulista, São Paulo'")
print('finalizado')
insert_values("Paciente", "NOME,CPF,DATA_NASCIMENTO,ENDEREÇO", "'Jessica Santana', '123.456.789-12', '12/12/1999', 'Av. Brigadeiro, São Paulo'")

connect_db().commit()

def con_close():
    connect_db().close()

con_close()