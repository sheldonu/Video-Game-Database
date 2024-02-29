import sqlite3

# define the connection to the database

con = sqlite3.connect("store.db")

# define the cursor to the database

cur = con.cursor()

# create games table

cur.execute("""CREATE TABLE IF NOT EXISTS 
            games(game_id INTEGER PRIMARY KEY, title VARCHAR(150), rating VARCHAR(4), 
            platform VARCHAR(75), release_date DATE, price DECIMAL(10,2), in_stock INT(1000))""")

# create customers table

cur.execute("""CREATE TABLE IF NOT EXISTS
            customers(customer_id INTEGER PRIMARY KEY, first_name VARCHAR(150), 
            last_name VARCHAR(150), email VARCHAR(150), phone CHAR(10))""")

# create orders table 

cur.execute("""CREATE TABLE IF NOT EXISTS
            orders(order_id INTEGER PRIMARY KEY, customer_id INTEGER, order_date DATE, 
            total_cost DECIMAL(10,2), FOREIGN KEY(customer_id) REFERENCES customers(customer_id))""")

# add data into games table

cur.execute("INSERT INTO games VALUES (1, 'Mario Bros', 'PG', 'Nintendo Switch', '2018-07-11', 59.99, 100)")

# add data into customers table

###

# add data into orders table

###

# get the data from the games table

cur.execute("SELECT * FROM games")

results = cur.fetchall()
print(results)