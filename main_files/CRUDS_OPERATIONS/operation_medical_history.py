from sqlite3 import Cursor
import CRUDS_QUERYS.query_medical_history as history_query
import menu.menu as menu 

def insert_medical_history() -> tuple:
    id_paciente = int(input('informe o id do paciente: ').strip())
    doenca = input('informe a doença(s): ')
    alergia = input('informe a(s) alergia(a): ')
    medicacao = input('informe os medicamentos: ')
    return id_paciente,doenca,alergia,medicacao

def find_medical_history(ID, cursor):
    result = cursor.execute(medical_history.query_find_medical_history_by_id_patient()).fetchone()
    if result:
        print(result)
    elif not result:
        print('nenhum resultado.')
    return result if result else None

def medical_history(cursor):
    while True:
        consulta = menu.submenu_medical_history()

        if consulta == '1':
            name = input('informe o nome: ').strip()
            result = find_patient_by_name(name, cursor)
            

        elif consulta == '2':
            ID = int(input('informe o ID: ').strip())
            
        elif consulta == '3':
            pass

        elif consulta == '4':
            pass

        elif consulta == '5':
            break
        else:
            print('opção inválida, tente novamente.')