from db.connection import Connection
from model import Model
from collections import namedtuple

db = Connection.instance()
Columns = namedtuple('Columns', 'id name age')
person = Columns(id=5, name='Prossy', age=25)
company = Model(db, 'company')
company.create(person)
print(company.find_all(Columns))
