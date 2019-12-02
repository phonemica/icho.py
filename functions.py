from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import (QSortFilterProxyModel, Qt, QTime)
from PyQt5.QtGui import QIcon, QStandardItemModel
from PyQt5.QtWidgets import QMessageBox
import array
import couchdb
import datetime
import requests
import json
import os
import sys
import binascii
import shelve  # used to do local data store
import sqlite3
import sys
import time
import urllib3  # only used to check if we're online

# couchd = couchdb.Server("https://xyy.tw:5985/")
# couchd.resource.credentials = (un, pw) # 31f450t4h7YFM4w

from auth import un, pw

language = 'phake'

from cloudant.client import Cloudant
client = Cloudant(un, pw, url='https://xyy.tw:5985', connect=True)
couch = client.create_database(language)
couch = client[language]

dbpath = os.path.join(os.path.dirname(sys.argv[0]), "default.db")
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

fontsize = 12

# separate function to reduce what needs to be changed in case of a switch from Qt5 down the road.
def status(message):
	print(message)
	# self.statusBar().showMessage(message)

def connected():
	# req = requests.get('http://clients3.google.com/generate_204')
	# print(req.status_code )
	# if req.status_code != 204:
	# 	raise Exception
	try:
		http = urllib3.PoolManager()
		status = http.request("GET", "https://xyy.tw")
		if status.status == 200:
			return True
		else:
			print(str(status.status))
			return False
	except:
		return False

def sort(array):
	unsorted = []
	for i, item in enumerate(array):
		data = item  # json.loads(item)
		unsorted.append([data["lexeme"], data["id"], data["source"]])
	newlist = sorted(unsorted)
	final = []
	for i, item in enumerate(newlist):
		for o, entry in enumerate(array):
			data = entry  # json.loads(entry)
			if data["id"] == item[1]:
				final.append(entry)
				break
	return array

def filtered(filt, filterstatus, column):
	start = time.time()
	edits = filter("edits", filt, filterstatus, column)
	clone = filter("clone", filt, filterstatus, column)
	merged = []
	loaded = []
	for row in edits:
		obj = row2obj(row)
		merged.append(obj)
		loaded.append(obj["id"])
	for row in clone:
		obj = row2obj(row)
		if obj["id"] not in loaded:
			merged.append(obj)
	end = time.time()
	# print(str(round(end - start, 2)) + " seconds for filtered()") # temporary for debugging
	return merged

def filtereddef(filt, filterstatus):
	start = time.time()
	edits = filterdef("edits", filt, filterstatus)
	clone = filterdef("clone", filt, filterstatus)
	merged = []
	loaded = []
	for row in edits:
		obj = row2obj(row)
		merged.append(obj)
		loaded.append(obj["id"])
	for row in clone:
		obj = row2obj(row)
		if obj["id"] not in loaded:
			merged.append(obj)
	end = time.time()
	# print(str(round(end - start, 2)) + " seconds for filtered()") # temporary for debuggin
	return merged

def make_tables():
	# Create the tables needed. Right now, `edits` and `clone` are the main tables,
	# but it might be worth having a table name match the language name.
	cursor.execute(
		"CREATE TABLE IF NOT EXISTS `edits` (`id` TEXT NOT NULL PRIMARY KEY, `data` JSON, `lexeme` TEXT, `gloss` TEXT)")
	cursor.execute(
		"CREATE TABLE IF NOT EXISTS `deletions` (`id` TEXT NOT NULL PRIMARY KEY)")
	cursor.execute(
		"CREATE TABLE IF NOT EXISTS `clone` (`id` TEXT NOT NULL PRIMARY KEY, `data` JSON, `lexeme` TEXT, `gloss` TEXT)")
	conn.commit()

def select(table):
	query = "SELECT * FROM {} ORDER BY `lexeme` ASC".format(table)
	cursor.execute(query)
	conn.commit()
	rows = cursor.fetchall()
	return rows

