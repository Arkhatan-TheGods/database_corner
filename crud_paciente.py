from sqlite3 import Cursor

# cria tabela paciente no banco 
def create_table_paciente():
    return """CREATE TABLE IF NOT EXISTS {}(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, {});
    """.format("Paciente", "Nome TEXT NOT NULL, CPF TEXT NOT NULL UNIQUE, Data_Nascimento TEXT NOT NULL, Endereco TEXT NOT NULL ")
    

# insere valores do paciente na tabela paciente dentro do banco
def insert_values_into_paciente():
    nome = input("nome do paciente: ")
    cpf = input("CPF: ")
    dt_nasc = input("Data de nascimento(xx/xx/xxxx): ")
    endereco = input("Endereço: ")
    values = (nome,cpf,dt_nasc,endereco)
    query = f"""INSERT INTO {'Paciente'}({'Nome,CPF,Data_Nascimento,Endereco'})
    VALUES('{values[0]}', '{values[1]}', '{values[2]}', '{values[3]}'); """
    return query

# procura pacientes que tenham o nome informado e tem a possiblidade de mostrar mais 5 resultados se existir
def find_paciente(cursor):
    nome = input("nome do paciente: ")
    query = f"SELECT * FROM Paciente WHERE LOWER(Nome) LIKE LOWER('{nome}%') LIMIT 5;"
    return cursor.execute(query).fetchall()

# atualiza registro do paciente a partir do ID que é fixo e único
def update_paciente(cursor):

    consulta = input('consulta por paciente: \n[1] Nome \n[2] CPF \nOpção:').strip()

    if consulta == '1':
        nome = input('nome: ').strip()
        query = f'SELECT * FROM Paciente WHERE Nome = "{nome}"; '
        result = cursor.execute(query).fetchone()
        print(result)
        if result != None:
            column = input('informe o campo(nome, cpf, data_nascimento, endereco): ')
            valor = input('novo valor: ')
            cursor.execute(f"UPDATE Paciente SET {column} = '{valor}' WHERE Nome = {nome};")


    elif consulta == '2':
        cpf = input('CPF: ').strip()
        query = f'SELECT * FROM Paciente WHERE CPF = {int(cpf)};'
        result = cursor.execute(query).fetchone()
        print(result)
        if result != None:
            column = input('informe o campo(nome, cpf, data_nascimento, endereco): ')
            valor = input('novo valor: ')
            cursor.execute(f"UPDATE Paciente SET {column} = '{valor}' WHERE Nome = {cpf};")
