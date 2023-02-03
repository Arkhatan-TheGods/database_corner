def query_create_medical_record() -> str:
    return """CREATE TABLE IF NOT EXISTS Prontuario(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    ID_Paciente INTEGER NOT NULL, 
    ID_Medico INTEGER NOT NULL, 
    ID_Historico_Clinico INTEGER NOT NULL,
    Descricao TEXT NOT NULL, 
    Data_Atendimento TEXT NOT NULL
    ); """

def query_insert_medical_record() -> str:
    return """ INSERT INTO Prontuario(ID_Paciente, ID_Medico, ID_Historico_Clinico, Descricao, Data_Atendimento)
    VALUES (:id_paciente, :id_medico, :h_clinico, :descricao, :dt_atendimento ) ; """

def query_find_medical_record_by_id() -> str:
    return " SELECT * FROM Prontuario WHERE ID = :id ; "

def query_find_medical_record_by_id_doctor() -> str:
    return "SELECT * FROM Prontuario WHERE ID_Medico = :id ; "

def query_find_medical_record_by_id_patient() -> str:
    return " SELECT * FROM Prontuario WHERE ID_Paciente = :id ; "

def query_update_medical_record() -> str:
    return """UPDATE Prontuario 
    SET ID_Paciente = :id, ID_Medico = :id, ID_Historico_Clinico = :id
    Descricao = :descricao, Data_Atendimento = :dt WHERE ID = :id ;"""

def query_delete_medical_record_by_id() -> str:
    return "DELETE FROM Prontuario WHERE ID = :id ;"

def query_show_all_medical_record() -> str:
    return "SELECT * FROM Prontuario ;"