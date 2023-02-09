def query_create_medical_history() -> str:
    return """CREATE TABLE IF NOT EXISTS Historico_Clinico(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    ID_Paciente INTEGER NOT NULL,
    Doenca TEXT NOT NULL, 
    Alergia TEXT NOT NULL, 
    Medicacao TEXT NOT NULL,
    FOREIGN KEY(ID_Paciente) REFERENCES Paciente(ID) );
    """


def query_insert_medical_history() -> str:
    return """INSERT INTO Historico_Clinico(ID_Paciente, Doenca, Alergia, Medicacao)
    VALUES (:id, :doenca, :alergia, :medicacao) ;"""


def query_find_medical_history_by_id_patient() -> str:
    return """SELECT * FROM Historico_Clinico WHERE ID_Paciente = :id ;"""


def query_find_medical_history_by_id() -> str:
    return """SELECT * FROM Historico_Clinico WHERE ID = :id ;"""


def query_update_medical_history_by_id() -> str:
    return """UPDATE Historico_Clinico 
    SET ID_Paciente = :id_paciente, Doenca = :doenca, Alergia = :alergia, Medicacao = :medicacao WHERE ID = :id ;"""


def query_delete_medical_history_by_id() -> str:
    return "DELETE FROM Historico_Clinico WHERE ID = id: ;"


def query_show_all_medical_history() -> str:
    return "SELECT * FROM Historico_Clinico;"
