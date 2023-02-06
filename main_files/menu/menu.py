def main_menu() -> str:
    menu = """

Controle de registros do Hospital!

    1 - acessar registro de pacientes
    2 - acessar registro de médicos
    3 - acessar registro de histórico clínico
    4 - acessar registro de prontuário
    5 - encerrar programa
    """
    print(menu)


def options() -> str:
    menu = """
    1 - criar registro na tabela
    2 - Consultar e/ou Atualizar registro na tabela
    3 - Deletar registro na tabela
    4 - Mostrar todos os registros
    5 - Encerrar programa
    """
    print(menu)

def option_choice():
    option = input("informe a opção: ")
    return option