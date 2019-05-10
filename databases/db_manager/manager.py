#!python

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

    def insert(self, table_name: str, fieldname: str, value: Any) -> None:
        self._execute(
            f"INSERT INTO {table_name} ({fieldname}) VALUES ({value})"
        )
