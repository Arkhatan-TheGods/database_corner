def query_create_doctor() -> str:
    return """CREATE TABLE IF NOT EXISTS Medico(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Nome TEXT NOT NULL, 
    CRM TEXT NOT NULL UNIQUE
    ); """


def query_insert_doctor() -> str:
    return """INSERT INTO Medico(Nome,CRM)
    VALUES (:nome, :crm) ;"""


def query_find_doctor_by_name() -> str:
    return "SELECT * FROM Medico WHERE LOWER(Nome) LIKE LOWER(':nome%') LIMIT 10 ;"


def query_update_doctor_by_id() -> str:
    return "UPDATE Medico SET Nome = :nome, CRM = :crm WHERE ID = :id ;"


def query_delete_doctor_by_id() -> str:
    return "DELETE FROM Medico WHERE ID = :id ;"

def query_Show_all_historic_clinic() -> str:
    return "SELECT * FROM Medico;"