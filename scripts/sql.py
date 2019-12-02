# Temporary script for adding glosses to the database table. This never needs to be run
# again. It is only being saved here for future reference

import urllib3
import shelve
import json
import os, sys, binascii
import datetime
import sqlite3
dbpath = os.path.join(os.path.dirname(sys.argv[0]), "storage.db")
conn = sqlite3.connect(dbpath)
connw = sqlite3.connect(dbpath)
cursor = conn.cursor()
cursorw = connw.cursor()

table = 'clone'

cursor.execute('SELECT * FROM `'+table+'`')
conn.commit()
datarows = cursor.fetchall()

for row in datarows:
	id = row[0]
	doc = json.loads(row[1])
	try:
		gloss = doc['sense'][0]["gloss"]['english']
	except:
		gloss = doc['sense'][0]["gloss"]
	# print(row[3])
	# print(gloss)
	try:
		cursorw.execute('UPDATE clone SET gloss="'+gloss+'" WHERE id="'+id+'";')
		connw.commit()
	except:
		print("ERROR")
