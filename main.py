from db.connection import Connection
from model import Model
from collections import namedtuple

db = Connection.instance()
# table_select = Select('company', db)
# print(table_select.execute())
company = Model(db, 'company')
print(company.find_all())

Table = namedtuple('Table', 'id name age')
person = Table(id=4, name='Gab', age=34)
company.create(person)
