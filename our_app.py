import database

# # add one record
# database.add_one('Sarah', 'Gates', 'sarah@gates.com')

# # delete record with rowid as string
# database.delete_one('3')

# add many records
stuff = [
	('Ann', 'Gregg', 'ann@greg.com'),
	('Chi', 'Oziri', 'chi@ozi.com'),
]

# database.add_many(stuff)

# # show all the records
# database.show_all()

# WHERE clause fx to lookup email
database.email_lookup('chi@ozi.com')
