from main_files.CRUDS.crud_paciente import query_step_update


def get_values():
    column_nome = input(
        'atualizar nome?[s/n]: ').strip().lower()
    if column_nome == 's':
        nome = input('novo nome: ').strip()

    column_cpf = input(
        'atualizar CPF?[s/n]: ').strip()
    if column_cpf == 's':
        cpf = input('novo CPF: ').strip()

    column_data_nascimento = input(
        'atualizar data de nascimento?[s/n]: ').strip().lower()
    if column_data_nascimento == 's':
        dt_nascimento = input(
            'nova data de nascimento(xx/xx/xxx): ')

    column_endereco = input(
        'atualizar endereço?[s/n]: ').strip().lower()
    if column_endereco == 's':
        endereco = input(
            'novo endereço: ').strip().capitalize()

    return nome, cpf, dt_nascimento, endereco

# atualiza registro do paciente a partir do ID que é fixo e único


def update_paciente(cursor):

    while True:

        consulta = input(
            'consulta por paciente: \n[1] Nome \n[2] CPF \n[3] atualizar por ID \n[4] Voltar \nOpção:').strip()

        if consulta == '1':
            nome = input('nome: ').strip()
            query = f"SELECT * FROM Paciente WHERE LOWER(Nome) LIKE LOWER(':nome%') LIMIT 10;"
            result = cursor.execute(
                query, (nome,)).fetchall()

            for c in result:
                print(c)

            nome, cpf, dt_nascimento, endereco = get_values()

            nome = nome if nome else found[1]
            cpf = cpf if cfp else found[2]
            dt_nascimento = dt_nascimento if dt_nascimento else found[3]
            endereco = endereco if endereco else found[4]

            cursor.execute(query_step_update(
            ), (nome, cpf, dt_nascimento, endereco, ID))
            break

        elif consulta == '2':
            cpf = input('CPF: ').strip()
            query = f"SELECT * FROM Paciente WHERE CPF = :cpf LIMIT 10;"
            result = cursor.execute(
                query, (cpf,)).fetchall()

            for c in result:
                print(c)

            nome = nome if nome else found[1]
            cpf = cpf if cfp else found[2]
            dt_nascimento = dt_nascimento if dt_nascimento else found[3]
            endereco = endereco if endereco else found[4]

            cursor.execute(query_step_update(
            ), (nome, cpf, dt_nascimento, endereco, ID))
            break

        elif consulta == '3':

            atualizar = input(
                'digite s se deseja atualizar: ').strip().lower()
            if atualizar == 's':
                ID = int(input('informe o ID: '))
                objetive = cursor.execute(
                    f'SELECT * FROM Paciente WHERE ID = :id ;', (ID,))
                found = cursor.fetchone()

                print({found})

                nome = nome if nome else found[1]
                cpf = cpf if cfp else found[2]
                dt_nascimento = dt_nascimento if dt_nascimento else found[3]
                endereco = endereco if endereco else found[4]

                cursor.execute(query_step_update(
                ), (nome, cpf, dt_nascimento, endereco, ID))
                break

        elif consulta == '4':
            break
