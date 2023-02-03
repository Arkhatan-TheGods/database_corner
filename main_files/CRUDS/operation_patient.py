from sqlite3 import Cursor
import CRUDS.query_patient as patient


class Patient():
    def __init__(self, id_, nome, cpf, dt_nascimento, endereco):
        self.id = id_
        self.nome = nome
        self.cpf = cpf
        self.dt_nascimento = dt_nascimento
        self.endereco = endereco

# get values to use with insert on the table patient


def values_patient() -> tuple:
    nome = input("nome do paciente: ")
    cpf = input("CPF: ")
    dt_nasc = input(
        "Data de nascimento(xx/xx/xxxx): ")
    endereco = input("Endereço: ")
    return nome, cpf, dt_nasc, endereco

# atualiza registro do paciente a partir do ID que é fixo e único


def new_values(patient: Patient) -> tuple:

    print("dê enter apenas caso deseja manter o valor.")
    if (nome := input("novo nome: ").strip()) != "":
        patient.nome = nome

    if (cpf := input("novo CPF: ").strip()) != "":
        patient.cpf = cpf

    if (data_nasci := input("nova data de nascimento(dd/mm/yyyy)").strip()) != "":
        patient.dt_nascimento

    if (endereco := input("novo endereço: ").strip()) != "":
        patient.endereco

    return patient

# atualiza os valores na tabela


def update_paciente(cursor):
    while True:
        consulta = input(
            "Consulta/Atualizar \n[1] Nome \n[2] CPF \n[3] atualizar direto pelo ID \n[4] Sair \nDigite sua opção: ")
        if consulta == '1':
            name = input("informe o nome: ")
            result = cursor.execute(patient.query_find_patient_by_name(), (f"{name}%",)).fetchall()

            if result:
                for c in result:
                    print(c)
                if input("deseja atualizar [s/n]: ").strip().lower() == 's':
                    ID = input("informe o ID: ")
                    patient_ = Patient(*cursor.execute(patient.query_find_patient_by_id(), (ID,)).fetchone())
                    values = new_values(patient_)

                    if values:
                        cursor.execute(patient.query_update_patient_by_id(), values)

            else:
                print('sem resultados.')

        elif consulta == '2':
            cpf = input("informe o cpf: ")
            result = cursor.execute(patient.query_find_patienty_by_cpf(), (f"{cpf}")).fetchone()

            if result:
                for c in result:
                    print(c)
                if input("deseja atualizar [s/n]: ").strip().lower() == 's':
                    ID = input("informe o ID: ")
                    patient_ = Patient(*cursor.execute(patient.query_find_patient_by_id(), (ID,)).fetchone())
                    values = new_values(patient_)

                    if values:
                        cursor.execute(patient.query_update_patient_by_id(), values)

            else:
                print('sem resultados.')

        elif consulta == '3':
            ID = input("informe o ID: ")
            patient_ = Patient(*cursor.execute(patient.query_find_patient_by_id(), (ID,)).fetchone())
            values = new_values(patient_)
            cursor.execute(patient.query_update_patient_by_id(), values)
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
