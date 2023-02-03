from sqlite3 import Cursor


class Patient():
    def __init__(self, id_, nome, cpf, dt_nascimento, endereco):
        self.id = id_
        self.nome = nome
        self.cpf = cpf
        self.dt_nascimento = dt_nascimento
        self.endereco = endereco


def values_patient():
    nome = input("nome do paciente: ")
    cpf = input("CPF: ")
    dt_nasc = input(
        "Data de nascimento(xx/xx/xxxx): ")
    endereco = input("Endereço: ")
    return nome, cpf, dt_nasc, endereco

# atualiza registro do paciente a partir do ID que é fixo e único


def update_paciente(cursor):

    while True:

        consulta = input(
            'consulta por paciente: \n[1] Nome \n[2] CPF \n[3] atualizar por ID \n[4] Voltar \nOpção:').strip()
        if consulta == '1':

            nome = input('nome: ').strip()
            query = f"SELECT * FROM Paciente WHERE LOWER(Nome) LIKE LOWER(:nome) LIMIT 10;"
            result = cursor.execute(
                query, (f"{nome}%",)).fetchall()

            for c in result:
                print(c)

            atualizar = input(
                'digite s se deseja atualizar: ').strip().lower()
            if atualizar == 's':
                ID = int(input('informe o ID: '))
                objetive = cursor.execute(
                    f'SELECT * FROM Paciente WHERE ID = :id ;', (ID,))
                found = Patient(cursor.fetchone())

                print({found})
                column_nome = input(
                    'atualizar nome?[s/n]: ').strip().lower()
                if column_nome == 's':
                    nome = input(
                        'novo nome: ').strip()

                    # cursor.execute(f"UPDATE Paciente SET Nome = :nome WHERE ID = :id ;",(nome,ID))

                column_cpf = input(
                    'atualizar CPF?[s/n]: ').strip()
                if column_cpf == 's':
                    cpf = input(
                        'novo CPF: ').strip()
                    cursor.execute(
                        f"UPDATE Paciente SET CPF = :cpf WHERE ID = :id ;", (cpf, ID))

                column_data_nascimento = input(
                    'atualizar data de nascimento?[s/n]: ').strip().lower()
                if column_data_nascimento == 's':
                    dt_nascimento = input(
                        'nova data de nascimento(xx/xx/xxx): ')
                    cursor.execute(
                        f"UPDATE Paciente SET Data_Nascimento = :dt WHERE ID = :id", (dt_nascimento, ID))

                column_endereco = input(
                    'atualizar endereço?[s/n]: ').strip().lower()
                if column_endereco == 's':
                    endereco = input(
                        'novo endereço: ').strip().capitalize()
                    cursor.execute(
                        f"UPDATE Paciente SET Endereco = :end WHERE ID = :id", (endereco, ID))
                break

        elif consulta == '2':
            cpf = input('CPF: ').strip()
            query = f"SELECT * FROM Paciente WHERE CPF = :cpf LIMIT 10;"
            result = cursor.execute(
                query, (cpf,)).fetchone()

            for c in result:
                print(c)

            atualizar = input(
                'digite s se deseja atualizar: ').strip().lower()
            if atualizar == 's':
                ID = int(input('informe o ID: '))
                objetive = cursor.execute(
                    f'SELECT * FROM Paciente WHERE ID = :id ;', (ID,))
                found = cursor.fetchone()

                print({found})
                column_nome = input(
                    'atualizar nome?[s/n]: ').strip().lower()
                if column_nome == 's':
                    nome = input(
                        'novo nome: ').strip()
                    cursor.execute(
                        f"UPDATE Paciente SET Nome = :nome WHERE ID = :id ;", (nome, ID))

                column_cpf = input(
                    'atualizar CPF?[s/n]: ').strip()
                if column_cpf == 's':
                    cpf = input(
                        'novo CPF: ').strip()
                    cursor.execute(
                        f"UPDATE Paciente SET CPF = :cpf WHERE ID = :id ;", (cpf, ID))

                column_data_nascimento = input(
                    'atualizar data de nascimento?[s/n]: ').strip().lower()
                if column_data_nascimento == 's':
                    dt_nascimento = input(
                        'nova data de nascimento(xx/xx/xxx): ')
                    cursor.execute(
                        f"UPDATE Paciente SET Data_Nascimento = :dt WHERE ID = :id", (dt_nascimento, ID))

                column_endereco = input(
                    'atualizar endereço?[s/n]: ').strip().lower()
                if column_endereco == 's':
                    endereco = input(
                        'novo endereço: ').strip().capitalize()
                    cursor.execute(
                        f"UPDATE Paciente SET Endereco = :end WHERE ID = :id", (endereco, ID))
                break

        elif consulta == '3':

            atualizar = input(
                'digite s se deseja atualizar: ').strip().lower()
            if atualizar == 's':
                ID = int(input('informe o ID: '))
                objetive = cursor.execute(
                    f'SELECT * FROM Paciente WHERE ID = :id ;', (ID,))
                found = Patient(
                    *cursor.fetchone())

                print(found.__dict__)
                column_nome = input(
                    'atualizar nome?[s/n]: ').strip().lower()
                if column_nome == 's':
                    nome = input(
                        'novo nome: ').strip()
                    cursor.execute(
                        f"UPDATE Paciente SET Nome = :nome WHERE ID = :id ;", (nome, ID))

                column_cpf = input(
                    'atualizar CPF?[s/n]: ').strip()
                if column_cpf == 's':
                    cpf = input(
                        'novo CPF: ').strip()
                    cursor.execute(
                        f"UPDATE Paciente SET CPF = :cpf WHERE ID = :id ;", (cpf, ID))

                column_data_nascimento = input(
                    'atualizar data de nascimento?[s/n]: ').strip().lower()
                if column_data_nascimento == 's':
                    dt_nascimento = input(
                        'nova data de nascimento(xx/xx/xxx): ')
                    cursor.execute(
                        f"UPDATE Paciente SET Data_Nascimento = :dt WHERE ID = :id", (dt_nascimento, ID))

                column_endereco = input(
                    'atualizar endereço?[s/n]: ').strip().lower()
                if column_endereco == 's':
                    endereco = input(
                        'novo endereço: ').strip().capitalize()
                    cursor.execute(
                        f"UPDATE Paciente SET Endereco = :end WHERE ID = :id", (endereco, ID))

                cursor.execute((nome, ID))
                break

        elif consulta == '4':
            break


def del_paciente(cursor):
    ID = int(
        input('informe o ID a ser deletado: '))
    cursor.execute(
        f'SELECT * FROM Paciente WHERE ID = :id ;', (ID,))
    print('seguinte registro foi deletado: \n',
          cursor.fetchone())
    cursor.execute(
        f"DELETE FROM Paciente WHERE ID = :id ;", (ID,))
