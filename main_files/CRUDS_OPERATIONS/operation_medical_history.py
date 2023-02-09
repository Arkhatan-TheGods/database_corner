from sqlite3 import Cursor
import CRUDS_QUERYS.query_medical_history as history_query
from CRUDS_OPERATIONS.operation_patient import find_patient_by_name
import menu.menu as menu


class History():
    def __init__(self, id_, id_paciente, doenca, alergia, medicacao):
        self.id = id_
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


def find_medical_history(ID, cursor) -> History:
    result = cursor.execute(history_query.query_find_medical_history_by_id_patient(), (ID,)).fetchone()
    return result


def insert_medical_history(values, cursor):
    cursor.execute(history_query.query_insert_medical_history(), (values))

def new_values(history: History) -> "class":
    print("dê enter apenas caso deseja manter o valor.")

    if (id_paciente := input("digite o novo id: ").strip()) != "":
        history.id_paciente = id_paciente

    if (doenca := input("atualizar registro de doença: ")) != "":
        history.doenca = doenca

    if (alergia := input("atualizar registro de alergia:")) != "":
        history.alergia = alergia
    
    if (medicacao := input("atualizar medicacao: ")) != "":
        history.medicacao = medicacao
    return history

def update_values(ID, cursor):
    history = find_medical_history(ID, cursor)
    values = new_values(history)
    cursor.execute(history_query.query_update_medical_history_by_id(), (history.id_paciente, 
    history.doenca, history.alergia, history.medicacao, history.id))

def del_history(ID, cursor):
    cursor.execute(history_query.query_delete_medical_history_by_id(), (ID,))

def submenu_medical_history(cursor):
    while True:
        consulta = menu.submenu_medical_history()

        if consulta == '1':
            "faz uma busca na tabela paciente e depois pergunta o id para verificar se existe um registro no histórico clínico"
            name = input('informe o nome: ').strip()
            result = find_patient_by_name(name, cursor)
            for c in result:
                print(c)

            ID = int(input('informe o ID do Paciente: ').strip())
            found = find_medical_history(ID, cursor)
            if found == None:
                print("Histórico Clínico não existe")
                if input("deseja criar? [s/n]: ").strip().lower() == 's':
                    values = values_medical_history()
                    insert_medical_history(values, cursor)

            elif found != None:
                print(found)

        elif consulta == '2':
            ID = int(input('informe o ID do Paciente: ').strip())
            found = find_medical_history(ID, cursor)
            if found == None:
                print("Histórico Clínico não existe")
            elif found != None:
                print(found)

        elif consulta == '3':
            ID = int(input('informe o ID do Paciente: ').strip())
            found = find_medical_history(ID, cursor)
            if found != None:
                update_values(ID, cursor)
                
            elif found == None:
                print("Histórico clínico não existe")
        elif consulta == '4':
            ID = int(input('informe o ID do Paciente: ').strip())
            found = find_medical_history(ID, cursor)
            if found == None:
                print("Histórico Clínico não existe")
            elif found != None:
                print(found)
                if input('deseja deletar o registro? [s/n]: ').strip().lower()[0] == 's':
                    del_history(ID, cursor)

        elif consulta == '5':
            break
        else:
            print('opção inválida, tente novamente.')
