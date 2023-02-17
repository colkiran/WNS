
from sqlalchemy import create_engine
from  sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql+pymysql://root:@localhost:3306/players")
base = declarative_base()

class Player(base):

    __tablename__ = 'Player'
    playerid = Column(String(5), primary_key=True)
    plyname = Column(String(50))
    sport = Column(String(35))
    achvmnt = Column(String(50))

    def __init__(self, playerid, plyname, sport, achvmnt):
        self.playerid = playerid
        self.plyname = plyname
        self.sport = sport
        self.achvmnt = achvmnt

base.metadata.create_all(engine)
