
from manager import DBManager, Field, FieldType, SqliteConnectionException


if __name__ == '__main__':
    dbm = DBManager()

    dbm.register_db("db1", "db1.sqlite3")
    dbm.register_db("db2", "db2.sqlite3")

    # use before selectng to determine exception
    try:
        dbm.insert("tablex", {})
    except SqliteConnectionException as e:
        print(f"raised: {e}")

    print("selecting db1 ...")
    dbm.select_db("db1")

    # table 1 db1
    table1_fields = [
        Field(name="no_pins", type=FieldType.INTEGER),
        Field(name="no_bolts", type=FieldType.INTEGER),
    ]

    print("create table1 in db1")
    dbm.create_table("table1", table1_fields)

    print("delete all from table1")
    dbm.delete_all("table1")

    print("insert some values into table1 ...")
    dbm.insert("table1", {"no_pins": 10, "no_bolts": 100})
    dbm.insert("table1", {"no_pins": 20, "no_bolts": 200})
    dbm.insert("table1", {"no_pins": 30, "no_bolts": 300})
    dbm.insert("table1", {"no_pins": 40, "no_bolts": 400})

    # table 2 db1
    table2_fields = [
        Field(name="id", type=FieldType.INTEGER),
        Field(name="description", type=FieldType.TEXT),
    ]

    print("create table2 in db1")
    dbm.create_table("table2", table2_fields)

    print("delete all from table2")
    dbm.delete_all("table2")

    print("insert some values into table2 ...")
    dbm.insert("table2", {"id": 1, "description": "invictificarae benedet"})
    dbm.insert("table2", {"id": 2, "description": "bla blaebare"})
    dbm.insert("table2", {"id": 3, "description": "pheritisimus pharus"})
    dbm.insert("table2", {"id": 4, "description": "velocticae gaetilus"})
