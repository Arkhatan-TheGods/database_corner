import sqlite3
from dotenv import dotenv_values

def create_table_pacientes():
    return

def connect_db():
    config = dotenv_values('.env.ambient')
    path_db = config.get('PATH_DATABASE') 
    connect = sqlite3.connect(path_db)
    #cursor = connect.cursor()
    return connect

def create_table(table, columns):
    conn = connect_db()
    query = f"""CREATE TABLE {table}(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,{columns}) ;"""
    conn.cursor().execute(query)
    print('tabela criada.')

#create_table("IF NOT EXISTS Paciente", "NOME TEXT NOT NULL, CPF TEXT NOT NULL, DATA_NASCIMENTO TEXT NOT NULL, ENDEREÇO TEXT NOT NULL")

def insert_values(table, columns, values):
    conn = connect_db()
    query = f"INSERT INTO {table}({columns}) VALUES({values}); "
    conn.cursor().execute(query)
    conn.commit()
    print('valores inseridos na tabela.')

insert_values("Paciente", "NOME,CPF,DATA_NASCIMENTO,ENDEREÇO", "'José Carlos', '987.654.321-00', '20/10/1990', 'Av. Paulista, São Paulo'")
