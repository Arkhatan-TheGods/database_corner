# cria tabela historico clinico no banco
def create_table_historico_clinico():
    return """CREATE TABLE IF NOT EXISTS {}(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, {});
    """.format('Historico_Clinico',"""ID_Paciente INTEGER NOT NULL,Doenca TEXT NOT NULL, Alergia TEXT NOT NULL, Medicacao TEXT NOT NULL,
    FOREIGN KEY(ID_Paciente) REFERENCES Paciente(ID)""")
