from asyncio.windows_events import NULL
import sqlite3 as sql
from sqlite3 import Error
# CONECION A LA BASE DE DATOS SQLITE3
DB_PATH = "db/tasks.db"
def create_connection():
    conn = None
    try:
        conn = sql.connect(DB_PATH)
    except Error as e:
        print("Error connecting to database: " + str(e))
        return NULL
    return conn

def read_file(path):
    with open(path, "r") as sql_file:
        return sql_file.read()

def create_tables():
    conn = create_connection()
    path = "db/querys/tables.sql"
    sql = read_file(path)
  
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(f"Error at create_tables() : {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    create_tables()