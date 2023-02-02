import sqlite3
import Exception
from os import system

system('cls')


def connect(database):
    try:
        conn = sqlite3.connect(database)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return conn

