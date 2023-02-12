from sqlite3 import Cursor
import main_files.CRUDS_QUERYS.query_medical_record as medical_record


def values_medical_record:
    id_patient = int(input("informe o id do paciente: ").strip())
    id_doctor = int(input("informe o id do médico: ").strip())
    id_history = int(input("informe o id do histórico clínico: ").strip())
    description = input("descrição dos sintomas: ").strip()
