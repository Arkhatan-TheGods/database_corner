# cria tabela medico no banco
def create_table_medico():
    return """CREATE TABLE IF NOT EXISTS {}(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, {});
    """.format('Medico','Nome TEXT NOT NULL, CRM TEXT NOT NULL UNIQUE')