def filter(table, lexeme, filterstatus, column):
	if column is 'lexeme':
		if filterstatus is 1:
			query = 'SELECT * FROM {} WHERE `lexeme` LIKE "{}" COLLATE BINARY ORDER BY `lexeme` ASC, `gloss` ASC'.format(
				table, lexeme)
		else:
			if filterstatus is 2:
				query = 'SELECT * FROM {} WHERE `lexeme` LIKE "{}%" COLLATE BINARY ORDER BY `lexeme` ASC, `gloss` ASC'.format(
					table, lexeme)
			else:
				if filterstatus is 3:
					query = 'SELECT * FROM {} WHERE `lexeme` LIKE "%{}" COLLATE BINARY ORDER BY `lexeme` ASC, `gloss` ASC'.format(
						table, lexeme)
				else:
					query = 'SELECT * FROM {} WHERE `lexeme` LIKE "%{}%" COLLATE BINARY ORDER BY `lexeme` ASC, `gloss` ASC'.format(
						table, lexeme)
	else:
		query = 'SELECT * FROM {} WHERE `gloss` LIKE "%{}%" COLLATE BINARY ORDER BY `lexeme` ASC, `gloss` ASC'.format(
			table, lexeme)
	cursor.execute("PRAGMA case_sensitive_like = ON;")
	conn.commit()
	cursor.execute(query)
	conn.commit()
	rows = cursor.fetchall()
	return rows

def clone(language):
	if connected():
		# detele the clone table if it exists, then remake it
		cursor.execute("DROP TABLE IF EXISTS `clone`")
		conn.commit()  # committing here because we're dropping and creating a single table. might be unnecessary
		cursor.execute(
			"CREATE TABLE IF NOT EXISTS clone (`id` TEXT NOT NULL PRIMARY KEY, `data` JSON, `lexeme` TEXT, `gloss` TEXT)")
		conn.commit()
		for doc in couch:
		# 	print(document)
		# docs = couch.view("_all_docs", include_docs=True)
		# for doc in docs:
			try:
				test = doc['lexeme']
			except:
				doc['lexeme'] = ''
			try:
				gloss = doc['sense'][0]['gloss']['english']
			except:
				gloss = ''
			cursor.execute(
				"""INSERT INTO `clone` (`data`, `id`, `lexeme`,`gloss`) VALUES (?, ?, ?, ?)""",
				(
					json.dumps(doc),
					doc['_id'],
					doc['lexeme'],
					gloss,
				)
			)
			conn.commit()
	else:
		cursor.execute(
			"CREATE TABLE IF NOT EXISTS `clone` (`id` TEXT NOT NULL PRIMARY KEY, `data` JSON, `lexeme` TEXT, `gloss` TEXT)")

def row2obj(row):
	return json.loads(row[1])

def set_store(flag, value):
	# sets the global language and writes the store
	shelvepath = os.path.join(os.path.dirname(sys.argv[0]), "settings.db")
	store = shelve.open(shelvepath)
	try:
		store[flag] = value
	except:
		sys.stdout.write(".")
		sys.stdout.flush()
		return False
	finally:
		store.close()
	return True

def get_store(flag):
	# sets the global language and writes the store
	shelvepath = os.path.join(os.path.dirname(sys.argv[0]), "settings.db")
	store = shelve.open(shelvepath)
	try:
		value = store[flag]
	finally:
		store.close()
	return value

def update_entry(data):
	id = data["id"]
	data["_id"] = data["id"]
	datajson = json.dumps(data)
	try:
		cursor.execute(
			"""UPDATE `edits` SET data=? WHERE id= ? """, (datajson, id))
		cursor.execute(
			"""UPDATE `edits` SET lexeme=? WHERE id= ? """, (
				data["lexeme"], id)
		)
		conn.commit()
	except:
		pass
	try:
		cursor.execute(
			"""INSERT OR IGNORE INTO `edits` (`data`, `id`, `lexeme`) VALUES (?, ?,?)""",
			(datajson, id, data["lexeme"]),
		)
		conn.commit()
	except:
		pass

def delete_entry_by(id):
	print(id)
	cursor.execute("""DELETE FROM `edits` WHERE `id`=?""", (id,))
	cursor.execute("""DELETE FROM `clone` WHERE `id`=?""", (id,))
	cursor.execute(
		"""INSERT OR IGNORE INTO `deletions` (`id`) VALUES (?)""", (id,))
	conn.commit()

def handle_deletions(language):
	# language is the collection
	cursor.execute("SELECT * FROM `deletions`")
	deletions = cursor.fetchall()
	toremove = []
	for row in deletions:
		id = row[0]
		if id in couch:
			doc = couch[id]
			doc["_id"] = id
			try:
				doc["_rev"] = doc["_rev"]
			except:
				doc["_rev"] = 0
			couch[id] = doc
			print(couch[id])
			# cdb.delete(doc)
		toremove.append(id)
	for i, id in enumerate(toremove):
		cursor.execute("""DELETE FROM `deletions` WHERE `id`=?""", (id,))

