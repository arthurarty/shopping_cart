from db.connection import Connection
from model import Model
from collections import namedtuple

db = Connection.instance()
Columns = namedtuple('Columns', 'id name age address salary')
person = Columns(id=6, name='Matthew', age=25, address='Ntinda', salary=5400)
Row_update = namedtuple('RowUpdate', 'id name age')
person_update = Row_update(id=5, name='Bony', age=6)
company = Model(db, 'company')
# company.create(person)
print(company.find_all(Columns))
company.update(person_update)
