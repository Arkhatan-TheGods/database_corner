import CRUDS_QUERYS.query_doctor as doctor_query
from sqlite3 import Cursor


def create_table_medico():
    return """CREATE TABLE IF NOT EXISTS Medico(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Nome TEXT NOT NULL, CRM TEXT NOT NULL UNIQUE);
    """


class Doctor():
    def __init__(self, ID, nome, crm):
        self.id = ID
        self.nome = nome
        self.crm = crm


def insert_values_into_medico():
    nome = input("nome do médico: ")
    crm = input("número do CRM: ")
    return nome, crm


def find_doctor_by_name(name, cursor):
    return cursor.execute(doctor_query.query_find_doctor_by_name(), (f"{name}%",)).fetchall()


def new_values(doctor: Doctor) -> "class":
    if (nome := input("novo nome: ").strip() != ''):
        doctor.nome = nome
    if (crm := input("novo crm: ").strip() != ''):
        doctor.crm = crm
    return doctor


def insert_new_values(ID, cursor):
    result = Doctor(*cursor.execute(doctor_query.query_find_doctor_by_id(), (ID,)).fetchone())
    values = new_values(result)
    cursor.execute(doctor_query.query_update_doctor_by_id(), (values.nome, values.crm, values.id))


def submenu_find_or_update(cursor):
    while True:
        consulta = input(
            "Consultar/Atualizar por: \n[1] Nome \n[2] atualizar direto pelo ID \n[3] voltar Menu Principal \nDigite sua opção: ")
        if consulta == '1':
            name = input("informe o nome: ").strip()
            result = find_doctor_by_name(name, cursor)
            for c in result:
                print(c)

            if input("deseja atualizar [s/n]: ").strip().lower()[0] == 's':
                ID = input("informe o ID: ")
                insert_new_values(ID, cursor)
        elif consulta == '2':
            ID = input("informe o ID: ")
            insert_new_values(ID, cursor)

        elif consulta == '3':
            break
