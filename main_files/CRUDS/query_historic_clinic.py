
def query_create_historic_clinic():
    return """CREATE TABLE Historico_Clinico(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    ID_Paciente INTEGER NOT NULL,
    Doenca TEXT NOT NULL, 
    Alergia TEXT NOT NULL, 
    Medicacao TEXT NOT NULL,
    FOREIGN KEY(ID_Paciente) REFERENCES Paciente(ID)
    """


def query_insert_historic_clinic():
    return """INSERT INTO Historico_Clinico(ID_Paciente, Doenca, Alergia, Medicacao)
    VALUES (:id, :doenca, :alergia, :medicacao) ;"""


def query_find_historic_clinic_by_id_patient():
    return """SELECT * FROM Historico_Clinico WHERE ID_Paciente = :id ;"""


def query_find_historic_clinic_by_id():
    return """SELECT * FROM Historico_Clinico WHERE ID = :id ;"""


def query_update_historic_clinic_by_id():
    return """UPDATE Historico_Clinico 
    SET ID_Paciente = :id, Doenca = :doenca, Alergia = :alergia, Medicacao WHERE ID = :id ;"""


def query_delete_historic_clinic_by_id():
    return "DELETE FROM Historico_Clinico WHERE ID = id: ;"
