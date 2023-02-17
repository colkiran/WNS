
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="players", port=3306)

cursor = conn.cursor()

query = [
    # "insert into player values ('PL001', 'Mike Tyson', 'Boxing', '85 knockouts')",
    # "insert into player values ('PL002', 'Sachin Tendulkar', 'Cricket', '100 centuries')",
    # "insert into player values ('PL003', 'Lionel Messi', 'Football', '7 Ballondor')",
    # "insert into player values ('PL004', 'Andre Agassi', 'Tennis', '10 Grandslams')",
    # "insert into player values ('PL005', 'PV Sindhu', 'Badmiton', 'Olympic Bronze')",
    # "insert into player values ('PL006', 'Micheal Jordan', 'Basket Ball', '250 Baskets')",
]

for qry in query:
    cursor.execute(qry)

conn.commit()

conn.close()



