from sqlite3 import connect
import traceback
from tables import entitys
import menu
from patient_db import new_patient

if __name__ == "__main__":

    conn = connect('hospital2.db')
    cursor = conn.cursor()
    cursor.executescript(entitys())
    conn.commit()
    conn.close()

    while True:
        try:
            conn = connect('hospital2.db')
            cursor = conn.cursor()
            
            menu.main()
            if menu.option() == '1':
                menu.submenu_patient()
                
                if menu.option() == '1':
                    new = new_patient()
                    
            elif menu.option() == '5':
                print('programa finalizado')
                break

        except Exception as e:
            conn.rollback()
            print(e)
            traceback.print_exc()
        
        finally:
            if conn:
                conn.close()