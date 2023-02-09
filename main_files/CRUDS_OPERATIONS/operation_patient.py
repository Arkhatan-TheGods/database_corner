from sqlite3 import Cursor
import CRUDS_QUERYS.query_patient as patient_query
import CRUDS_QUERYS.query_medical_history as medical_history


class Patient():

    def __init__(self, id_, nome, cpf, dt_nascimento, endereco):
        self.id = id_
        self.nome = nome
        self.cpf = cpf
        self.dt_nascimento = dt_nascimento
        self.endereco = endereco


def values_patient() -> tuple:
    nome = input("nome do paciente: ")

    cpf = input("CPF: ")

    dt_nasc = input("Data de nascimento(xx/xx/xxxx): ")

    endereco = input("Endereço: ")

    return nome, cpf, dt_nasc, endereco


def new_values(patient: Patient) -> "class":
    print("dê enter apenas caso deseja manter o valor.")

    if (nome := input("novo nome: ").strip()) != "":
        patient.nome = nome

    if (cpf := input("novo CPF: ").strip()) != "":
        patient.cpf = cpf

    if (data_nasci := input("nova data de nascimento(dd/mm/yyyy): ").strip()) != "":
        patient.dt_nascimento = data_nasci

    if (endereco := input("novo endereço: ").strip()) != "":
        patient.endereco = endereco
    return patient


def insert_new_values(ID, cursor):
    patient = Patient(*cursor.execute(patient_query.query_find_patient_by_id(), (ID,)).fetchone())
    values = new_values(patient)
    cursor.execute(patient_query.query_update_patient_by_id(), (values.nome,
                   values.cpf, values.dt_nascimento, values.endereco, values.id))


def find_patient_by_name(name, cursor):

    return cursor.execute(patient_query.query_find_patient_by_name(), (f"{name}%",)).fetchall()


def find_patient_by_cpf(cpf, cursor):

    return cursor.execute(patient_query.query_find_patient, by_cpf(), (f"{cpf}")).fetchone()


def submenu_find_or_update(cursor):
    while True:
        consulta = input(
            "Consulta/Atualizar \n[1] Nome \n[2] CPF \n[3] atualizar direto pelo ID \n[4] Menu Principal \nDigite sua opção: ")

        if consulta == '1':
            name = input("informe o nome: ")
            result = find_patient_by_name(name, cursor)
            if result:
                for c in result:
                    print(c)

                if input("deseja atualizar [s/n]: ").strip().lower() == 's':
                    ID = int(input("informe o ID: "))
                    insert_new_values(ID, cursor)
            else:
                print('sem resultados.')

        elif consulta == '2':
            cpf = input("informe o cpf: ")
            result = find_patient_by_cpf(cpf, cursor)
            if result:
                for c in result:
                    print(c)

                if input("deseja atualizar [s/n]: ").strip().lower() == 's':
                    ID = input("informe o ID: ")
                    insert_new_values(ID, cursor)
            else:
                print('sem resultados.')

        elif consulta == '3':
            ID = int(input("informe o ID: "))
            insert_new_values(ID, cursor)

        elif consulta == '4':
            break
