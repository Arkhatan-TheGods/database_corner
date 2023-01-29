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
    query = f"SELECT * FROM Paciente WHERE LOWER(Nome) LIKE LOWER('{nome}%') LIMIT 10;"
    return cursor.execute(query).fetchall()

# atualiza registro do paciente a partir do ID que é fixo e único
def update_paciente(cursor):

    while True:

        consulta = input('consulta por paciente: \n[1] Nome \n[2] CPF \n[3] atualizar por ID \n[4] Sair \nOpção:').strip()
        if consulta == '1':
            nome = input('nome: ').strip()
            query = f"SELECT * FROM Paciente WHERE LOWER(Nome) LIKE LOWER('{nome}%') LIMIT 10;"
            result = cursor.execute(query).fetchall()

            for c in result:
                print(c)

            atualizar = input('digite s se deseja atualizar registro: ').strip().lower()
            if atualizar == 's':
                ID = int(input('informe o ID:'))
                encontrado = cursor.execute(f'SELECT * FROM Paciente WHERE ID = {ID};').fetchone()
                campo = int(input("""
                [1] Nome
                [2] CPF
                [3] Data de Nascimento
                [4] Endereço
                Sua Opção: """).strip())
                if campo == 1:
                    valor = input('novo nome: ')
                    cursor.execute(f"UPDATE Paciente SET Nome = '{valor}' WHERE ID = '{ID}';")

                elif campo == 2:
                    valor = input('Novo CPF:')
                    cursor.execute(f"UPDATE Paciente SET CPF = '{valor}' WHERE ID = '{ID}';")
            
                elif campo == 3:
                    valor = input('nova Data de Nascimento(xx/xx/xxxx): ')
                    cursor.execute(f"UPDATE Paciente SET Data_Nascimento = '{valor}' WHERE ID = '{ID}';")
                    
                elif campo == 4:
                    valor = input('novo Endereço: ')
                    cursor.execute(f"UPDATE Paciente SET Endereco = '{valor}' WHERE ID = '{ID}';")


        elif consulta == '2':
            cpf = input('CPF: ').strip()
            query = f"SELECT * FROM Paciente WHERE CPF = '{cpf}' ; "
            result = cursor.execute(query).fetchall()

            for c in result:
                print(c)

            atualizar = input('digite s se deseja atualizar registro: ').strip().lower()
            if atualizar == 's':
                ID = int(input('informe o ID:'))
                encontrado = cursor.execute(f'SELECT * FROM Paciente WHERE ID = {ID};').fetchone()
                campo = int(input("""
                [1] Nome
                [2] CPF
                [3] Data de Nascimento
                [4] Endereço
                Sua Opção: """).strip())
                if campo == 1:
                    valor = input('novo nome: ')
                    cursor.execute(f"UPDATE Paciente SET Nome = '{valor}' WHERE ID = '{ID}';")

                elif campo == 2:
                    valor = input('Novo CPF:')
                    cursor.execute(f"UPDATE Paciente SET CPF = '{valor}' WHERE ID = '{ID}';")
            
                elif campo == 3:
                    valor = input('nova Data de Nascimento(xx/xx/xxxx): ')
                    cursor.execute(f"UPDATE Paciente SET Data_Nascimento = '{valor}' WHERE ID = '{ID}';")
                    
                elif campo == 4:
                    valor = input('novo Endereço: ')
                    cursor.execute(f"UPDATE Paciente SET Endereco = '{valor}' WHERE ID = '{ID}';")


        elif consulta == '3':
            atualizar = 's'
            if atualizar == 's':
                ID = int(input('informe o ID:'))
                encontrado = cursor.execute(f'SELECT * FROM Paciente WHERE ID = {ID};').fetchone()
                campo = int(input("""
                [1] Nome
                [2] CPF
                [3] Data de Nascimento
                [4] Endereço
                Sua Opção: """).strip())
                if campo == 1:
                    valor = input('novo nome: ')
                    cursor.execute(f"UPDATE Paciente SET Nome = '{valor}' WHERE ID = '{ID}';")

                elif campo == 2:
                    valor = input('Novo CPF:')
                    cursor.execute(f"UPDATE Paciente SET CPF = '{valor}' WHERE ID = '{ID}';")
            
                elif campo == 3:
                    valor = input('nova Data de Nascimento(xx/xx/xxxx): ')
                    cursor.execute(f"UPDATE Paciente SET Data_Nascimento = '{valor}' WHERE ID = '{ID}';")
                    
                elif campo == 4:
                    valor = input('novo Endereço: ')
                    cursor.execute(f"UPDATE Paciente SET Endereco = '{valor}' WHERE ID = '{ID}';")
                    

        elif consulta == '4':
            break