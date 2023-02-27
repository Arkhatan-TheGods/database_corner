from sqlite3 import Cursor
from typing import TypedDict, Callable, Any

Operation = TypedDict('Operation', {'execute': Callable[[str, tuple], Any], 
                                    'fetchone': Callable[[str, tuple], Any], 
                                    'fetchall': Callable[[str, tuple], Any]})

def operator(cursor: Cursor) -> Operation:
    def execute(query: str, parameters: tuple):
        return cursor.execute(query, parameters)

    def fetchone(query: str, parameters: tuple) -> tuple:
        return cursor.execute(query, parameters).fetchone()

    def fetchall(query: str, parameters: tuple) -> list[tuple]:
        return cursor.execute(query, parameters).fetchall()
    
    def all(query: str) -> list[tuple]:
        return cursor.execute(query).fetchall()

    return {"execute": execute, "fetchone": fetchone, "fetchall": fetchall, "all": all}