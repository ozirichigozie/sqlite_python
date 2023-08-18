import sqlite3

# conn = sqlite3.connect(':memory:')

# conn = sqlite3.connect('customer.db')

# # create a cursor
# c = conn.cursor()

# # Create a table
# # datatypes for sqlite: NULL, INT (integers), REAL (float), TEXT (string) and BLOB (Images,multimedia)
# c.execute("""CREATE TABLE customers (
# 	first_name text,
# 	last_name text,
# 	email text
# 	)
# """)

# # Insert one value at a time
# c.execute("INSERT INTO customers VALUES ('John', 'Doe', 'john@doe.com')")
# c.execute("INSERT INTO customers VALUES ('Smith', 'Code', 'codewith@smith.com')")
# c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@brown.com')")

# # Insert many values at a time
# many_customers = [
# 	('Wes', 'Brown', 'wes@bronn.com'),
# 	('Steve', 'Jobs', 'steph@cann.com'),
# 	('Dan', 'Hills', 'dan@hills.com'),
# ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# c.execute("DELETE from customers WHERE rowid = 7")

# c.execute("""UPDATE customers SET email = 'gary@brown.code'
# 	WHERE rowid = 4
# 	""")
# c.execute("""UPDATE customers SET first_name = 'Gary'
# 	WHERE rowid = 4
# """)

# c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%' ")
# c.execute("SELECT * FROM customers WHERE email LIKE '%.com' ")
# c.execute("SELECT * FROM customers WHERE first_name = 'Mary' ")

# # order by
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

# # AND and OR
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 3")

# # limit
# c.execute("SELECT rowid, * FROM customers LIMIT 3")

# # DROPPING a TABLE
# c.execute("DROP TABLE customers")

# c.execute("SELECT rowid, * FROM customers")
# items = c.fetchall()
# for item in items:
# 	print(item)

# print(f"S/N\tFULLNAME\t\tEMAIL")
# for item in items:
# 	print(f"{item[0]}\t{item[1]}\t{item[2]}\t\t{item[3]}")

# print(items)
# print(c.fetchone()[0])
# print(c.fetchmany(2))


# # commit our command
# conn.commit()

# # close your connection
# conn.close()

# print('\nCommand executed successfully...')

# Query the DB and return all records
def show_all():
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c = conn.cursor()

	# Query the Database
	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()
	
	for item in items:
		print(item)

	# commit our command
	conn.commit()

	# close your connection
	conn.close()

# add records to DB
def add_one(first,last,email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("INSERT INTO customers VALUES (?,?,?)", (first,last,email))
	conn.commit()
	conn.close()

# delete records from DB
def delete_one(id):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("DELETE FROM customers WHERE rowid = (?)", id)
	conn.commit()
	conn.close()

# add many records to a table
def add_many(list):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
	conn.commit()
	conn.close()

# WHERE clause function
def email_lookup(email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
	items = c.fetchall()
	
	for item in items:
		print(item)
	conn.commit()
	conn.close()
