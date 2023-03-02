from sqlite3 import connect, Connection
import traceback
from tables import entitys
import menu
from adapters import patient, new_patient
from db_operations import operator
from patient_operation import find_patient, get_id_patient, update_patient, insert_update_patient


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
            option_menu = menu.option()
            
            if option_menu == '1':

                menu.submenu_patient()
                
                option_submenu = menu.option()
                if option_submenu == '1':
                    new = 's'
                    while new == 's':
                        id_patient = fn_patient["create"](new_patient())
                        new = input('adicionar outro paciente [s/n]? ').lower().strip()[0]
                    
                elif option_submenu == '2':
                    find = 's'
                    while find == 's':                   
                        choice = menu.submenu_find_or_update_patient()
                        result = find_patient(choice, fn_patient)
                        print(result)
                        find = input('deseja fazer nova busca [s/n]? ').lower().strip()[0]

                    update = menu.update()
                    if update == 's':
                        ID = get_id_patient(choice, result)
                        updates = update_patient(fn_patient, ID)
                        insert_update_patient(updates, fn_patient)
                        

                elif option_submenu == '5':
                    for r in fn_patient['show_all']():
                        print(r)
           
            elif option_menu == '5':
                print('programa finalizado')
                break
            
            conn_.commit()

        except Exception as e:
            print(e)
            traceback.print_exc()
            if conn_:
                conn_.rollback()

        finally:
            if conn_:
                conn_.close()
