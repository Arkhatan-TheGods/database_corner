# cria tabela medico no banco
def create_table_medico():
    return """CREATE TABLE IF NOT EXISTS Medico(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Nome TEXT NOT NULL, CRM TEXT NOT NULL UNIQUE);
    """