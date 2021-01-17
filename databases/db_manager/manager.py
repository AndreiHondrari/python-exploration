#!python3

import sqlite3
import enum
from collections import namedtuple

from typing import List, Dict, Union, Any

SqliteConnection = Union[sqlite3.Connection, None]


Field = namedtuple("Field", ('name', 'type',))


class SqliteConnectionException(Exception):
    pass


class FieldType(enum.Enum):
    INTEGER = "integer"
    REAL = "real"
    TEXT = "text"


class DBManager:

    def __init__(self) -> None:
        self._databases: Dict[str, str] = {}
        self._active_db_conn: SqliteConnection = None

    def __del__(self) -> None:
        if self._active_db_conn is not None:
            self._active_db_conn.close()

    def register_db(self, alias: str, filename: str) -> None:
        self._databases[alias] = filename

    def select_db(self, alias: str) -> SqliteConnection:
        conn = sqlite3.connect(self._databases[alias])
        self._active_db_conn = conn
        return self._active_db_conn

    def _execute(self, query: str) -> None:
        if self._active_db_conn is None:
            raise SqliteConnectionException(
                "Database connection is not active!"
            )

        c = self._active_db_conn.cursor()
        c.execute(query)
        self._active_db_conn.commit()

    def create_table(self, table_name: str, fields: List[Field]) -> None:
        fields_strings = [f"{f.name} {f.type.value}" for f in fields]
        fields_query_atom = ", ".join(fields_strings)
        self._execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} ({fields_query_atom})"
        )

    def drop_table(self, table_name: str) -> None:
        self._execute(f"DROP TABLE {table_name}")

    def insert(self, table_name: str, values: Dict[str, Any]) -> None:
        fieldnames: Any = []
        fieldvalues: Any = []

        for key, val in values.items():
            fieldnames.append(key)
            fieldvalues.append(f"'{str(val)}'")

        fieldnames = ", ".join(fieldnames)
        fieldvalues = ", ".join(fieldvalues)

        self._execute(
            f"INSERT INTO {table_name} ({fieldnames}) VALUES ({fieldvalues})"
        )

    def delete_all(self, table_name: str) -> None:
        self._execute(f"DELETE FROM {table_name}")
