from db.connection import Connection
from model import Model
from collections import namedtuple

db = Connection.instance()

# specify the columns to insert data into
Columns = namedtuple('Columns', 'id name age address salary')
person = Columns(id=6, name='Matthew', age=25, address='Ntinda', salary=5400)

# specify the columns to update
Row_update = namedtuple('Row_Update', 'id name age')
person_update = Row_update(id=5, name='Bony', age=6)


company = Model(db, 'company')
# company.create(person)
# print(company.find_all(Columns))
# company.update(person_update)

# delete record from the db
Del_record = namedtuple('Del_record', 'id')
person_delete = Del_record(id=1)
company.delete(person_delete)