def set_language(input):
	if set_store("language", input):
		language = "phake"
	return language

def save_entry(form):
	now = datetime.datetime.now()
	today = int(str(now.year) + str(now.month) + str(now.day))
	# start fix to undo earlier space removal by Ailot. this should be removed soon.
	form.date = today
	form.phonemic = form.phonemic.replace("₁", "₁ ")
	form.phonemic = form.phonemic.replace("₂", "₂ ")
	form.phonemic = form.phonemic.replace("₃", "₃ ")
	form.phonemic = form.phonemic.replace("₄", "₄ ")
	form.phonemic = form.phonemic.replace("₅", "₅ ")
	form.phonemic = form.phonemic.replace("₆", "₆ ")
	form.phonemic = form.phonemic.replace("₇", "₇ ")
	form.phonemic = form.phonemic.replace("₈", "₈ ")
	form.phonemic = form.phonemic.replace("₉", "₉ ")
	form.phonemic = form.phonemic.replace("  ", " ")
	form.phonemic = form.phonemic.replace("( ", "(")
	form.phonemic = form.phonemic.replace(" )", ")")
	form.phonemic = form.phonemic.strip()
	# end fix
	gloss = form.sense[0].gloss.english
	cursor.execute(
		"""INSERT OR IGNORE INTO `edits` (`id`) VALUES (?)""", (form.id,))
	try:
		cursor.execute(
			"""UPDATE `edits` SET data=? WHERE id= ? """, (form.json(
			), form.id)
		)
		cursor.execute(
			"""UPDATE `edits` SET lexeme=? WHERE id= ? """, (
				form.lexeme, form.id)
		)
		cursor.execute(
			"""UPDATE `edits` SET gloss=? WHERE id= ? """, (gloss, form.id))
		conn.commit()
	except:
		print("error updating")
	cursor.execute(
		"""INSERT OR IGNORE INTO `deletions` (`id`) VALUES (?)""", (form.id,)
	)
	conn.commit()

def upload_changes(language):
	# couch = couchd[language]
	cursor.execute("SELECT * FROM edits")
	edits = cursor.fetchall()
	toremove = []
	for row in edits:
		data = json.loads(row[1])
		id = data["id"]
		toremove.append(id)
		if data["lexeme"].strip() != "":
			data["changed"] = ""
			data["source"] = ""
			cursor.execute(
				"""INSERT OR IGNORE INTO `clone` (`id`) VALUES (?)""", (id,))
			conn.commit()
			if id in couch:
				# update couchdb document
				doc = couch[id]
				for key, value in data.items():
					doc[key] = data[key]
				try:
					del doc['data']
				except:
					pass
				doc.save()
				# save to clone table in sqlite
				cursor.execute(
					"""UPDATE `clone` SET lexeme=? WHERE id= ? """, (
						data["lexeme"], id)
				)
				cursor.execute(
					"""UPDATE `clone` SET data=? WHERE id= ? """, (json.dumps(
						data), id)
				)
				conn.commit()
			else:
				print(id, 'doesnt exist')
				# create document in couchdb
				try:
					couch[id] = entry
				except:
					pass
				# save to clone table in sqlite
				cursor.execute(
					"""UPDATE `clone` SET lexeme=? WHERE id= ? """, (
						data["lexeme"], id)
				)
				cursor.execute(
					"""UPDATE `clone` SET data=? WHERE id= ? """, (json.dumps(
						data), id)
				)
				conn.commit()
	for id in toremove:
		cursor.execute("""DELETE FROM `edits` WHERE `id`=?""", (id,))
	conn.commit()

#        _     _           _
#   ___ | |__ (_) ___  ___| |_ ___
#  / _ \| '_ \| |/ _ \/ __| __/ __|
# | (_) | |_) | |  __/ (__| |_\__ \
#  \___/|_.__// |\___|\___|\__|___/
#           |__/

class Definition(object):
	def __init__(self):
		self.english = ""
		self.assamese = ""

	def json(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)  # indent=4

