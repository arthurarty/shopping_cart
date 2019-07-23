from db.connection import Connection
from db.select import Select

db = Connection.instance()
table_select = Select('company', db)
print(table_select.execute())
