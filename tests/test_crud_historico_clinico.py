import pytest
import sqlite3
from os import system
from dotenv import dotenv_values

system('cls')

@pytest.fixture()
def historico_clinico():
    config = dotenv_values('.env.ambient')
    test = config.get('teste')

    connect = sqlite3.connect(test)
    cursor = connect.cursor()
    connect.set_trace_callback(print)

    cursor.execute("CREATE TABLE IF NOT EXISTS Paciente(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL);")
    cursor.execute('DROP TABLE Paciente ;')
    cursor.execute("CREATE TABLE Paciente(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Nome TEXT NOT NULL) ;")
    cursor.execute("INSERT INTO Paciente(Nome) VALUES('PAULO') ;")
    
    cursor.execute("CREATE TABLE IF NOT EXISTS Historico_Clinico(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL);")
    cursor.execute('DROP TABLE Historico_Clinico ;')
    cursor.execute("""CREATE TABLE Historico_Clinico(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        ID_Paciente INTEGER NOT NULL,Doenca TEXT NOT NULL, Alergia TEXT NOT NULL, Medicacao TEXT NOT NULL,
        FOREIGN KEY(ID_Paciente) REFERENCES Paciente(ID));
        """)

    connect.commit()
    yield connect, cursor
    connect.close()

@pytest.fixture()
def historico_clinico2():
    config = dotenv_values('.env.ambient')
    test = config.get('teste')

    connect = sqlite3.connect(test)
    cursor = connect.cursor()
    connect.set_trace_callback(print)

    cursor.executescript("""
    BEGIN;
    CREATE TABLE IF NOT EXISTS Paciente(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL);
    DROP TABLE Paciente ;
    CREATE TABLE IF NOT EXISTS Paciente(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Nome TEXT NOT NULL) ;
    INSERT INTO Paciente(Nome) VALUES('PAULO'),('JOSÉ') ;
    CREATE TABLE IF NOT EXISTS Historico_Clinico(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL);
    DROP TABLE Historico_Clinico ;
    CREATE TABLE IF NOT EXISTS Historico_Clinico(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        ID_Paciente INTEGER NOT NULL,Doenca TEXT NOT NULL, Alergia TEXT NOT NULL, Medicacao TEXT NOT NULL,
        FOREIGN KEY(ID_Paciente) REFERENCES Paciente(ID));
    INSERT INTO Historico_Clinico(ID_Paciente, Doenca, Alergia, Medicacao)
        VALUES(1, 'cancer', 'lactose', 'dipirona') ;  
    COMMIT; """)
    
    connect.commit()
    yield connect, cursor
    connect.close()


def test_insert_paciente_in_historico_clinico(historico_clinico):
    connect, cursor = historico_clinico
    cursor.execute("""INSERT INTO Historico_Clinico(ID_Paciente, Doenca, Alergia, Medicacao)
        VALUES(1, 'cancer', 'lactose', 'dipirona') ;""")
    cursor.execute('SELECT * FROM Historico_Clinico WHERE ID = 1 ;')
    assert cursor.fetchone()[2] == 'cancer'

def test_find_historico_clinico_by_id(historico_clinico2):
    connect, cursor = historico_clinico2
    cursor.execute("SELECT * FROM Historico_Clinico WHERE ID = 1 ;")
    assert cursor.fetchone()[0] == 1

def test_find_historico_clinico_by_id_paciente(historico_clinico2):
    connect, cursor = historico_clinico2
    cursor.execute("SELECT * FROM Historico_Clinico WHERE ID_Paciente = 1 ;")
    assert cursor.fetchone()[1] == 1

def test_find_historico_clinico_by_doenca(historico_clinico2):
    connect, cursor = historico_clinico2
    cursor.execute("SELECT * FROM Historico_Clinico WHERE Doenca = 'cancer' ;")
    assert cursor.fetchone()[2] == 'cancer'

def test_find_historico_clinico_by_alergia(historico_clinico2):
    connect, cursor = historico_clinico2
    cursor.execute("SELECT * FROM Historico_Clinico WHERE Alergia = 'lactose' ;")
    assert cursor.fetchone()[3] == 'lactose'

def test_find_historico_clinico_by_medicacao(historico_clinico2):
    connect, cursor = historico_clinico2
    cursor.execute("SELECT * FROM Historico_Clinico WHERE Medicacao = 'dipirona' ;")
    assert cursor.fetchone()[4] == 'dipirona'
    
def test_update_id_paciente(historico_clinico2):
    connect, cursor = historico_clinico2
    cursor.execute("UPDATE Historico_Clinico SET ID_Paciente = 2 WHERE ID_Paciente = 1 ;")
    cursor.execute("SELECT * FROM Historico_Clinico WHERE ID_Paciente = 2;")
    assert cursor.fetchone()[1] == 2

def test_update_doenca(historico_clinico2):
    connect, cursor = historico_clinico2
    cursor.execute("UPDATE Historico_Clinico SET Doenca = 'conjuntivite' WHERE ID = 1 ;")
    cursor.execute("SELECT * FROM Historico_Clinico WHERE ID= 1 ;")
    assert cursor.fetchone()[2] == 'conjuntivite'

def test_update_alergia(historico_clinico2):
    connect, cursor = historico_clinico2
    cursor.execute("UPDATE Historico_Clinico SET Alergia = 'gatos' WHERE ID = 1 ;")
    cursor.execute("SELECT * FROM Historico_Clinico WHERE ID = 1;")
    assert cursor.fetchone()[3] == 'gatos'

def test_update_medicacao(historico_clinico2):
    connect, cursor = historico_clinico2
    cursor.execute("UPDATE Historico_Clinico SET Medicacao = 'contra-ceptivo' WHERE ID = 1 ;")
    cursor.execute("SELECT * FROM Historico_Clinico WHERE ID = 1;")
    assert cursor.fetchone()[4] == 'contra-ceptivo'

def test_delete_historico_clinico(historico_clinico2):
    connect, cursor = historico_clinico2
    cursor.execute("DELETE FROM Historico_Clinico WHERE ID = :id ;", (1,))
    cursor.execute("SELECT * FROM Historico_Clinico WHERE ID = 1 ;")
    assert cursor.fetchone() == None