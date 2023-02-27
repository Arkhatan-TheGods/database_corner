from adapters import patient, new_patient
from db_operations import operator


def patient_operation(choice: str, fn_patient) -> dict:
    while True:
        if choice == '1':
            name = input('informe o nome: ').strip()
            return fn_patient["find_by_name"](name)

        elif choice == '2':
            cpf = input('informe o CPF: ').strip()
            return fn_patient["find_by_cpf"](cpf)

        elif choice == '3':
            ID = int(input("informe o ID: ").strip())
            return fn_patient["find_by_id"](ID)

        elif choice == '4':
            break

        else:
            print('opção inválida, tente novamente')

def update_patient(fn_patient) -> tuple:
    ID = int(input("informe o ID: ").strip())
    result = fn_patient["find_by_id"](ID)
    
    if result:
        print(result)
    else:
        print('não encontrado.')