class Morphology(object):
	def __init__(self):
		self.nominal = ""
		self.past = ""

	def json(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

class Media(object):
	def __init__(self):
		self.sound = ""
		self.photo = ""

	def json(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

class Gloss(object):
	def __init__(self):
		self.english = ""
		self.assamese = ""
		self.burmese = ""

	def json(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

class Example(object):
	def __init__(self):
		self.english = ""
		self.orthographic = ""
		self.phonemic = ""
		self.unicode = ""

	def json(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

class Sense(object):
	def __init__(self):
		self.definition = []
		self.gloss = ""
		self.pos = []

	def json(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

class Entry(object):
	def __init__(self):
		self.alt = ""  # can be song language, couplet or other
		self.changed = ""
		self.date = ""
		self.sense = []
		self.sense.append(Sense())
		self.sense[0].definition = []
		self.sense[0].definition.append(Definition())
		self.sense[0].definition[0].english = ""
		self.sense[0].gloss = Gloss()
		self.id = ""  # str(uuid.uuid4())
		self.lexeme = ""
		self.sense[0].example = Example()
		self.media = Media()
		self.media.photo = ""
		self.media.sound = ""
		self.morphology = Morphology()
		self.morphology.nominal = ""
		self.morphology.past = ""
		self.notes = ""
		self.phonemic = ""
		self.sense[0].pos.append("")
		self.source = ""
		self.taxonomy = ""
		self.unicode = ""

	def json(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

#        _                       _  __ _
#  _   _(_)  ___ _ __   ___  ___(_)/ _(_) ___
# | | | | | / __| '_ \ / _ \/ __| | |_| |/ __|
# | |_| | | \__ \ |_) |  __/ (__| |  _| | (__
#  \__,_|_| |___/ .__/ \___|\___|_|_| |_|\___|
#               |_|

def populate_treeview(tree, array, self):
	global fontsize
	start = time.time()
	count = 0

	engfont = QtGui.QFont()
	engfont.setFamily("Open Sans")
	engfont.setPixelSize(12)

	for i in range(len(array)):
		data = array[i]
		item = QtWidgets.QTreeWidgetItem(tree)
		item.setText(0, data["changed"])
		item.setTextAlignment(0, Qt.AlignCenter)
		item.setText(1, data["lexeme"])
		item.setFont(1, QtGui.QFont("Phake Script", int(1.2 * fontsize)))
		item.setText(2, data["phonemic"])
		item.setFont(2, engfont)
		try:
			item.setText(3, data["sense"][0]["gloss"]["english"])
		except:
			try:
				item.setText(3, "—" + data["sense"]
							 [0]["definition"][0]["english"])
			except:
				pass  # print('gloss missing in treeview for '+data["lexeme"])
		# item.setText(4, data["id"])
		item.setFont(3, engfont)
		item.setText(4, data["unicode"])
		item.setFont(4, QtGui.QFont("Ghin Khao", int(0.75 * fontsize)))
		count = count + 1
	# resize first two content columns with +6 extra padding
	tree.resizeColumnToContents(1)
	tree.setColumnWidth(1, tree.columnWidth(1) + 6)
	if (tree.columnWidth(1) > 100):
		tree.setColumnWidth(1, 100)
	tree.resizeColumnToContents(2)
	tree.setColumnWidth(2, tree.columnWidth(2) + 6)
	if (tree.columnWidth(2) > 125):
		tree.setColumnWidth(2, 125)
	tree.setColumnWidth(3, tree.columnWidth(3) + 6)
	if (tree.columnWidth(3) > 100):
		tree.setColumnWidth(3, 100)
	print("tree populated with " + str(len(array)) + " entries")
	self.label_word_count.setText(str(len(array)))
	end = time.time()
	# print(str(round(end - start, 2)) + ' seconds for populate_treeview()')

def editable(self):
	# array of editable entries to be enabled and disabled as needed
	array = []
	# array.append(self.alt_entry) # tangsa
	# array.append(self.nominal_entry) # tangsa
	array.append(self.definition_textarea)
	array.append(self.entry_docid)
	array.append(self.entry_gloss)
	array.append(self.entry_lexeme)
	array.append(self.entry_phon)
	array.append(self.entry_taxonomy)
	array.append(self.entry_temp)
	array.append(self.entry_unicode)
	array.append(self.example_english_entry)
	array.append(self.example_phonemic_entry)
	array.append(self.example_script_entry)
	array.append(self.notes_textarea)
	array.append(self.photo_entry)
	array.append(self.sound_entry)
	return array

def disable_edits(self):
	array = editable(self)
	for entry in array:
		entry.setDisabled(True)
	self.combo_pos.setDisabled(True)
	self.button_save.setDisabled(True)
	self.button_delete.setDisabled(True)

def enable_edits(self):
	array = editable(self)
	for entry in array:
		entry.setDisabled(False)
	self.combo_pos.setDisabled(False)
	self.button_save.setDisabled(False)
	self.button_delete.setDisabled(False)

def populate_form(self, data):
	print('populate form')
	clear_form(self)
	enable_edits(self)
	# this is to automatically limit the treeview to homographs when selecting an entry to help speed things up

	try:
		self.entry_gloss.setText(data["sense"][0]["gloss"]["english"])
	except:
		self.entry_gloss.setText("")
	try:
		self.definition_textarea.setPlainText(
			data["sense"][0]["definition"][0]["english"])
	except:
		self.definition_textarea.setPlainText("")
	try:
		self.entry_docid.setText(data["id"])
	except:
		self.entry_docid.setText("NO ID")
	try:
		self.entry_lexeme.setText(data["lexeme"])
	except:
		self.entry_lexeme.setText("")

	unilex = data["lexeme"]
	# set the unicode holder with converted lexeme.
	# this is temporary.
	unilex = unilex.replace("a", "ါ")
	unilex = unilex.replace("b", "ဗ")
	unilex = unilex.replace("c", "ꩡ")
	unilex = unilex.replace("d", "ဒ")
	unilex = unilex.replace("e", "ေ")
	unilex = unilex.replace("f", "ၸ")
	unilex = unilex.replace("g", "င")
	unilex = unilex.replace("h", "ꩭ")
	unilex = unilex.replace(" i", "ိ")
	unilex = unilex.replace("i", "ိ")
	unilex = unilex.replace("j", "")
	unilex = unilex.replace("k", "က")
	unilex = unilex.replace("l", "လ")
	unilex = unilex.replace("m", "မ")
	unilex = unilex.replace("n", "ꩫ")
	unilex = unilex.replace("o", "ွ")
	unilex = unilex.replace("p", "ပ")
	unilex = unilex.replace("q", "်")
	unilex = unilex.replace("r", "ꩺ")
	unilex = unilex.replace("s", "ꩢ")
	unilex = unilex.replace("t", "တ")
	unilex = unilex.replace("u", "ု")
	unilex = unilex.replace("v", "ထ")
	unilex = unilex.replace("w", "ဝ")
	unilex = unilex.replace("x", "ၵ")
	unilex = unilex.replace("y", "ယ")
	unilex = unilex.replace("z", "꩸")
	unilex = unilex.replace("A", "ဢ")
	unilex = unilex.replace("B", "ꩰ")
	unilex = unilex.replace("C", "ႊ")
	unilex = unilex.replace("D", "ꩰ")
	unilex = unilex.replace("E", "ၞ်")
	unilex = unilex.replace("F", "်ံ")
	unilex = unilex.replace("G", "ႇ")
	unilex = unilex.replace("H", "ႈ")
	unilex = unilex.replace("I", "ီ")
	unilex = unilex.replace("$", "ီ")
	unilex = unilex.replace("J", "ို")
	unilex = unilex.replace("K", "္က")
	unilex = unilex.replace("L", "း")
	unilex = unilex.replace("M", "ံ")
	unilex = unilex.replace("N", "ၺ")
	unilex = unilex.replace("O", "ႉ")
	unilex = unilex.replace("P", "္ပ")
	unilex = unilex.replace("Q", "Q")
	unilex = unilex.replace("R", "ြ")
	unilex = unilex.replace("S", "꩷")
	unilex = unilex.replace("T", "္တ")
	unilex = unilex.replace("U", "ုု")
	unilex = unilex.replace("V", "႒")
	unilex = unilex.replace("W", "ွ်")
	unilex = unilex.replace("X", "ႜ")
	unilex = unilex.replace("Y", "ျ")
	unilex = unilex.replace("Z", "ၞ")
	unilex = unilex.replace("^", "ာ")
	print("LEXEME: " + unilex)
	try:
		self.entry_temp.setText(unilex)
	except:
		self.entry_temp.setText("၀")
	try:
		self.entry_unicode.setText(data["unicode"])
	except:
		self.entry_unicode.setText("")
	try:
		self.notes_textarea.setPlainText(data["notes"])
	except:
		self.notes_textarea.setPlainText("")
	try:
		self.entry_phon.setText(data["phonemic"])
	except:
		self.entry_phon.setText("")
	try:
		self.photo_entry.setText(data["media"]["photo"])
	except:
		self.photo_entry.setText("")
	try:
		self.example_english_entry.setText(
			data["sense"][0]["example"]["english"])
	except:
		self.example_english_entry.setText("")
	try:
		self.example_script_entry.setText(
			data["sense"][0]["example"]["script"])
	except:
		self.example_script_entry.setText("")
	try:
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"N", "ŋ")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"j", "ɛ")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"q", "ɔ")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"A", "ā")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"U", "ū")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"B", "β")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"E", "ē")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"kh", "kʰ")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"ph", "pʰ")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"th", "tʰ")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"v", "ü")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"z", "ə")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"I", "ī")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"J", "ɛ̄")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"1", "₁")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"2", "₂")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"3", "₃")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"4", "₄")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"5", "₅")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"6", "₆")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"7", "₇")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"8", "₈")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"9", "₉")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			"( ", "(")
		data["sense"][0]["example"]["phonemic"] = data["sense"][0]["example"]["phonemic"].replace(
			" )", ")")
		self.example_phonemic_entry.setText(
			data["sense"][0]["example"]["phonemic"])
	except:
		self.example_phonemic_entry.setText("")
	try:
		pos = data["sense"][0]["pos"][0]
	except:
		pos = ''
	if (pos == 'n.'):
		pos = "noun"
	if (pos == 'v.'):
		pos = "verb"
	if (pos == 'adj.'):
		pos = "adjective"
	if (pos == 'adv.'):
		pos = "adverb"
	try:
		comboindex = self.combo_pos.findText(pos, QtCore.Qt.MatchFixedString)
	except:
		comboindex = -1
	self.combo_pos.setCurrentIndex(0)
	if comboindex >= 0:
		self.combo_pos.setCurrentIndex(comboindex)
	try:
		self.sound_entry.setText(data["media"]["sound"])
	except:
		self.sound_entry.setText("")
	status('Opening "' + data["phonemic"] + '"...')
	self.entry_taxonomy.setText(data["taxonomy"])
	self.button_save.setDisabled(False)
	self.button_delete.setDisabled(False)

