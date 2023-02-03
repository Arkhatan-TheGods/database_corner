import sqlite3

from dotenv import dotenv_values

from time import sleep

from os import system

from datetime import date, datetime

import CRUDS.query_patient as patient_query

import CRUDS.query_patient as patient_operation

import main_files.menu.menu


system('cls')


# cria conexão com o banco

def connect_db(path_db: str) -> sqlite3.Connection:
    "this connect to db that you want, inform the: .db"

    # print('conectado.')

    try:

        conn = sqlite3.connect(path_db)

    except Exception as ex:

        print(ex)
    return conn


# fecha a conexão com o banco

def conn_close(conn):

    if conn:
        conn.close()


if __name__ == "__main__":

    conn = connect_db("Hospital.db")
    cur = conn.cursor()

    fk = cur.execute('PRAGMA foreign_keys = ON;')

    # cur.execute(cp.create_table_paciente())

    # create_table_medico(cursor=cur)

    # create_table_historico_clinico(cursor=cur)

    # create_table_prontuario(cursor=cur)
    conn_close(conn)

    while True:

        try:

            conn = connect_db("Hospital.db")
            cur = conn.cursor()

            print("\nBem-Vindo ao controle de registros do hospital.")

            # main_menu()
            options()

            option = input("digite sua opção: ").strip()

            if option == '1':

                # cp.insert_values_into_paciente(cursor=cur)

                cur.execute(cp.query_step_insert(), cp.values_paciente())

            elif option == '2':

                pacientes = cp.find_paciente(cursor=cur)

                for c in pacientes:
                    print(c)

            elif option == '3':
                paciente = cp.update_paciente(cursor=cur)

                # for c in paciente:

                #    print(c)

            elif option == '4':
                cp.del_paciente(cursor=cur)

            elif option == '5':

                lista = show_all(cursor=cur)

                for c in lista:
                    print(c)

            elif option == '6':

                print('programa finalizado.')
                conn_close(conn)

                sleep(1)

                break

                exit()

            else:

                option = input("opção inválida, digite novamente: ")

            conn.commit()

        except Exception as ex:

            print(ex)

            conn.rollback()

        finally:
            conn_close(conn)
