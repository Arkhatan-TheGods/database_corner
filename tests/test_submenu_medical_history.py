import pytest
import sqlite3
from dotenv import dotenv_values

@pytest.fixture()
def s1():
    config = dotenv_values('.env.ambient')
    test = config.get('teste')
    
    connect = sqlite3.connect(test)
    cursor = connect.cursor()
    connect.set_trace_callback(print)

    cursor.executescript("""BEGIN;
    CREATE TABLE IF NOT EXISTS Historico_Clinico(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL);

    DROP TABLE Historico_Clinico ;

    CREATE TABLE IF NOT EXISTS Historico_Clinico(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    ID_Paciente INTEGER NOT NULL,
    Doenca TEXT NOT NULL, 
    Alergia TEXT NOT NULL, 
    Medicacao TEXT NOT NULL,
    FOREIGN KEY(ID_Paciente) REFERENCES Paciente(ID) );

    CREATE TABLE IF NOT EXISTS Paciente(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL) ;

    DROP TABLE Paciente ;

    CREATE TABLE IF NOT EXISTS Paciente(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    Nome TEXT NOT NULL, 
    CPF TEXT NOT NULL UNIQUE, 
    Data_Nascimento TEXT NOT NULL, 
    Endereco TEXT NOT NULL
    );

    INSERT INTO Paciente(Nome,CPF,Data_Nascimento,Endereco)
    VALUES('Paulo','12345','01/01/1997','São Paulo'), ('Jessica','54321','01/01/1999','São Paulo'), 
    ('Isabella','56789','01/01/1999','São Paulo') ;

    INSERT INTO Historico_Clinico(ID_Paciente,Doenca,Alergia,Medicacao)
    VALUES(1,'osteoporose','cachorro','ibuprofeno'), (2,'gastrite','leite','albendazol'), (3,'cancer','gatos','Alterzanota') ;

    COMMIT;""")

    connect.commit()
    yield connect, cursor
    connect.close()
    