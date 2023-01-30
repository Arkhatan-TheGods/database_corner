import pytest
import sqlite3 
from dotenv import dotenv_values
from os import system

system('cls')

@pytest.fixture()
def test_medico():
    config = dotenv_values('.env.ambient')
    test = config.get('teste')
    
    connect = sqlite3.connect(test)
    cursor = connect.cursor()
    
    cursor.executescript("""
    BEGIN;
    CREATE TABLE IF NOT EXISTS Medico(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL);
    DROP TABLE Medico ;
    CREATE TABLE IF NOT EXISTS Medico(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Nome TEXT NOT NULL, CRM TEXT NOT NULL UNIQUE);
    COMMIT;
    """)
    connect.commit()
    connect.set_trace_callback(print)
    yield connect, cursor
    connect.close()


@pytest.fixture()
def test_medico2():
    config = dotenv_values('.env.ambient')
    test = config.get('teste')

    connect = sqlite3.connect(test)
    cursor = connect.cursor()

    cursor.executescript("""
    BEGIN; 
    CREATE TABLE IF NOT EXISTS Medico(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL);
    DROP TABLE Medico ;
    CREATE TABLE IF NOT EXISTS Medico(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Nome TEXT NOT NULL, CRM TEXT NOT NULL UNIQUE);
    INSERT INTO Medico(Nome, CRM) VALUES('Rodrigo','1234') ;
    COMMIT ;
    """)
    
    connect.commit()
    connect.set_trace_callback(print)
    yield connect, cursor
    connect.close()

def test_insert_medico(test_medico):
    connect, cursor = test_medico
    cursor.execute("INSERT INTO Medico(Nome, CRM) VALUES('Rodrigo','1234') ; ")
    cursor.execute('SELECT * FROM Medico WHERE ID = 1 ;')
    assert cursor.fetchone()[1][0:7] == 'Rodrigo'

def test_find_medico(test_medico2):
    connect, cursor = test_medico2
    cursor.execute("SELECT * FROM Medico WHERE LOWER(Nome) LIKE LOWER('Rodrigo%'); ")
    assert cursor.fetchone()[1] == 'Rodrigo'    

def test_find_medico_by_crm(test_medico2):
    connect, cursor = test_medico2
    cursor.execute("SELECT * FROM Medico WHERE CRM = '1234' ; ")
    assert cursor.fetchone()[1] == 'Rodrigo'    

def test_update_nome_medico(test_medico2):
    connect, cursor = test_medico2
    cursor.execute("UPDATE Medico SET Nome = 'Marty' WHERE ID = 1 ;")
    cursor.execute("SELECT * FROM Medico WHERE ID = 1 ;")
    assert cursor.fetchone()[1] == 'Marty'

def test_update_crm_medico(test_medico2):
    connect, cursor = test_medico2
    cursor.execute("UPDATE Medico SET CRM = '4321' WHERE ID = 1 ;")
    cursor.execute("SELECT * FROM Medico WHERE ID = 1 ;")
    assert cursor.fetchone()[2] == '4321'

def test_delete_medico(test_medico2):
    connect, cursor = test_medico2
    ID = 1
    cursor.execute('SELECT * FROM Paciente WHERE ID = :id ;', (ID,))
    print('seguinte registro foi deletado: \n',cursor.fetchone())
    cursor.execute("DELETE FROM Paciente WHERE ID = :id ;", (ID,))
    assert cursor.fetchone() == None