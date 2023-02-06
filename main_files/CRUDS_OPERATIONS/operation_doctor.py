import CRUDS_QUERYS.query_doctor as doctor_query
from sqlite3 import Cursor

# cria tabela medico no banco


def create_table_medico():
    return """CREATE TABLE IF NOT EXISTS Medico(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Nome TEXT NOT NULL, CRM TEXT NOT NULL UNIQUE);
    """

# insere valores do medico na tabela medico dentro do banco


class Doctor():
    def __init__(self, ID, name, crm):
        self.id = ID
        self.name = name
        self.crm = crm


def insert_values_into_medico():
    nome = input("nome do médico: ")
    crm = input("número do CRM: ")
    return nome, crm

# procura o doutor pelo nome


def find_doctor_by_name(name, cursor):
    return cursor.execute(doctor_query.query_find_doctor_by_name(), (f"{name}%",)).fetchall()


def new_values(Doctor: Doctor) -> "class":
    pass

def insert_new_values(ID, cursor):
    result = Doctor(cursor.execute(doctor_query.query_find_doctor_by_id(),(ID,)).fetchone())
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

        elif consulta == '2':
            pass
        elif consulta == '3':
            break
