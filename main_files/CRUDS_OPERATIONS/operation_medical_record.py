from sqlite3 import Cursor
import main_files.CRUDS_QUERYS.query_medical_record as medical_record
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


def find_by_id(cursor):
    while choice := input("""busca por id de:
    1 - paciente
    2 - doutor
    3 - histórico clínico
    digite sua opção: """).strip() != '1' or '2' or '3':
        if choice == '1':
            return cursor.execute(query_find_patient_by_id())
        elif choice == '2':
            return cursor.execute(query_find_doctor_by_id())
        elif choice == '3':
            return cursor.execute(query_find_medical_history_by_id())
        else:
            print('inválido, repita operação.')
