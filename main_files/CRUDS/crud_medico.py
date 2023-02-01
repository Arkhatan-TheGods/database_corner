# cria tabela medico no banco
def create_table_medico():
    return """CREATE TABLE IF NOT EXISTS Medico(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Nome TEXT NOT NULL, CRM TEXT NOT NULL UNIQUE);
    """

# insere valores do medico na tabela medico dentro do banco
def insert_values_into_medico(cursor):
    nome = input("nome do médico: ")
    crm = input("número do CRM: ")
    query = f"""INSERT INTO Medico(Nome,CRM) VALUES(:nome, :crm);"""
    cursor.execute(query,(nome, crm))

