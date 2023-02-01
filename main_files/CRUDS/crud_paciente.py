from sqlite3 import Cursor

# cria tabela paciente no banco 
def create_table_paciente():
    return """CREATE TABLE IF NOT EXISTS Paciente(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    Nome TEXT NOT NULL, CPF TEXT NOT NULL UNIQUE, Data_Nascimento TEXT NOT NULL, Endereco TEXT NOT NULL);
    """

# insere valores do paciente na tabela paciente dentro do banco
def insert_values_into_paciente(cursor):
    nome = input("nome do paciente: ")
    cpf = input("CPF: ")
    dt_nasc = input("Data de nascimento(xx/xx/xxxx): ")
    endereco = input("Endereço: ")
    cursor.execute("""INSERT INTO Paciente(Nome,CPF,Data_Nascimento,Endereco)
    VALUES( :nome ,  :cpf ,  :nasc , :endereco ); """,(nome,cpf,dt_nasc,endereco))
    print("paciente inserido.")

# procura pacientes que tenham o nome informado e tem a possiblidade de mostrar mais 5 resultados se existir
def find_paciente(cursor):
    nome = input("nome do paciente: ")
    query = f"SELECT * FROM Paciente WHERE LOWER(Nome) LIKE LOWER('{nome}%') LIMIT 10;"
    return cursor.execute(query).fetchall()

# atualiza registro do paciente a partir do ID que é fixo e único
def update_paciente(cursor):

    while True:

        consulta = input('consulta por paciente: \n[1] Nome \n[2] CPF \n[3] atualizar por ID \n[4] Voltar \nOpção:').strip()
        if consulta == '1':
            nome = input('nome: ').strip()
            query = f"SELECT * FROM Paciente WHERE LOWER(Nome) LIKE LOWER(':nome%') LIMIT 10;"
            result = cursor.execute(query,(nome,)).fetchall()

            for c in result:
                print(c)
            
            atualizar = input('digite s se deseja atualizar: ').strip().lower()
            if atualizar == 's':
                ID = int(input('informe o ID: '))
                objetive = cursor.execute(f'SELECT * FROM Paciente WHERE ID = :id ;', (ID,))
                found = cursor.fetchone()
                
                print({found})
                column_nome = input('atualizar nome?[s/n]: ').strip().lower()
                if column_nome == 's':
                    nome = input('novo nome: ').strip()
                    cursor.execute(f"UPDATE Paciente SET Nome = :nome WHERE ID = :id ;",(nome,ID))
                
                column_cpf =input('atualizar CPF?[s/n]: ').strip()
                if column_cpf == 's':
                    cpf = input('novo CPF: ').strip()
                    cursor.execute(f"UPDATE Paciente SET CPF = :cpf WHERE ID = :id ;", (cpf, ID))

                column_data_nascimento = input('atualizar data de nascimento?[s/n]: ').strip().lower()
                if column_data_nascimento == 's':
                    dt_nascimento = input('nova data de nascimento(xx/xx/xxx): ')
                    cursor.execute(f"UPDATE Paciente SET Data_Nascimento = :dt WHERE ID = :id",(dt_nascimento, ID))
                
                column_endereco = input('atualizar endereço?[s/n]: ').strip().lower()
                if column_endereco == 's':
                    endereco = input('novo endereço: ').strip().capitalize()
                    cursor.execute(f"UPDATE Paciente SET Endereco = :end WHERE ID = :id",(endereco,ID))
                break

        elif consulta == '2':
            cpf = input('CPF: ').strip()
            query = f"SELECT * FROM Paciente WHERE CPF = :cpf LIMIT 10;"
            result = cursor.execute(query,(cpf,)).fetchall()

            for c in result:
                print(c)
            
            atualizar = input('digite s se deseja atualizar: ').strip().lower()
            if atualizar == 's':
                ID = int(input('informe o ID: '))
                objetive = cursor.execute(f'SELECT * FROM Paciente WHERE ID = :id ;', (ID,))
                found = cursor.fetchone()
                
                print({found})
                column_nome = input('atualizar nome?[s/n]: ').strip().lower()
                if column_nome == 's':
                    nome = input('novo nome: ').strip()
                    cursor.execute(f"UPDATE Paciente SET Nome = :nome WHERE ID = :id ;",(nome,ID))
                
                column_cpf =input('atualizar CPF?[s/n]: ').strip()
                if column_cpf == 's':
                    cpf = input('novo CPF: ').strip()
                    cursor.execute(f"UPDATE Paciente SET CPF = :cpf WHERE ID = :id ;", (cpf, ID))


                column_data_nascimento = input('atualizar data de nascimento?[s/n]: ').strip().lower()
                if column_data_nascimento == 's':
                    dt_nascimento = input('nova data de nascimento(xx/xx/xxx): ')
                    cursor.execute(f"UPDATE Paciente SET Data_Nascimento = :dt WHERE ID = :id",(dt_nascimento, ID))
                
                column_endereco = input('atualizar endereço?[s/n]: ').strip().lower()
                if column_endereco == 's':
                    endereco = input('novo endereço: ').strip().capitalize()
                    cursor.execute(f"UPDATE Paciente SET Endereco = :end WHERE ID = :id",(endereco,ID))
                break

        elif consulta == '3':

            atualizar = input('digite s se deseja atualizar: ').strip().lower()
            if atualizar == 's':
                ID = int(input('informe o ID: '))
                objetive = cursor.execute(f'SELECT * FROM Paciente WHERE ID = :id ;', (ID,))
                found = cursor.fetchone()
                
                print({found})
                column_nome = input('atualizar nome?[s/n]: ').strip().lower()
                if column_nome == 's':
                    nome = input('novo nome: ').strip()
                    cursor.execute(f"UPDATE Paciente SET Nome = :nome WHERE ID = :id ;",(nome,ID))
                
                column_cpf =input('atualizar CPF?[s/n]: ').strip()
                if column_cpf == 's':
                    cpf = input('novo CPF: ').strip()
                    cursor.execute(f"UPDATE Paciente SET CPF = :cpf WHERE ID = :id ;", (cpf, ID))

                column_data_nascimento = input('atualizar data de nascimento?[s/n]: ').strip().lower()
                if column_data_nascimento == 's':
                    dt_nascimento = input('nova data de nascimento(xx/xx/xxx): ')
                    cursor.execute(f"UPDATE Paciente SET Data_Nascimento = :dt WHERE ID = :id",(dt_nascimento, ID))
                
                column_endereco = input('atualizar endereço?[s/n]: ').strip().lower()
                if column_endereco == 's':
                    endereco = input('novo endereço: ').strip().capitalize()
                    cursor.execute(f"UPDATE Paciente SET Endereco = :end WHERE ID = :id",(endereco,ID))
                break

        elif consulta == '4':
            break

def del_paciente(cursor):
    ID = int(input('informe o ID a ser deletado: '))
    cursor.execute(f'SELECT * FROM Paciente WHERE ID = :id ;', (ID,))
    print('seguinte registro foi deletado: \n',cursor.fetchone())
    cursor.execute(f"DELETE FROM Paciente WHERE ID = :id ;", (ID,))
