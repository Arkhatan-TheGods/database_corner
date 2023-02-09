from sqlite3 import Cursor
import CRUDS_QUERYS.query_medical_history as history_query
from CRUDS_OPERATIONS.operation_patient import find_patient_by_name
import menu.menu as menu

class History():
    def __init__(self,id_paciente,doenca,alergia,medicacao):
        self.id_paciente = id_paciente
        self.doenca = doenca
        self.alergia = alergia
        self.medicacao = medicacao

def values_medical_history() -> tuple:
    id_paciente = int(input('informe o id do paciente: ').strip())
    doenca = input('informe a doença(s): ')
    alergia = input('informe a(s) alergia(a): ')
    medicacao = input('informe os medicamentos: ')
    return id_paciente, doenca, alergia, medicacao


def find_medical_history(cursor) -> "class History":
    ID = int(input('informe o ID do Paciente: ').strip())
    result = History(cursor.execute(history_query.query_find_medical_history_by_id_patient(), (ID,)).fetchone())
    return result


def insert_medical_history(values, cursor):
    cursor.execute(history_query.query_insert_medical_history(),(values))

def submenu_medical_history(cursor):
    while True:
        consulta = menu.submenu_medical_history()

        if consulta == '1':
            name = input('informe o nome: ').strip()
            result = find_patient_by_name(name, cursor)
            for c in result:
                print(c)

            found = find_medical_history(ID, cursor)
            if found == None:
                print("Histórico Clínico não existe")
                if input("deseja criar? [s/n]: ").strip().lower() == 's':
                    values = values_medical_history()
                    insert_medical_history(values, cursor)

            elif found != None:
                print(found)

        elif consulta == '2':
            find_medical_history(cursor)
            
        elif consulta == '3':
            found = find_medical_history(cursor)
            

        elif consulta == '4':
            pass

        elif consulta == '5':
            break
        else:
            print('opção inválida, tente novamente.')
