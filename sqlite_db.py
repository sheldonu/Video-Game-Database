import sqlite3

# define the connection to the database

con = sqlite3.connect("store.db")

# define the cursor to the database

cur = con.cursor()

# create games table

cur.execute("""CREATE TABLE IF NOT EXISTS games
            (game_id INTEGER PRIMARY KEY, title VARCHAR(150), rating VARCHAR(4), 
            platform VARCHAR(75), release_date DATE, price DECIMAL(10,2), in_stock INT(1000))""")

# create customers table

cur.execute("""CREATE TABLE IF NOT EXISTS customers
            (customer_id INTEGER PRIMARY KEY, first_name VARCHAR(150), 
            last_name VARCHAR(150), email VARCHAR(150), phone CHAR(10))""")

# create orders table 

cur.execute("""CREATE TABLE IF NOT EXISTS orders
            (order_id INTEGER PRIMARY KEY, customer_id INTEGER, order_date DATE, 
            total_cost DECIMAL(10,2), FOREIGN KEY(customer_id) REFERENCES customers(customer_id))""")

# add data into games table

cur.execute("""INSERT OR IGNORE INTO games VALUES 
            (1, 'Mario Bros', 'E', 'Nintendo Switch', '2018-07-11', 59.99, 100),
            (2, 'Legend of Zelda', 'E10', 'Nintendo Switch', '2019-06-12', 69.99, 50),
            (3, 'Kirby Air Ride', 'E', 'Gamecube', '2012-01-06', 29.99, 10)""")

# add data into customers table

cur.execute("""INSERT OR IGNORE INTO customers VALUES 
            (1, 'adam', 'bingham', 'abing@example.com', 1233334444)""")

# add data into orders table

cur.execute("""INSERT OR IGNORE INTO orders VALUES 
            (1, 1, '2024-02-29', 129.99)""")

# commit everything

con.commit()

# print games table

for row in cur.execute("SELECT * FROM games"):
    print(row)
print('')

# # print customers table

for row in cur.execute("SELECT * FROM customers"):
    print(row)
print('')

# # print orders table

for row in cur.execute("SELECT * FROM orders"):
    print(row)