def clear_form(self):
	self.combo_pos.setCurrentIndex(0)
	array = editable(self)
	for entry in array:
		try:
			entry.setText("")
		except:
			entry.setPlainText("")
	disable_edits(self)

def retrieve_form(self):
	entry = Entry()
	#entry.alt = self.alt_entry.text().strip()
	entry.changed = "*"
	entry.sense[0].definition[0].english = self.definition_textarea.toPlainText(
	).strip()
	entry.sense[0].gloss.english = self.entry_gloss.text().strip()
	entry.sense[0].example.script = self.example_script_entry.text().strip()
	entry.sense[0].example.english = self.example_english_entry.text().strip()
	entry.sense[0].example.phonemic = self.example_phonemic_entry.text().strip()
	entry.id = self.entry_docid.text().strip()
	entry.lexeme = self.entry_lexeme.text().strip()
	entry.media.photo = self.photo_entry.text().strip()
	entry.media.sound = self.sound_entry.text().strip()
	#entry.morphology.nominal = self.nominal_entry.text().strip()
	entry.morphology.past = self.entry_unicode.text().strip()
	entry.notes = self.notes_textarea.toPlainText().strip()
	entry.phonemic = self.entry_phon.text().strip()
	entry.sense[0].pos[0] = self.combo_pos.currentText()
	entry.source = "e"
	entry.taxonomy = self.entry_taxonomy.text().strip()
	entry.unicode = self.entry_unicode.text().strip()
	return entry

