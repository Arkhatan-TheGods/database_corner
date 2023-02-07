# cria tabela prontuario no banco
def create_table_prontuario():
    return """CREATE TABLE IF NOT EXISTS Prontuario(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    ID_Paciente INTEGER NOT NULL, ID_Medico INTEGER NOT NULL, ID_Historico_Clinico INTEGER NOT NULL,
    Descricao TEXT NOT NULL, Data_Atendimento TEXT NOT NULL);
    """