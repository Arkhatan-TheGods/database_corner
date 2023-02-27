from typing import TypedDict, Callable, Any

def new_patient() -> tuple:
    
    name = input("informe nome: ").strip().capitalize()
    cpf = input("informe CPF: ").strip().strip()
    born = input("data de nascimento(dd/mm/yyyy): ").strip()
    adress = input("endereço: ").capitalize().strip()
    
    return name, cpf, born, adress

Operation = TypedDict('Operation', {'execute': Callable[[str, tuple], Any], 
                                    'fetchone': Callable[[str, tuple], Any], 
                                    'fetchall': Callable[[str, tuple], Any]})

def patient(operation: Operation) -> dict:

    def create(values: tuple) -> tuple:
        
        sql="""INSERT INTO Paciente(Nome,CPF,Data_Nascimento,Endereco)
            VALUES(:nome, :cpf, :dt_nasc, :endereco);"""
                
        return operation["execute"](sql, values).rowcount
        

    def find_by_id(id: tuple) -> tuple:
        return operation["fetchone"]("SELECT * FROM Paciente WHERE ID = :id ;", id)

    def find_by_name(name: str) -> tuple:
        return operation["fetchall"]("SELECT * FROM Paciente WHERE LOWER(Nome) = LOWER(:name) LIMIT 10 ;", (f"{name}%",))

    def find_by_cpf(cpf: tuple) -> tuple:
        return operation["fetchone"]("SELECT * FROM Paciente WHERE CPF = :cpf ;", cpf)

    def update(values: tuple) -> tuple:
        return operation["execute"]("""UPDATE Paciente 
        SET Nome = :nome, CPF = :cpf, 
        Data_Nascimento = :dt_nasc, 
        Endereco = :end WHERE ID = :id ;""", values)

    def show_all() -> tuple:
        query = "SELECT * FROM Paciente;"
        return operation["fetchall"](query)

    return {"create": create,
            "find_by_id": find_by_id,
            "find_by_name": find_by_name,
            "find_by_cpf": find_by_cpf,
            "update": update}
