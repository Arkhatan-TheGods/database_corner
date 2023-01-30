# cria tabela prontuario no banco
def create_table_prontuario():
    return """CREATE TABLE IF NOT EXISTS {}(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, {});
    """.format('Prontuario',"""ID_Paciente INTEGER NOT NULL, ID_Medico INTEGER NOT NULL, ID_Historico_Clinico INTEGER NOT NULL,
    Descricao TEXT NOT NULL, Data_Atendimento TEXT NOT NULL""")
