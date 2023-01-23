import sqlite3

from sqlite3 import Error

from dotenv import dotenv_values


def connect_db():

    config = dotenv_values('.env')

    path_db = config.get('PATH_DATABASE') 

    connect = sqlite3.connect(path_db)

    cursor = connect.cursor()
    return connect, cursor


def create_table(query, connect_db):
    connect, cursor = connect_db
    
    cursor.execute(query)

    connect.commit()


def add_column(table_name, new_column_name, column_type, null_or_not_null):
    cursor, connect = connect_db()
    table = table_name

    new_column = new_column_name

    column_type = column_type
    
    null_or_not = null_or_not_null

    add_column = f"ALTER TABLE {table} ADD {new_column} {column_type} {null_or_not};"

    cursor.execute(add_column)

    connect.commit()


def insert_value(table_name, column_name,value_to_insert):
    cursor, connect = connect_db()
    table = table_name
    column = column_name

    value = value_to_insert

    insert = f"INSERT INTO table(column) VALUES(value);", {"table":table, "column":column, "value":value}


create_table("CREATE TABLE IF NOT EXISTS Paciente (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL);", connect_db())

