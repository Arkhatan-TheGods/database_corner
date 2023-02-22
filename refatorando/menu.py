def main() -> str:
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

def submenu_patient() -> str:
    patient = """Controle de Pacientes
    1 - novo registro 
    2 - procurar e/ou atualizar paciente
    3 - deletar registro do paciente
    4 - voltar menu principal"""
    print(patient)