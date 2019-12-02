# this script is meant as a one time use repair for missing lexeme column values, used
# by sqlite for faster sorting. it should not be used more than once ever.

import os, sys, binascii
import sqlite3
import json
dbpath = os.path.join(os.path.dirname(sys.argv[0]), "storage.db")
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

print('Adding lexeme to sqlite3 for sorting')
print('to clone...')
query = 'SELECT * FROM `clone`'
cursor.execute(query)
conn.commit()
rows = cursor.fetchall()
for row in rows:
	data = json.loads(row[1])
	id = data['id']
	lex = data["lexeme"]
	cursor.execute("""UPDATE `clone` SET lexeme=? WHERE id= ? """, (lex, id,))
	conn.commit()

print('to edits...')
query = 'SELECT * FROM `edits`'
cursor.execute(query)
conn.commit()
rows = cursor.fetchall()
for row in rows:
	data = json.loads(row[1])
	id = data['id']
	lex = data["lexeme"]
	cursor.execute("""UPDATE `edits` SET lexeme=? WHERE id= ? """, (lex, id,))
	conn.commit()

print('Done')
