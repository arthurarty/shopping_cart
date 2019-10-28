from connection import Connection
from connection.table import Table


# create db connection
db = Connection()

# create users' table
users_table = Table(db, 'user_table', '''
      ID SERIAL PRIMARY KEY,
      EMAIL          TEXT    NOT NULL UNIQUE,
      PASSWORD       TEXT    NOT NULL,
      DATE_CREATED   TIMESTAMP    NOT NULL
      ''')

# create product table
product_table = Table(db, 'product', '''
      ID SERIAL PRIMARY KEY,
      NAME           VARCHAR(255)    NOT NULL,
      PRICE          INT    NOT NULL,
      DATE_CREATED   TIMESTAMP    NOT NULL,
      UNIQUE (NAME, PRICE)
      ''')

# create cart table
cart_table = Table(db, 'cart', '''
      ID SERIAL PRIMARY KEY,
      USER_ID INT,
      FOREIGN KEY (USER_ID)
      REFERENCES user_table (ID)
      ON DELETE CASCADE
      ''')

# table to track cart - product many to many relationship
cart_product_table = Table(db, 'cart_product', '''
      ID SERIAL PRIMARY KEY,
      PRODUCT_ID INT,
      FOREIGN KEY (PRODUCT_ID)
      REFERENCES product (ID)
      ON DELETE CASCADE,
      CART_ID INT,
      FOREIGN KEY (CART_ID)
      REFERENCES cart (ID)
      ON DELETE CASCADE
      ''')
