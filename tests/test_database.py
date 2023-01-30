import sqlite3
import pytest
from os import system

system('cls')

@pytest.fixture(scope="session")
def setup():
    connect = sqlite3.connect("teste_hospital.db")
    connect.set_trace_callback(print)
    cursor = connect.cursor()
    cursor.execute()
    cursor.execute(create_table_pacientes())
    yield cursor, connect
    connect.close()
