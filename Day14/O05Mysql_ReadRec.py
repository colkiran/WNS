
import pymysql
from prettytable import from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", database="players", port=3306)

cursor = conn.cursor()

query = "select * from player"

cursor.execute(query)

ply_tbl = from_db_cursor(cursor)

print(ply_tbl)

conn.close()



