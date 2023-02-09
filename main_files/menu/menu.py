def main_menu() -> str:
    menu = """

Controle de registros do Hospital!

    1 - Acessar registro de pacientes e/ou histórico clínico
    2 - Acessar registro de médicos
    3 - Acessar registro de prontuário
    4 - Encerrar programa
    """
    print(menu)


def options_patient() -> str:
    menu = """
    1 - Criar registro na tabela
    2 - Consultar e/ou Atualizar registro na tabela 
    3 - Consultar histórico clínico
    4 - Deletar registro na tabela
    5 - Mostrar todos os registros
    6 - Encerrar programa
    """
    print(menu)


def options() -> str:
    menu = """
    1 - Criar registro na tabela
    2 - Consultar e/ou Atualizar registro na tabela
    3 - Deletar registro na tabela
    4 - Mostrar todos os registros
    5 - Encerrar programa
    """
    print(menu)


def option_choice():
    option = input("Informe a opção: ")
    return option


def submenu_medical_history():
    consulta = input("""
    1 - busca por nome 
    2 - acessar direto pelo ID do Paciente 
    3 - atualizar histórico clínico 
    4 - deletar histórico clínico
    5 - menu principal
    Sua opção: """)
    return consulta
