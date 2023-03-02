from adapters import patient, new_patient
from db_operations import operator


def find_patient(choice: str, fn_patient) -> dict:
    if choice == '1':
        name = input('informe o nome: ').strip()
        return fn_patient["find_by_name"](name)

    elif choice == '2':
        cpf = input('informe o CPF: ').strip()
        return fn_patient["find_by_cpf"](cpf)

    elif choice == '3':
        ID = int(input("informe o ID: ").strip())
        return fn_patient["find_by_id"](ID)

    else:
        print('opção inválida, tente novamente')

# def update_patient(fn_patient) -> tuple:
#     ID = int(input("informe o ID: ").strip())
#     result = fn_patient["find_by_id"](ID)
    
#     if result:
#         print(result)
#         dados = {"nome":result[1], "cpf":result[2], "data de nascimento":result[3], "endereço":result[4]}
#         for c in dados:
#             novo_valor = input(f"novo valor para {c}: ").strip()
#             if novo_valor != "":
#                 dados[c] = novo_valor
#         values = (dados["nome"], dados["cpf"], dados["data de nascimento"], dados["endereço"], dados["id"], result[0])
#         fn_patient["update"](values)
#     else:
#         print('não encontrado.')

def get_id_patient(choice: str, result) -> int:
    if choice == '1':
        return input('informe o ID: ').strip()
    if choice == '2' or '3':
        return result[0]
   



def update_patient(fn_patient, ID) -> tuple:
    
    result = fn_patient["find_by_id"](ID)

    print(result, '\n dê enter se deseja manter os valores atuais.')
    dados = {"nome":result[1], "cpf":result[2], "data de nascimento":result[3], "endereço":result[4]}
    for c in dados:
        novo_valor = input(f"novo valor para {c}: ").strip()
        if novo_valor != "":
            dados[c] = novo_valor
    
    return (dados["nome"], dados["cpf"], dados["data de nascimento"], dados["endereço"], ID)

def insert_update_patient(values: tuple, fn_patient):
    fn_patient["update"](values)