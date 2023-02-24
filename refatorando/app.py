from sqlite3 import connect
import traceback
from tables import entitys
import menu
from adapters import patient
import db_operations as operator

if __name__ == "__main__":

    conn = connect('hospital.db')
    cursor = conn.cursor()
    cursor.executescript(entitys())
    conn.commit()
    conn.close()

    while True:
        try:
            conn = connect('hospital.db')
            cursor = conn.cursor()
            
            menu.main()
            if menu.option() == '1':
                menu.submenu_patient()

                if menu.option() == '1':
                    #patient = adapter.new_patient()
                    #print(type(patient["create"]))
                    pass

            elif menu.option() == '5':
                print('programa finalizado')
                break

        except Exception as e:
            print(e)
            traceback.print_exc()
            if conn:
                conn.rollback()

        finally:
            if conn:
                conn.close()
