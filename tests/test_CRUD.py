import pytest
import sqlite3
from dotenv import dotenv_values


def create_table_pacientes():
    return """CREATE TABLE Pacientes(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Idade INTEGER NOT NULL,
    Entrada TEXT NOT NULL,
    Cidade TEXT NOT NULL,
    Estado TEXT NOT NULL);
    """


def insert_values_pacientes():
    return """INSERT INTO Pacientes(nome, idade, entrada, cidade, estado) VALUES
    ('Paulo Everton', 25, '01/01/2023','São Paulo', 'SP')
    """


def insert_values_pacientes2():
    return """INSERT INTO Pacientes(nome, idade, entrada, cidade, estado) VALUES
    ('Carlos Henrique', 20, '12/12/2022','Rio de Janeiro', 'RJ')
    """


def select_all():
    return """ SELECT * FROM Pacientes; """


def find_by_id(id):
    return """SELECT * FROM Pacientes WHERE ID = :id """, {"id": id}


@pytest.fixture(scope='function')
def session():
    config = dotenv_values('.env')
    path_db = config.get('PATH_DATABASE') or ""
    connect = sqlite3.connect(path_db)
    connect.set_trace_callback(print)
    cursor = connect.cursor()
    cursor.execute("DROP TABLE IF EXISTS Pacientes;")
    cursor.execute(create_table_pacientes())
    yield cursor, connect
    connect.close()


@pytest.fixture(scope='function')
def session_two():
    # config = dotenv_values('.env')
    # path_db = config.get('PATH_DATABASE') or ""
    connect = sqlite3.connect(':memory:')
    connect.set_trace_callback(print)
    cursor = connect.cursor()
    cursor.execute("DROP TABLE IF EXISTS Pacientes;")
    cursor.execute(create_table_pacientes())
    cursor.execute(insert_values_pacientes())
    cursor.execute(insert_values_pacientes2())
    connect.commit()
    yield cursor, connect
    connect.close()


def test_insert_value(session):
    cursor, connect = session
    cursor.execute(insert_values_pacientes())
    cursor.execute(select_all())
    row_total = len(cursor.fetchall())
    assert row_total == 1
    cursor.execute(insert_values_pacientes2())
    cursor.execute(select_all())
    row_total = len(cursor.fetchall())
    connect.commit()
    assert row_total == 2


def test_get_paciente(session_two):
    cursor, connect = session_two
    cursor.execute("SELECT Nome FROM Pacientes WHERE LOWER(nome) LIKE LOWER('%PAULO%')")
    record = cursor.fetchone()
    assert record[0] == 'Paulo Everton'


def test_delete_row(session_two):
    cursor, connect = session_two
    cursor.execute("DELETE FROM Pacientes WHERE id =:id ; ", {'id': 2})
    connect.commit()
    sql, id = find_by_id(2)
    cursor.execute(sql, id)
    row_total = cursor.fetchone()
    print(row_total)
    assert row_total is None


def test_insert_column(session_two):
    cursor, connect = session_two
    get_columns = "PRAGMA table_info(Pacientes);"
    cursor.execute(get_columns)
    add_column = "ALTER TABLE Pacientes ADD país VARCHAR(80);"
    cursor.execute(add_column)
    connect.commit()
    cursor.execute(get_columns)
    total_columns = len(cursor.fetchall())
    assert total_columns == 7


def test_remove_column(session_two):
    cursor, connect = session_two
    get_columns = "PRAGMA table_info(Pacientes);"
    remove_column = "ALTER TABLE Pacientes DROP COLUMN Estado;"
    cursor.execute(remove_column)
    connect.commit()
    cursor.execute(get_columns)
    total_columns = len(cursor.fetchall())
    assert total_columns == 5


def test_update_value(session_two):
    cursor, connect = session_two
    cursor.execute("UPDATE Pacientes SET Cidade = 'Cabo Frio' WHERE ID = 2;")
    cursor.execute("SELECT * FROM Pacientes WHERE ID = 2;")
    resultado = cursor.fetchone()
    connect.commit()
    assert resultado[4] == 'Cabo Frio'
