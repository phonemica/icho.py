print('')
print('WARNING:')
print('This script is to import a json file, taken from Metric,')
print('and convert it to an SQLite3 database. Do not use this')
print('script unless actually necessary.')
print('')
print('To run, you will need to uncomment the remaining lines.')

# Uncomment everything below this line

# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets, uic
# from PyQt5.QtGui import QIcon, QStandardItemModel
# from PyQt5.QtCore import (QSortFilterProxyModel, Qt, QTime)
# from PyQt5.QtWidgets import QMessageBox, QWidget
# import uuid
# from threading import Timer
# import time
# from functions import *
# from objects import Entry, Morphology, Definition, Media
# from actions import *
# import adjustments as adjustments
# import json
#
# with open ('2018-02-02 ailot.json') as f:
# 	docs = json.load(f)
# 	rows = docs['rows']
# count = 0
# for item in rows:
# 	#if count < 5:
# 		doc = Entry()
# 		doc.sense = []
# 		doc.sense.append(Sense())
# 		doc.sense[0].definition = []
# 		doc.sense[0].definition.append(Definition())
# 		doc.sense[0].gloss = Gloss()
# 		doc.sense[0].pos = []
# 		doc.sense[0].example = Example()
# 		lex = ''
# 		try:
# 			doc.lexeme = item['doc']['lexeme']
# 			lex = item['doc']['lexeme']
# 		except:
# 			doc.lexeme = ''
# 		try:
# 			doc.phonemic = item['doc']['phonemic']
# 		except:
# 			doc.phonemic = ''
# 		try:
# 			doc.sense[0].pos = []
# 			doc.sense[0].pos.append(item['doc']['sense'][0]['pos'][0])
# 		except:
# 			doc.sense[0].pos = []
# 		try:
# 			doc.sense[0].gloss.english = item['doc']['sense'][0]['gloss']['english']
# 		except:
# 			doc.sense[0].gloss = ''
# 		try:
# 			doc.sense[0].definition[0].english = item['doc']['sense'][0]['definition'][0]['english']
# 		except:
# 			doc.sense[0].definition[0].english = ''
# 		id = str(uuid.uuid4())
# 		doc.id = id
# 		sys.stdout.write(lex+' ')
# 		sys.stdout.flush()
# 		if lex is not '':
# 			cursor.execute("""INSERT INTO `edits` (`id`, `data`, `lexeme`) VALUES (?, ?, ?);""", (id, doc.json(), lex))
# 			conn.commit()
# 		count = count + 1
