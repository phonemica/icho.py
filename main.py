from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import (QSortFilterProxyModel, Qt, QTime)
from PyQt5.QtGui import QIcon, QStandardItemModel
from PyQt5.QtWidgets import QMessageBox, QWidget
from threading import Timer
import json
import sys
import time
import uuid
from functions import *

# UI files
import ui.main as main
import ui.about as about
import ui.settings as settings
import ui.help as help

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

# global variables
language = set_language('phake')
entries = []
sorting = False
filter_text = ''
filter_text_def = ''
filter_selection = ''

class IchoDict(QtWidgets.QMainWindow, main.Ui_MainWindow):
	def __init__(self):
		global entries
		global filter_text
		global filter_selection
		super(self.__class__, self).__init__()
		self.setupUi(self)
		make_tables()
		# tweak(self) # UI adjustments not done in Designer
		disable_edits(self)

		entries = filtered(filter_text, filter_selection,'lexeme')
		populate_treeview(self.treeWidget, entries, self)  # fill the tree

		# def tweak(self):
		self.treeheader = self.treeWidget.header()
		for i in range(0, len(self.treeheader)):
			self.treeheader.setSectionResizeMode(
				i, QtWidgets.QHeaderView.Fixed)
		self.treeWidget.setColumnWidth(0, 20)
		self.treeWidget.setColumnWidth(1, 100)
		self.treeWidget.setColumnWidth(2, 100)
		self.treeWidget.setColumnWidth(3, 100)
		self.treeWidget.setRootIsDecorated(False)
		self.entry_docid.setReadOnly(True)
		self.entry_docid.setStyleSheet(
			"border: none; background-color: rgba(0,0,0,0)")
		# self.rev_entry.setReadOnly(True)
		# self.rev_entry.setStyleSheet("border: none; background-color: rgba(0,0,0,0)")
		self.button_save.setDisabled(True)
		self.button_delete.setDisabled(True)
		self.splitter.setCollapsible(0, False)
		self.splitter.setCollapsible(1, False)
		self.button_clone.setDisabled(True) # it needs to be a hassle to clone the database. right now that means commenting out this line.
		self.button_about.clicked.connect(self.about_clicked)

		# set global language
		# print('language is '+language)
		currentlangindex = self.combo_lang.findText(
			language, QtCore.Qt.MatchFixedString)
		self.combo_lang.setCurrentIndex(currentlangindex)
		self.combo_lang.currentIndexChanged.connect(self.setlanguage)
		self.combo_lang.setDisabled(True)

		selmodel = self.treeWidget.selectionModel()
		selmodel.selectionChanged.connect(self.selection_changed)
		# button triggers
		self.button_about.clicked.connect(self.about_clicked)
		self.button_clone.clicked.connect(self.clone_clicked)
		self.button_help.clicked.connect(self.help_clicked)
		self.button_sync.clicked.connect(self.sync_clicked)
		self.button_save.clicked.connect(self.update_entry)
		self.button_delete.clicked.connect(self.delete_entry)
		self.button_add.clicked.connect(self.add_entry)
		# text verification
		self.entry_lexeme.textChanged.connect(self.isblank)
		# searching
		self.entry_filter.textChanged.connect(self.filtertree)
		self.entry_filter_def.textChanged.connect(self.filtertreedef)
		self.combo_filter.currentIndexChanged.connect(self.filtertree)

		# keyboard shortcuts
		# add shortcut
		self.add_shortcut = QtWidgets.QShortcut(
			QtGui.QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_A), self)
		self.add_shortcut.activated.connect(self.add_entry)
		self.add_shortcut = QtWidgets.QShortcut(
			QtGui.QKeySequence(Qt.CTRL + Qt.Key_S), self)
		self.add_shortcut.activated.connect(self.sync_clicked)
		# delete shortcut
		self.delete_shortcut = QtWidgets.QShortcut(
			QtGui.QKeySequence(Qt.CTRL + Qt.Key_Backspace), self)
		self.delete_shortcut.activated.connect(self.delete_entry)
		self.delete_shortcut = QtWidgets.QShortcut(
			QtGui.QKeySequence(Qt.CTRL + Qt.Key_Delete), self)
		self.delete_shortcut.activated.connect(self.delete_entry)
		# enter to save on text entries
		self.entry_unicode.returnPressed.connect(self.button_save.click)
		self.entry_gloss.returnPressed.connect(self.button_save.click)
		self.entry_lexeme.returnPressed.connect(self.button_save.click)
		self.entry_phon.returnPressed.connect(self.button_save.click)
		self.photo_entry.returnPressed.connect(self.button_save.click)
		# self.alt_entry.returnPressed.connect(self.button_save.click)
		self.sound_entry.returnPressed.connect(self.button_save.click)
		self.entry_taxonomy.returnPressed.connect(self.button_save.click)

		# self.textarea_baseline.textChanged.connect(self.start_glossing)
		self.button_gloss_initial.clicked.connect(self.start_glossing)

	def update_filters(self):
		global filter_text
		global filter_text_def
		global filter_selection
		filter_text = self.entry_filter.text()
		filter_text_def = self.entry_filter_def.text()
		filter_selection = self.combo_filter.currentIndex()

	def isblank(self):
		# why cant this call directly from the connection?
		check_if_blank(self)

	def start_glossing(self):
		self.button_gloss_initial.setDisabled(True)
		self.tabs.setCurrentIndex(2)
		doGlossing(self)

	def filtertree(self,column):
		global entries
		global filter_text
		global filter_selection
		self.update_filters() # this probably slows things down. might be worth looking at.
		entries = filtered(filter_text, filter_selection, 'lexeme')
		reset_treeview(self, entries)

	def filtertreedef(self,column):
		global entries
		global filter_text_def
		global filter_selection
		self.update_filters()
		entries = filtered(filter_text_def, filter_selection, 'gloss')
		reset_treeview(self, entries)

	def setlanguage(self):
		global language
		language = self.combo_lang.currentText()

	def delete_entry(self):
		print('deleting entry')
		global entries
		global filter_text
		global filter_selection
		form = retrieve_form(self)
		buttonReply = QMessageBox.question(
			self, 'Deleting', "Are you sure you want to delete this word?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if buttonReply == QMessageBox.Yes:
			try:
				delete_entry_by(form.id)
			except:
				print('cant delete for some reason')
			self.update_filters()
			entries = filtered(filter_text, filter_selection, 'lexeme')
			reset_treeview(self, entries)
		else:
			print('deletion cancelled')

	def selection_changed(self, selected, deselected):
		indicies = self.treeWidget.selectedIndexes()
		try:
			if len(indicies) == 0:
				disable_edits(self)
			else:
				selected = [entries[index.row()]
							for index in self.treeWidget.selectedIndexes()]
				row = selected[0]
				enable_edits(self)
				populate_form(self, row)
		except:
			# this try/except is to prevent crashing when pasting long strings into the search box. otherwise can get an IndexError
			pass

	def add_entry(self):
		global entries
		global filter_text
		global filter_selection
		print('add_entry')
		id = str(uuid.uuid4())
		doc = Entry()
		doc.id = id
		doc.lexeme = ''
		doc.source = 'e'
		doc.changed = '*'
		update_status('Adding entry ' + id + '...')
		cursor.execute(
			"""INSERT INTO `edits` (`id`, `data`,`lexeme`) VALUES (?, ?, ?);""", (id, doc.json(), '',))
		conn.commit()
		self.update_filters()
		entries = filtered(filter_text, filter_selection, 'lexeme')
		reset_treeview(self, entries)
		clear_form(self)
		enable_edits(self)
		select_new_word(self, id)
		# a backup for select_new_word() not working right
		self.entry_docid.setText(id)
		self.button_save.setDisabled(True)

	def about_clicked(self):
		self.about_window = AboutWindow()
		self.about_window.show()

	def clone_clicked(self):
		global filter_text
		global filter_selection
		update_status('Cloning. This will take a while.')
		# self.settings_window = SettingsWindow()
		# self.settings_window.show()
		clone(language)  # clone to local sqlite3 if online
		update_status('Cloning complete')
		clear_form(self)
		self.update_filters()
		entries = filtered(filter_text, filter_selection, 'lexeme')
		reset_treeview(self, entries)

	def help_clicked(self):
		self.help_window = HelpWindow()
		self.help_window.show()

	def sync_clicked(self):
		print('sync_clicked')
		global entries
		global filter_text
		global filter_selection
		update_status('Trying to connect...')
		if not connected():
			print('not connected')
			error_dialog = QtWidgets.QErrorMessage()
			error_dialog.showMessage(
				'You must be connected to the internet to do this.')
			update_status('Error: You are not connected to the internet')
		else:
			print('connected')
			handle_deletions(language)
			print('deletions handled')
			update_status('Saving changes to the database...')
			upload_changes(language)
			print('changes uploaded')
			# clone(language)
			self.update_filters()
			entries = filtered(filter_text, filter_selection, 'lexeme')
			update_status('Your changes have been saved to the database')
			reset_treeview(self, entries)
			update_status('List updated')
			error_dialog = QtWidgets.QErrorMessage()
			error_dialog.showMessage(
				'Your changes have been saved to the database')

	def update_entry(self, entry):
		print('update_entry')
		global entries
		global filter_text
		global filter_selection
		form = retrieve_form(self)
		update_status('saving entry "' + form.lexeme +
					  '" - ' + form.id + '...')
		save_entry(form)
		clear_form(self)
		self.update_filters()
		entries = filtered(filter_text, filter_selection, 'lexeme')
		reset_treeview(self, entries)
		update_status(form.phonemic + ' has been saved.')
		select_new_word(self, form.id)

class AboutWindow(QtWidgets.QWidget, about.Ui_AboutDialog):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.close_button.clicked.connect(self.close_dialog)

	def close_dialog(self):
		self.hide()

class SettingsWindow(QtWidgets.QWidget, settings.Ui_Dialog):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.close_button.clicked.connect(self.close_dialog)

	def close_dialog(self):
		self.hide()

class HelpWindow(QtWidgets.QWidget, help.Ui_Dialog):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.close_button.clicked.connect(self.close_dialog)

	def close_dialog(self):
		self.hide()

def main():
	print('starting main...')
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle('fusion')
	form = IchoDict()
	print('showing form...')
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