def check_if_blank(self):
	if (self.entry_lexeme.text().strip() == ''):
		self.button_save.setDisabled(True)
	else:
		self.button_save.setDisabled(False)

def reset_treeview(self, entries):
	start = time.time()
	tree = self.treeWidget
	tree.clearSelection()
	clear_treeview(tree)
	tree.horizontalScrollBar().setValue(0)
	populate_treeview(tree, entries, self)  # fill the tree
	end = time.time()
	# print(str(round(end - start, 2)) + ' seconds for reset_treeview()')

def clear_treeview(tree):
	start = time.time()
	iterator = QtWidgets.QTreeWidgetItemIterator(tree)
	while iterator.value():
		iterator.value().takeChildren()
		iterator += 1
	i = tree.topLevelItemCount()
	while i > -1:
		tree.takeTopLevelItem(i)
		i -= 1
	end = time.time()
	# print(str(round(end - start, 2)) + ' seconds for clear_treeview()')

def select_new_word(self, id):
	self.treeWidget.horizontalScrollBar().setValue(0)
	iterator = QtWidgets.QTreeWidgetItemIterator(self.treeWidget)
	while iterator.value():
		if (iterator.value().text(4) == id):
			iterator.value().setSelected(True)
			self.entry_lexeme.setFocus()
			break
		else:
			iterator += 1

