def query_create_patient() -> str:
    return """CREATE TABLE IF NOT EXISTS Paciente(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    Nome TEXT NOT NULL, 
    CPF TEXT NOT NULL UNIQUE, 
    Data_Nascimento TEXT NOT NULL, 
    Endereco TEXT NOT NULL
    ); """


def query_insert_patient() -> str:
    return """INSERT INTO Paciente(Nome,CPF,Data_Nascimento,Endereco)
    VALUES(:nome, :cpf, :dt_nasc, :endereco) ;"""

def query_find_patient_by_id() -> str:
    return "SELECT * FROM Paciente WHERE ID = :id ;"

def query_find_patient_by_name() -> str:
    return "SELECT * FROM Paciente WHERE LOWER(Nome) LIKE LOWER(:nome) LIMIT 10 ;"


def query_find_patienty_by_cpf() -> str:
    return "SELECT * FROM Paciente WHERE CPF = :cpf ;"


def query_update_patient_by_id() -> str:
    return """UPDATE Paciente 
    SET Nome = :nome, CPF = :cpf, Data_Nascimento = :dt_nasc, Endereco = :end WHERE ID = :id ;"""


def query_delete_patient_by_id() -> str:
    return "DELETE FROM Paciente WHERE ID = :id ;"

def query_show_all_patient() -> str:
    return "SELECT * FROM Paciente;"