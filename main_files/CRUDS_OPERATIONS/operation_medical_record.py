from sqlite3 import Cursor
import main_files.CRUDS_QUERYS.query_medical_record as record_query
from main_files.CRUDS_QUERYS.query_patient import query_find_patient_by_id
from main_files.CRUDS_QUERYS.query_doctor import query_find_doctor_by_id
from main_files.CRUDS_QUERYS.query_medical_history import query_find_medical_history_by_id


def values_medical_record():
    id_patient = int(input("informe o id do paciente: ").strip())
    id_doctor = int(input("informe o id do médico: ").strip())
    id_history = int(input("informe o id do histórico clínico: ").strip())
    description = input("descrição dos sintomas: ").strip()
    data = input("informe a data(dd/mm/yyyy): ")
    return id_patient, id_doctor, id_history, description, data

def insert_medical_record(values, cursor):
    return cursor.execute(record_query.query_insert_medical_record(), (values))

def get_id():
    return int(input("informe o ID: ").strip())


def find_by_id(ID, cursor):
    "this function find by id in table patient or doctor to return the lines with limit in sql query."
    while choice := input("""busca por id de:
    1 - paciente
    2 - doutor
    3 - histórico clínico
    digite sua opção: """).strip() != '1' or '2':
        if choice == '1':
            return cursor.execute(query_find_patient_by_id(), (ID,)).fetchone(), '1'
        elif choice == '2':
            return cursor.execute(query_find_doctor_by_id(), (ID,)).fetchone(), '2'
        else:
            print('inválido, repita operação.')


def find_medical_record_by_patient(ID, cursor):
    return cursor.execute(record_query.query_find_medical_record_by_id_patient(), (ID,)).fetchone()

def find_medical_record_by_doctor(ID, cursor):
    return cursor.execute(record_query.query_find_medical_record_by_id_doctor(), (ID,)).fetchall()


def submenu_medical_record(cursor):
    while True:
        consulta = input("""
        1 - consulta por nome do paciente ou médico
        2 - consulta por id do paciente ou médico
        3 - atualizar por id do paciente 
        4 - menu principal """).strip().lower()[0]
        if consulta == '1':
            ID = get_id()
            result, choice = find_by_id(ID, cursor)
            for c in result:
                print(c)
            
            if choice == '1':
                ID = get_id()
                found = find_medical_record_by_patient(ID, cursor)
                
                if found is None:
                    print("Histórico Clínico não existe")
                    
                    if input("deseja criar? [s/n]").strip().lower()[0] == 's':
                        values = values_medical_record()
                        insert_medical_record(values, cursor)

                else:
                    for c in found:
                        print(c)
            
            elif choice == '2':
                ID = get_id()
                found = find_medical_record_by_doctor(ID, cursor)
                
                if found is None:
                    print("Histórico Clínico não existe")
                                        
                else:
                    print(found)
                if input("deseja criar um Prontuário? [s/n]").strip().lower()[0] == 's':
                        values = values_medical_record()
                        insert_medical_record(values, cursor)
                
            else:
                print('opção inválida, tente novamente,')

        elif consulta == '2':
            pass
        elif consulta == '3':
            pass
        elif consulta == '4':
            break
        else:
            print('inválido tente novamente.')