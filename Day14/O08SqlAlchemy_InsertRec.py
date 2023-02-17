
import O07SqlAlchemy_DBConnect as db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)
session = Session()

# tr = db.Player('PL001', 'Mike Tyson', 'Boxing', '85 knockouts')
# tr = db.Player('PL002', 'Sachin Tendulkar', 'Cricket', '100 centuries')
# tr = db.Player('PL003', 'Lionel Messi', 'Football', '7 Ballondor')
# tr = db.Player('PL004', 'Andre Agassi', 'Tennis', '10 Grandslams')
# tr = db.Player('PL005', 'PV Sindhu', 'Badmiton', 'Olympic Bronze')
tr = db.Player('PL006', 'Micheal Jordan', 'Basket Ball', '250 Baskets')

session.add(tr)
session.commit()
