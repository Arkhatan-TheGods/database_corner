import sqlite3
from os import system
import menu.menu as menu
import CRUDS_QUERYS.query_patient as patient_query
import CRUDS_QUERYS.query_doctor as doctor_query
import CRUDS_QUERYS.query_medical_history as history_query
import CRUDS_QUERYS.query_medical_record as record_query
import CRUDS_OPERATIONS.operation_patient as patient_operation
import CRUDS_OPERATIONS.operation_doctor as doctor_operation
import CRUDS_OPERATIONS.operation_medical_history as history_operation
import CRUDS_OPERATIONS.operation_medical_record as record_operation
import traceback

system('cls')


def connect_db(path_db: str) -> sqlite3.Connection:
    "this connect to db that you want, inform the: .db"
    try:
        conn = sqlite3.connect(path_db)
    except Exception as ex:
        print(ex)
    return conn


def conn_close(conn):
    if conn:
        conn.close()


if __name__ == "__main__":

    conn = connect_db("Hospital.db")
    cur = conn.cursor()
    cur.execute(patient_query.query_create_patient())
    cur.execute(doctor_query.query_create_doctor())
    cur.execute(history_query.query_create_medical_history())
    cur.execute(record_query.query_create_medical_record())
    conn.close()
    while True:

        try:
            conn = connect_db("Hospital.db")
            cur = conn.cursor()
            menu.main_menu()
            option = menu.option_choice()
            if option == '1':
                menu.options_patient()
                option = menu.option_choice()

                if option == '1':
                    novo = 's'
                    while novo == 's':
                        values = patient_operation.values_patient()
                        cur.execute(patient_query.query_insert_patient(), values)
                        novo = input('deseja adicionar novo paciente [s/n]? ').strip().lower()[0]

                elif option == '2':
                    patient_operation.submenu_find_or_update(cursor=cur)

                elif option == '3':
                    history_operation.submenu_medical_history(cursor=cur)

                elif option == '4':
                    ID = int(input("informe o ID a ser deletado: "))
                    result = cur.execute(patient_query.query_find_patient_by_id(), (ID,)).fetchone()
                    print(
                        f"ID:{result[0]}, Nome:{result[1]}, CPF:{result[2]}, Data de Nascimento:{result[3]} Endereço:{result[4]}")
                    question = input(f"deseja realmente deletar o paciente [s/n]: ").strip().lower()[0]
                    if question == 's':
                        cur.execute(patient_query.query_delete_patient_by_id(), (ID,))

                elif option == '5':
                    all = cur.execute(patient_query.query_show_all_patient()).fetchall()
                    for c in all:
                        print(f"ID: {c[0]:.3f} NOME: {c[1]} CPF: {c[2]} DATA DE NASCIMENTO: {c[3]} ENDEREÇO: {c[4]}")

                elif option == '6':
                    print("Programa Finalizado.")
                    break

            elif option == '2':
                menu.options()
                option = menu.option_choice()

                if option == '1':
                    novo = 's'
                    while novo == 's':
                        cur.execute(doctor_query.query_insert_doctor(), doctor_operation.insert_values_into_medico())
                        novo = input('deseja adicionar novo doutor [s/n]? ').strip().lower()[0]

                elif option == '2':
                    doctor_operation.submenu_find_or_update(cursor=cur)

                elif option == '3':
                    ID = input("informe o ID a ser deletado: ")
                    result = cur.execute(doctor_query.query_find_doctor_by_id(), (ID,)).fetchone()
                    print(f'ID:{result[0]} Nome:{result[1]} CRM:{result[2]}')
                    if input('deseja realmente deletar o doutor [s/n]: ') == 's':
                        cur.execute(doctor_query.query_delete_doctor_by_id(), (ID,))

                elif option == '4':
                    all = cur.execute(doctor_query.query_Show_all_doctor())
                    for c in all:
                        print("ID: {} Nome: {} CRM: {}".format(c[0], c[1], c[2]))

                elif option == '5':
                    print("Programa Finalizado.")
                    break

            elif option == '3':
                menu.options()
                option = menu.option_choice()

                if option == '1':
                    novo = 's'
                    while novo == 's':
                        cur.execute(record_query.query_insert_medical_record(),(record_operation.values_medical_record()))
                        novo = input("novo registro [s/n]: ").strip().lower()[0]
                    pass
                elif option == '2':
                    pass

                elif option == '3':
                    pass

                elif option == '4':
                    all = cur.execute(record_query.query_show_all_medical_record())
                    for c in all:
                        print(c)
                    
                elif option == '5':
                    print("Programa Finalizado.")
                    break

            elif option == '4':
                print("Programa Finalizado.")
                break

            else:
                print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE.")
            conn.commit()

        except Exception as ex:
            conn.rollback()
            print(traceback.format_exc())

        finally:
            conn_close(conn)
