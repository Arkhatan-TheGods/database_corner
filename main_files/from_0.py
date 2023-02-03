import sqlite3

from os import system

import menu.menu as menu

import CRUDS.query_patient as patient_query

import CRUDS.query_doctor as doctor

import CRUDS.query_historic_clinic as historic

import CRUDS.query_medical_record as record

import CRUDS.operation_patient as patient_operation

import traceback

system('cls')


def connect_db(path_db: str) -> sqlite3.Connection:
    "this connect to db that you want, inform the: .db"

    # print('conectado.')

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

    cur.execute(doctor.query_create_doctor())

    cur.execute(

        historic.query_create_historic_clinic())

    cur.execute(

        record.query_create_medical_record())
    conn.close()

    while True:

        try:

            conn = connect_db("Hospital.db")
            cur = conn.cursor()

            menu.main_menu()

            option = menu.option_choice()

            if option == '1':

                menu.options()

                option = menu.option_choice()

                if option == '1':

                    novo = 's'

                    while novo == 's':

                        values = patient_operation.values_patient()

                        cur.execute(
                            patient_query.query_insert_patient(), values)

                        novo = input('deseja adicionar novo valor [s/n]?').strip().lower()[0]

                elif option == '2':

                    patient_operation.update_paciente(cursor=cur)

                elif option == '3':
                    ID = int(input("informe o ID a ser deletado: "))
                    cur.execute(patient_query.query_delete_patient_by_id(), (ID,))

                elif option == '4':

                    all = cur.execute(patient_query.query_show_all_patient()).fetchall()

                    for c in all:
                        print(c)

                elif option == '5':

                    print("Programa Finalizado.")

                    break

            elif option == '2':

                menu.options()

                option = menu.option_choice()

                if option == '1':
                    pass

                elif option == '2':
                    pass

                elif option == '3':
                    pass

                elif option == '4':
                    pass

                elif option == '5':
                    pass

                elif option == '6':

                    print("Programa Finalizado.")

            elif option == '3':

                menu.options()

                option = menu.option_choice()

                if option == '1':
                    pass

                elif option == '2':
                    pass

                elif option == '3':
                    pass

                elif option == '4':
                    pass

                elif option == '5':
                    pass

                elif option == '6':

                    print("Programa Finalizado.")

            elif option == '4':

                menu.options()

                option = menu.option_choice()

                if option == '1':
                    pass

                elif option == '2':
                    pass

                elif option == '3':
                    pass

                elif option == '4':
                    pass

                elif option == '5':
                    pass

                elif option == '6':

                    print("Programa Finalizado.")

            elif option == '5':

                print("Programa Finalizado.")

                break

            else:
                print(

                    "OPÇÃO INVÁLIDA, TENTE NOVAMENTE.")

            conn.commit()

        except Exception as ex:

            conn.rollback()

            print(traceback.format_exc())

        finally:
            conn_close(conn)
