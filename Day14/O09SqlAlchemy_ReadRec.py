
import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://root:@localhost:3306/players")
connection = engine.connect()
metadata = db.MetaData()

Player = db.Table('player', metadata, autoload=True, autoload_with=engine)

query = db.select([Player])

result = connection.execute(query)

for rec in result.fetchall():
    print(rec)
