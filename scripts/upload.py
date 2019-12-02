# This should only ever be run when completely resetting the online couchdb database to match a local
# sqlite database file. It will take a long time to run because it has to check whether a document
# exists on the remote server or not. That is a slow process. Do not run this unless absolutely needed.

from functools import partial
import array
import couchdb
import datetime
import requests
import json
import os
import sys
import binascii
import sqlite3
import sys

language = 'phake'
rows = []

from cloudant.client import Cloudant
from cloudant.document import Document
from cloudant.database import CloudantDatabase

from auth import un, pw

client = Cloudant(un, pw, url='https://xyy.tw:5985', connect=True)
couch = client.create_database(language)

dbpath = os.path.join(os.path.dirname(sys.argv[0]), "default.db")
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

cursor.execute("SELECT * FROM `clone`")
rows = cursor.fetchall()
toremove = []
for row in rows:
	id = row[0]
	if id is not "":
		client = Cloudant(un, pw, url='https://xyy.tw:5985', connect=True)
		couch = client[language]
		doc = json.loads(row[1])
		doc['_id'] = id
		doc_exists = id in couch
		if doc_exists:
			print('skip',id)
			# pass
		else:
			my_document = couch.create_document(doc)
			print('create',id)
