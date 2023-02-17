

import pymysql
from prettytable import from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", database="players", port=3306)

cursor = conn.cursor()

query = "update player set achievement = '96 knock outs' where plyid = 'PL001'"

# delete player where plyid = 'PL005'

cursor.execute(query)

conn.close()



