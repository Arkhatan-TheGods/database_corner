

def main() -> None:
    main = """Controle de Registros do Hospital
    1 - Pacientes
    2 - Médicos
    3 - Histórico Clínicos
    4 - Prontuários
    5 - Fechar Programa
    """
    print(main)

def option() -> str:
    return input('informe sua oção: ')

def submenu_patient() -> None:
    patient = """Controle de Pacientes
    1 - novo registro 
    2 - procurar e/ou atualizar paciente
    3 - deletar registro do paciente
    4 - voltar menu principal"""
    print(patient)

def submenu_find_or_update_patient() -> str:
    return input(
            """Consulta/Atualizar 
            [1] Nome 
            [2] CPF 
            [3] atualizar direto pelo ID 
            [4] Menu Principal Digite sua opção: """).strip()
    