#        _               _
#   __ _| | ___  ___ ___(_)_ __   __ _
#  / _` | |/ _ \/ __/ __| | '_ \ / _` |
# | (_| | | (_) \__ \__ \ | | | | (_| |
#  \__, |_|\___/|___/___/_|_| |_|\__, |
#  |___/                         |___/

wordbreak = " "
sentencebreak = "."
gloss_store = []
para_count = []
fulltext = ""

class wordClass:
	def __init__(self, word, disp, anch, notes):
		self.disp = word
		self.anch = ""
		self.notes = ""

# cuts sentence into words. currently requires breaking character. 對不起，漢字。
def splitSentence(input):
	result = []
	input = (
		input + " "
	)  # this is a dumb solution to the last word being ignored by the following for loop.
	word = ""
	for character in input:
		if character is not wordbreak:
			word += character
		else:
			result.append(word)
			word = ""
	return result

# splits paragraphs into sentences, requires full stop equivalent glyph
def splitParagraph(input):
	block = []
	sentence = ""
	for character in input:
		if character is not sentencebreak:
			sentence += character
		else:
			block.append(sentence.strip())
			sentence = ""
	return block

def makeObjFromText(input):  # not currently used
	textobj = splitParagraph(input)
	i = 0
	for sent in textobj:
		textobj[i] = splitSentence(sent)
		i += 1
	return textobj

def checkDictForMatches(word):
	query = "SELECT * FROM edits WHERE lexeme LIKE {} ORDER BY `lexeme` ASC".format(
		word)
	cursor.execute(query)
	conn.commit()
	rows = cursor.fetchall()
	result = []
	for entry in dictionary:
		if entry["orth"] == word:
			word = wordClass(word)
			word["id"] = entry["id"]  # internal unique identifier
			word["orth"] = entry["orth"]
			word["phon"] = entry["phon"]
			word["pos"] = entry["pos"]
			result.append(word)
		else:
			word = wordClass(word)
			# if there is no matching entry just make a new object
			result.append(word)

def clearLayout(layout):
	while layout.count():
		child = layout.takeAt(0)
		if child.widget() is not None:
			child.widget().deleteLater()
		elif child.layout() is not None:
			clearLayout(child.layout())

def indexChanged(self):
	# phrase_store = []
	global fulltext
	for row in range(len(fulltext)):
		for col in range(len(fulltext[row])):
			sentence_block = self.glossbox.itemAtPosition(row, 0)
			newgloss = sentence_block.itemAtPosition(1, col)
			cursor.execute(
				'SELECT * FROM edits WHERE lexeme LIKE "{}" AND gloss LIKE "{}" LIMIT 0,1'.format(
					fulltext[row][col]["lex"], fulltext[row][col]["gloss"]
				)
			)
			conn.commit()
			rows = cursor.fetchall()
			fulltext[row][col]["gloss"] = newgloss.widget().currentText()
			posval = sentence_block.itemAtPosition(2, col)
			phonval = sentence_block.itemAtPosition(3, col)
			# now do it again to get the updated part of speech, etc
			cursor.execute(
				'SELECT * FROM edits WHERE lexeme LIKE "{}" AND gloss LIKE "{}" LIMIT 0,1'.format(
					fulltext[row][col]["lex"], fulltext[row][col]["gloss"]
				)
			)
			conn.commit()
			rows = cursor.fetchall()
			fulltext[row][col]["id"] = rows[0][0]
			try:
				posrow = json.loads(rows[0][1])
				posrow = posrow["sense"][0]["pos"][0]
			except:
				posrow = ""
			try:
				phonrow = json.loads(rows[0][1])
				phonrow = phonrow["phonemic"]
			except:
				phonrow = ""
			posval.widget().setText(posrow)
			phonval.widget().setText(phonrow)

