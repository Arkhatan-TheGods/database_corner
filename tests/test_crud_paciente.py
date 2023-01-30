import pytest
import sqlite3
from dotenv import dotenv_values
from os import system

system('cls')

@pytest.fixture()
def test_paciente():
    config = dotenv_values('.env.ambient')
    test = config.get('teste')
    connect = sqlite3.connect(test)
    cursor = connect.cursor()
    cursor.executescript("""
    BEGIN;
    DROP TABLE Paciente;
    CREATE TABLE Paciente(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        Nome TEXT NOT NULL, CPF TEXT NOT NULL UNIQUE,
        Data_Nascimento TEXT NOT NULL, Endereco TEXT NOT NULL);
    COMMIT;""")
    connect.commit()
    connect.set_trace_callback(print)
    yield connect, cursor
    connect.close()

@pytest.fixture()
def test_paciente2():
    config = dotenv_values('.env.ambient')
    test = config.get('teste')
    
    connect = sqlite3.connect(test)
    cursor = connect.cursor()
    connect.set_trace_callback(print)
    
    cursor.executescript("""
    BEGIN;
    CREATE TABLE IF NOT EXISTS Paciente(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL);
    DROP TABLE Paciente;
    CREATE TABLE Paciente(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     Nome TEXT NOT NULL, CPF TEXT NOT NULL UNIQUE,
        Data_Nascimento TEXT NOT NULL, Endereco TEXT NOT NULL);
    INSERT INTO Paciente(Nome, CPF, Data_Nascimento, Endereco)
    VALUES('Paulo','12345','97','SÃO PAULO');
    COMMIT;""")
    
    connect.commit()
    yield connect, cursor
    connect.close()

def test_insert_paciente(test_paciente):
    connect, cursor = test_paciente
    cursor.execute(f"""INSERT INTO Paciente(Nome, CPF, Data_Nascimento, Endereco)
    VALUES('Paulo','12345','97','SÃO PAULO'); """)
    cursor.execute(f"""SELECT * FROM Paciente WHERE Nome = 'Paulo' ;""")
    assert cursor.fetchone()[1][0:5] == 'Paulo'

def test_find_paciente(test_paciente2):
    connect, cursor = test_paciente2
    cursor.execute("SELECT * FROM Paciente WHERE LOWER(Nome) LIKE LOWER('Paulo%'); ")
    assert cursor.fetchone()[1][0:5] == 'Paulo'

def test_find_paciente_by_cpf(test_paciente2):
    connect, cursor = test_paciente2
    cursor.execute("SELECT * FROM Paciente WHERE CPF = '12345' ;")
    assert cursor.fetchone()[2][0:5] == '12345'

def test_find_paciente_by_data_nascimento(test_paciente2):
    connect, cursor = test_paciente2
    cursor.execute("SELECT * FROM Paciente WHERE Data_Nascimento = '97' ;")
    assert cursor.fetchone()[3] == '97'

def test_find_paciente_by_endereco(test_paciente2):
    connect, cursor = test_paciente2
    cursor.execute("SELECT * FROM Paciente WHERE Endereco = 'SÃO PAULO' ;")
    assert cursor.fetchone()[4] == 'SÃO PAULO'

def test_update_nome_paciente(test_paciente2):
    connect, cursor = test_paciente2
    cursor.execute("UPDATE Paciente SET Nome = 'José Santos' WHERE ID = 1 ;")
    cursor.execute("SELECT * FROM Paciente WHERE ID = 1 ;")
    assert cursor.fetchone()[1][0:5] == 'José' or 'José '

def test_update_cpf_paciente(test_paciente2):
    connect, cursor = test_paciente2
    cursor.execute("UPDATE Paciente SET CPF = '54321' WHERE ID = 1 ;")
    cursor.execute("SELECT * FROM Paciente WHERE ID = 1 ;")
    assert cursor.fetchone()[2] == '54321'

def test_update_data_nascimento_paciente(test_paciente2):
    connect, cursor = test_paciente2
    cursor.execute("UPDATE Paciente SET Data_Nascimento = '20/07/1997' WHERE ID = 1 ;")
    cursor.execute("SELECT * FROM Paciente WHERE ID = 1 ;")
    assert cursor.fetchone()[3] == '20/07/1997'

def test_update_endereco_paciente(test_paciente2):
    connect, cursor = test_paciente2
    cursor.execute("UPDATE Paciente SET Endereco = 'São Paulo/SP' WHERE ID = 1 ;")
    cursor.execute("SELECT * FROM Paciente WHERE ID = 1 ;")
    assert cursor.fetchone()[4] == 'São Paulo/SP'

def test_delete_paciente(test_paciente2):
    connect, cursor = test_paciente2
    ID = 1
    cursor.execute('SELECT * FROM Paciente WHERE ID = :id ;', (ID,))
    print('seguinte registro foi deletado: \n',cursor.fetchone())
    cursor.execute("DELETE FROM Paciente WHERE ID = :id ;", (ID,))
    assert cursor.fetchone() == None