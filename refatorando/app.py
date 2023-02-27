from sqlite3 import connect, Connection
import traceback
from tables import entitys
import menu
from adapters import patient, new_patient
from db_operations import operator
from patient_operation import patient_operation


if __name__ == "__main__":

    conn = connect('hospital.db')
    cursor = conn.cursor()
    cursor.executescript(entitys())
    conn.commit()
    conn.close()
    
    conn_:Connection | None = None

    while True:
        try:
            conn_ = connect('hospital.db')
            cursor = conn_.cursor()

            fn_patient=patient(operator(cursor))

            menu.main()
            if menu.option() == '1':
                menu.submenu_patient()

                if menu.option() == '1':
                    id_patient = fn_patient["create"](new_patient())
                    
                elif menu.option() == '2':
                    choice = menu.submenu_find_or_update_patient()
                    result = patient_operation(choice)

            elif menu.option() == '5':
                print('programa finalizado')
                break

        except Exception as e:
            print(e)
            traceback.print_exc()
            if conn_:
                conn_.rollback()

        finally:
            if conn_:
                conn_.close()