def splitText(input):  # this is only for getting nested arrays from the text box
	output = splitParagraph(input)
	for i in range(len(output)):
		output[i] = splitSentence(output[i])
		for e in range(len(output[i])):
			lex = output[i][e]
			output[i][e] = {}
			output[i][e]["lex"] = lex
			output[i][e]["id"] = ""
	return output

def StaticLabel(self, text):
	label = QtWidgets.QLabel(self.layoutWidget)
	# label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse | QtCore.Qt.TextSelectableByKeyboard)
	label.setText(text)
	return label

def update_status(status):
	print(status)

def SelectablePhakeLabel(self, text):
	label = QtWidgets.QLabel(self.layoutWidget)
	label.setFont(QtGui.QFont("Phake Script", int(16)))
	label.setTextInteractionFlags(
		QtCore.Qt.TextSelectableByMouse | QtCore.Qt.TextSelectableByKeyboard)
	label.setText(text)
	return label

def populateGlossingTab(
		self
):  # this takes an object, from splitText() or elsewhere, and populates the glossing tab
	global fulltext
	spacer_h = QtWidgets.QSpacerItem(
		0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
	)
	spacer_v = QtWidgets.QSpacerItem(
		0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
	)
	# this should only happen on resets or first run through
	clearLayout(self.glossbox)
	e = 0  # used to place the final horizontalß spacer
	for i in range(len(fulltext)):  # each row
		row = QtWidgets.QGridLayout()
		for e in range(len(fulltext[i])):
			lex = SelectablePhakeLabel(self, fulltext[i][e]["lex"])
			row.addWidget(lex, 0, e)

			com = QtWidgets.QComboBox(self)
			com.setFont(QtGui.QFont("Open Sans", 10))
			com.activated.connect(lambda: indexChanged(self))
			cursor.execute(
				'SELECT * FROM edits WHERE lexeme LIKE "{}" ORDER BY gloss ASC'.format(
					fulltext[i][e]["lex"]
				)
			)
			conn.commit()
			rows = cursor.fetchall()
			for o in range(len(rows)):
				com.addItem(rows[o][3])
			row.addWidget(com, 1, e)
			fulltext[i][e]["gloss"] = com.currentText()
			try:  # get rows data
				idrow = rows[0][0]
			except:
				idrow = ""
			try:
				posrow = json.loads(rows[0][1])
				posrow = posrow["sense"][0]["pos"][0]
			except:
				posrow = ""
			try:
				pron = json.loads(rows[0][1])
				pron = pron["phonemic"]
			except:
				pron = ""

			pos = StaticLabel(self, posrow)
			row.addWidget(pos, 2, e)

			phn = StaticLabel(self, pron)
			row.addWidget(phn, 3, e)

			# idl = StaticLabel(self,idrow)
			# row.addWidget(idl,3,e)

			buttonholder = QtWidgets.QHBoxLayout()
			plusbuttonleft = QtWidgets.QPushButton('|<-')
			plusbuttondel = QtWidgets.QPushButton('X')
			plusbuttonright = QtWidgets.QPushButton('->|')

			plusbuttonright.clicked.connect(partial(add_to_the_right, e))
			plusbuttonleft.clicked.connect(partial(add_to_the_left, e))
			plusbuttondel.clicked.connect(partial(delete_this, e))

			buttonholder.addWidget(plusbuttonleft)
			buttonholder.addWidget(plusbuttondel)
			buttonholder.addWidget(plusbuttonright)

			plusbuttonleft.setFixedWidth(30)
			plusbuttondel.setFixedWidth(30)
			plusbuttonright.setFixedWidth(30)
			row.addLayout(buttonholder, 4, e)

		row.addItem(spacer_h, 0, e + 1)
		self.glossbox.addLayout(row, i, 0)
	self.glossbox.addItem(spacer_v)

def delete_this(e):
	print("delete " + str(e))

def add_to_the_right(e):
	print("add right of " + str(e))

def add_to_the_left(e):
	print("add left of " + str(e))

def doGlossing(self):  # this is only for the first time it's done
	global fulltext
	fulltext = splitText(self.textarea_baseline.toPlainText())
	populateGlossingTab(self)
