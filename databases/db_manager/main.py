
from manager import DBManager, Field, FieldType


if __name__ == '__main__':
    dbm = DBManager()

    dbm.register_db("db1", "db1.sqlite3")
    dbm.register_db("db2", "db2.sqlite3")

    print("selecting db1 ...")
    dbm.select_db("db1")

    table1_fields = [
        Field(name="no_pins", type=FieldType.INTEGER),
        Field(name="no_bolts", type=FieldType.INTEGER),
    ]

    print("create table1 in db1")
    dbm.create_table("table1", table1_fields)

    print("insert some values into table1 ...")
    dbm.insert("table1", "no_pins", 10)
    dbm.insert("table1", "no_pins", 20)
    dbm.insert("table1", "no_pins", 30)
    dbm.insert("table1", "no_pins", 40)

    dbm.insert("table1", "no_bolts", 70)
    dbm.insert("table1", "no_bolts", 80)
    dbm.insert("table1", "no_bolts", 90)
    dbm.insert("table1", "no_bolts", 99)
