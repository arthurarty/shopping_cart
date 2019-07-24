from db.connection import Connection
from models.model import Model
from collections import namedtuple
from models.user_model import UserModel

db = Connection.instance()

# specify the columns to insert data into
# Columns = namedtuple('Columns', 'id name age address salary')
# person = Columns(id=6, name='Matthew', age=25, address='Ntinda', salary=5400)

# # specify the columns to update
# Row_update = namedtuple('Row_Update', 'id name age')
# person_update = Row_update(id=5, name='Bony', age=6)


# company = Model(db, 'user_table')
# Columns = namedtuple('Columns', 'email')
# user_details = Columns(email='arthur.nangai@gmail.com')
# company.create(person)
# print(company.find(user_details))
# company.update(person_update)

# delete record from the db
# Del_record = namedtuple('Del_record', 'id')
# person_delete = Del_record(id=1)
# company.delete(person_delete)

new_user = UserModel(db)
print(new_user.user_dict(email_address='arthur12.nangai@gmail.com'))
