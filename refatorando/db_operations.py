from sqlite3 import Cursor

def operator(cursor: Cursor) -> dict:
    def execute(query: str, parameters: tuple):
        return cursor.execute(query, parameters)

    def fetchone(query: str, parameters: tuple) -> tuple:
        return cursor.execute(query, parameters).fetchone()

    def fetchall(query: str, parameters: tuple) -> list[tuple]:
        return cursor.execute(query, parameters).fetchall()

    return {"execute": execute, "fetchone": fetchone, "fetchall": fetchall}