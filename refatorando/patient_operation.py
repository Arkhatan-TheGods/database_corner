def patient_operation(choice: str) -> tuple:
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
