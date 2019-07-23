from connection import Connection, Table

# create db connection
db = Connection()

# create members table
members_table = Table(db, 'company', '''
      ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL''')
