from sqlite3 import Cursor


# def new_patient():
#     name = input('nome: ').capitalize().strip()
#     cpf = input('CPF: ').strip()
#     born = input('data de nascimento (dd/mm/yyyy): ').strip()
#     adress = input('endereço: ').capitalize().strip()
#     return name, cpf, born, adress


# def return_new_patient(*arguments: tuple):
#     query = """INSERT INTO Paciente(Nome,CPF,Data_Nascimento,Endereco)
#     VALUES(:nome, :cpf, :dt_nasc, :endereco) ;"""
#     return cursor.execute(query, (arguments))

def patient(operation: dict) -> dict:

    def create(values: tuple) -> tuple:
        return operation["execute"]("""INSERT INTO Paciente(Nome,CPF,Data_Nascimento,Endereco)
        VALUES(:nome, :cpf, :dt_nasc, :endereco) ;""", values).rowcount

    def find_by_id(id: tuple) -> tuple:
        return operation["fetchone"]("SELECT * FROM Paciente WHERE ID = :id ;", id)

    def find_by_name(name: tuple) -> tuple:
        return operation["fetchall"]("SELECT * FROM Paciente WHERE ID = :id ;", name)

    def find_by_cpf(cpf: tuple) -> tuple:
        return operation["fetchone"]("SELECT * FROM Paciente WHERE CPF = :cpf ;", cpf)

    def update(values: tuple) -> tuple:
        return operation["execute"]("""UPDATE Paciente 
    SET Nome = :nome, CPF = :cpf, 
    Data_Nascimento = :dt_nasc, 
    Endereco = :end WHERE ID = :id ;""", values)

    return {"create": create, 
    "find_by_id": find_by_id,
    "find_by_name": find_by_name, 
    "find_by_cpf": find_by_cpf, 
    "update":update}
