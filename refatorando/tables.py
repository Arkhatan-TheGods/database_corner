def entitys() -> str:
    return """BEGIN;
    
    CREATE TABLE IF NOT EXISTS Paciente(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    Nome TEXT NOT NULL, 
    CPF TEXT NOT NULL UNIQUE, 
    Data_Nascimento TEXT NOT NULL, 
    Endereco TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Medico(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Nome TEXT NOT NULL, 
    CRM TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS Prontuario(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    ID_Paciente INTEGER NOT NULL UNIQUE, 
    ID_Medico INTEGER NOT NULL, 
    ID_Historico_Clinico INTEGER NULL,
    Descricao TEXT NOT NULL, 
    Data_Atendimento TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Historico_Clinico(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    ID_Paciente INTEGER NOT NULL,
    Doenca TEXT NOT NULL, 
    Alergia TEXT NOT NULL, 
    Medicacao TEXT NOT NULL,
    FOREIGN KEY(ID_Paciente) REFERENCES Paciente(ID) );
    
    COMMIT; """