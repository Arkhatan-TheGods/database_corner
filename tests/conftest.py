import pytest 
import sqlite3



@pytest.fixture()
def test_hospital():
    connect = sqlite3.connect("\\tests\\test_hospital.db")
    cursor = connect.cursor()
    yield connect, cursor
    connect.close()