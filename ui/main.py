from PyQt5 import QtCore, QtGui, QtWidgets

fontsize = 12
engfont = QtGui.QFont()
engfont.setFamily("Open Sans")
engfont.setPixelSize(fontsize)
smallfont = QtGui.QFont()
smallfont.setFamily("Open Sans")
smallfont.setPixelSize(int(fontsize*0.9))

styleSheet = """
QTreeView {
	alternate-background-color: #aaa;
}
QTreeView::item {
	border-left: 10px solid #000
}
"""

def horizontal_line():
	line = QtWidgets.QFrame()
	line.setFrameShape(QtWidgets.QFrame.HLine)
	line.setFrameShadow(QtWidgets.QFrame.Sunken)
	return line

def add_widget(parent,children):
	for x in range (0, len(children)):
		parent.addWidget(children[x])

def add_layout(parent,children):
	for x in range (0, len(children)):
		parent.addLayout(children[x])

def new_qt_combo(self,name,length,contents=[]):
	global fontsize
	combo = QtWidgets.QComboBox()
	combo.setMinimumSize(QtCore.QSize(50, 0))
	combo.setMaximumSize(QtCore.QSize(200, 16777215))
	combo.setFont(engfont)
	combo.setObjectName(name)
	for x in range(0, length):
		combo.addItem("")
	return combo

def new_button(self,name):
	button = QtWidgets.QPushButton()
	button.setObjectName(name)
	button.setFont(engfont)
	return button

def new_qt_entry(self,name,placeholder,script='def'):
	global fontsize
	entry = QtWidgets.QLineEdit(self.layoutWidget)
	entry.setFont(engfont)
	entry.setText("")
	entry.setPlaceholderText(placeholder)
	entry.setMinimumSize(QtCore.QSize(200, 2*fontsize))
	entry.setMaximumSize(QtCore.QSize(500, 2*fontsize))
	entry.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
	entry.setObjectName(name)
	entry.setFont(engfont)
	if script is 'pha':
		entry.setFont(QtGui.QFont("Phake Script", int(fontsize*1.2)))
	if script is 'mya':
		entry.setFont(QtGui.QFont("Ghin Khao", int(0.75*fontsize)))
	return entry

def new_qt_hbox(self, name):
	layout = QtWidgets.QHBoxLayout()
	layout.setContentsMargins(0, 0, 0, 0)
	layout.setObjectName(name)
	return layout

def new_qt_label(self,name,text="blank"):
	label = QtWidgets.QLabel(self.layoutWidget)
	label.setObjectName(name)
	label.setFont(engfont)
	label.setText(text)
	return label

def new_qt_vbox(self, name):
	layout = QtWidgets.QVBoxLayout()
	layout.setContentsMargins(0, 0, 0, 0)
	layout.setObjectName(name)
	return layout

class Ui_MainWindow(object):
	global fontsize
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1000, 700)
		MainWindow.setDocumentMode(False)
		#MainWindow.setStyleSheet(styleSheet)
		MainWindow.setFont(engfont)

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		# main layout container
		self.vertical_container = QtWidgets.QVBoxLayout(self.centralwidget)
		self.vertical_container.setContentsMargins(5, 5, 5, 5)
		self.vertical_container.setSpacing(5)
		self.vertical_container.setObjectName("verticalLayout")

		# tabs
		self.tabs = QtWidgets.QTabWidget()
		self.tabs.setFont(smallfont)
		# dictionary tab
		self.tab_dictionary = QtWidgets.QWidget()
		self.layout_dictionary = QtWidgets.QVBoxLayout()
		self.tab_dictionary.setLayout(self.layout_dictionary)
		self.tabs.addTab(self.tab_dictionary,"Lexicon")
		# baseline text tab
		self.layout_baseline = QtWidgets.QVBoxLayout()
		self.tab_baseline = QtWidgets.QWidget()
		self.tab_baseline.setLayout(self.layout_baseline)
		# baseline buttons
		self.button_gloss_initial = new_button(self,'gloss_initial')
		self.button_gloss_reset = new_button(self,'gloss_reset')
		spacer_baseline = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		# baseline buttons layout
		self.layout_baseline_buttons = new_qt_hbox(self,'layout_baseline_buttons')
		self.layout_baseline_buttons.addWidget(self.button_gloss_initial)
		self.layout_baseline_buttons.addWidget(self.button_gloss_reset)
		self.layout_baseline_buttons.addItem(spacer_baseline)
		self.layout_baseline.addLayout(self.layout_baseline_buttons)
		# textarea
		self.textarea_baseline = QtWidgets.QPlainTextEdit()
		self.textarea_baseline.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.textarea_baseline.setFont(engfont)
		self.textarea_baseline.setTabChangesFocus(True)
		self.textarea_baseline.setObjectName("textarea_baseline")
		self.textarea_baseline.setFont(QtGui.QFont("Phake Script", int(fontsize*1.5)))
		self.textarea_baseline.setPlainText("kinq xW.")
		self.layout_baseline.addWidget(self.textarea_baseline)
		# glossing tab
		self.layout_glossing = QtWidgets.QVBoxLayout()
		self.tab_glossing = QtWidgets.QWidget()
		self.glossbox = QtWidgets.QGridLayout()
		self.layout_glossing.addLayout(self.glossbox)
		self.tab_glossing.setLayout(self.layout_glossing)
		# self.tabs.addTab(self.tab_glossing,"Glossing")
		self.vertical_container.addWidget(self.tabs)
		# top bar buttons
		self.layout_top_buttons = QtWidgets.QHBoxLayout()
		self.layout_top_buttons.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
		self.layout_top_buttons.setContentsMargins(0, 0, 0, 0)
		self.layout_top_buttons.setObjectName("topbuttonbar")
		# sync button
		self.button_sync = new_button(self,'button_sync')
		self.button_sync.setToolTipDuration(5)
		self.layout_top_buttons.addWidget(self.button_sync)
		# spacer
		spacer_topbuttonbar = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.layout_top_buttons.addItem(spacer_topbuttonbar)

		# language selector
		self.combo_lang = new_qt_combo(self,'lang_choice',2,contents=['phake','muishaung'])
		self.combo_lang.setItemText(0, "Muishaung")
		self.combo_lang.setItemText(1, "Phake")
		self.layout_top_buttons.addWidget(self.combo_lang)

		# clone button
		self.button_clone = new_button(self,'button_clone')
		self.layout_top_buttons.addWidget(self.button_clone)
		# help button
		self.button_help = new_button(self,'button_help')
		self.layout_top_buttons.addWidget(self.button_help)
		# about button
		self.button_about = new_button(self,'button_about')
		self.layout_top_buttons.addWidget(self.button_about)
		# add button bar to main container

		self.layout_dictionary.addLayout(self.layout_top_buttons)

		# hr = horizontal_line()
		# self.layout_dictionary.addWidget(hr)

		self.splitter = QtWidgets.QSplitter(self.centralwidget)
		self.splitter.setMinimumSize(QtCore.QSize(0, 0))
		self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.splitter.setOrientation(QtCore.Qt.Horizontal)
		self.splitter.setOpaqueResize(True)
		self.splitter.setHandleWidth(6)
		self.splitter.setChildrenCollapsible(False)
		self.splitter.setObjectName("splitter")
		self.layoutWidget = QtWidgets.QWidget(self.splitter)
		self.layoutWidget.setObjectName("layoutWidget")
		self.layout_left_margin = QtWidgets.QVBoxLayout(self.layoutWidget)
		self.layout_left_margin.setContentsMargins(0, 0, 0, 0)
		self.layout_left_margin.setObjectName("layout_left_margin")
		# treewidget word list
		self.treeWidget = QtWidgets.QTreeWidget(self.layoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
		self.treeWidget.setSizePolicy(sizePolicy)
		self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.treeWidget.setBaseSize(QtCore.QSize(100, 0))
		self.treeWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
		self.treeWidget.setProperty("showDropIndicator", False)
		self.treeWidget.setAlternatingRowColors(True)
		self.treeWidget.setAutoExpandDelay(1)
		self.treeWidget.setItemsExpandable(False)
		self.treeWidget.setColumnCount(4)
		self.treeWidget.setObjectName("treeWidget")
		self.treeWidget.headerItem().setText(0, "　")
		self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
		self.treeWidget.header().setCascadingSectionResizes(False)
		self.treeWidget.header().setHighlightSections(False)
		self.treeWidget.header().setMinimumSectionSize(10)

		self.layout_filter = new_qt_hbox(self,'layout_filter')
		self.label_filter = new_qt_label(self,"label_filter")
		self.layout_filter.addWidget(self.label_filter)

		self.entry_filter = new_qt_entry(self, 'entry_filter', '','pha')
		self.entry_filter.setFixedWidth(120)
		self.entry_filter.setPlaceholderText('tjfaek')
		self.entry_filter_def = new_qt_entry(self, 'entry_filter_def', '','')
		self.entry_filter_def.setFixedWidth(120)
		self.entry_filter_def.setPlaceholderText('gloss')
		self.combo_filter = new_qt_combo(self,'combo_filter', 4)
		self.combo_filter.setFixedWidth(120)
		self.layout_filter.addWidget(self.entry_filter)
		self.layout_filter.addWidget(self.combo_filter)
		self.layout_filter.addWidget(self.entry_filter_def)
		self.layout_left_margin.addLayout(self.layout_filter)
		self.layout_left_margin.addWidget(self.treeWidget)

		# add entry
		self.layout_add_entry = new_qt_hbox(self,'layout_add_entry')
		self.button_add = new_button(self,'button_add')
		self.layout_add_entry.addWidget(self.button_add)
		spacer_add_entry = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.layout_add_entry.addItem(spacer_add_entry)

		# wordcount
		self.label_word_count = new_qt_label(self,"label_temp")
		self.layout_add_entry.addWidget(self.label_word_count)
		self.label_wordcount_text = new_qt_label(self,"label_wordcount_text")
		self.layout_add_entry.addWidget(self.label_wordcount_text)
		self.layout_left_margin.addLayout(self.layout_add_entry)
		self.layoutWidget = QtWidgets.QWidget(self.splitter)
		self.layoutWidget.setObjectName("layoutWidget1")

		# don't create this one with new_qt_vbox()
		self.info_panel_vertical = QtWidgets.QVBoxLayout(self.layoutWidget)
		self.info_panel_vertical.setContentsMargins(0, 0, 0, 0)
		self.info_panel_vertical.setSpacing(5)
		self.info_panel_vertical.setObjectName("info_panel_vertical")
		# doc id row
		self.label_docid = new_qt_label(self,"label_docid")
		self.layout_docid = new_qt_hbox(self,"layout_docid")
		# spacer_docid = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.entry_docid = new_qt_entry(self, 'entry_docid', '')
		self.layout_docid.addWidget(self.label_docid)
		# self.layout_docid.addItem(spacer_docid)
		self.layout_docid.addWidget(self.entry_docid)
		self.info_panel_vertical.addLayout(self.layout_docid)

		# revision ID (not currently used)
		# self.horizontalLayout = new_qt_hbox(self,"horizontalLayout")
		# self.rev_entry = QtWidgets.QLineEdit(self.layoutWidget)
		# self.rev_entry.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		# self.rev_entry.setObjectName("rev_entry")
		# self.horizontalLayout.addWidget(self.rev_entry)
		# self.info_panel_vertical.addLayout(self.horizontalLayout)

		# headword row
		self.layout_headword = new_qt_hbox(self,"layout_headword")
		self.layout_lexeme = new_qt_vbox(self,"layout_lexeme")
		self.label_lexeme = new_qt_label(self,"label_lexeme")
		self.entry_lexeme = new_qt_entry(self, 'entry_lexeme', 'faek', 'pha')
		add_widget(self.layout_lexeme, [self.label_lexeme, self.entry_lexeme])
		self.layout_unicode = new_qt_vbox(self,"layout_unicode")
		self.label_unicode = new_qt_label(self,"label_unicode")
		self.entry_unicode = new_qt_entry(self, 'entry_unicode', 'ၸါကေ', 'mya')
		add_widget(self.layout_unicode, [self.label_unicode, self.entry_unicode])
		self.layout_temp = new_qt_vbox(self,"layout_temp")
		self.label_temp = new_qt_label(self,"label_temp")
		self.entry_temp = new_qt_entry(self, 'entry_temp', 'ၸါကေ', 'mya')
		add_widget(self.layout_temp, [self.label_temp, self.entry_temp])
		add_layout(self.layout_headword, [self.layout_lexeme, self.layout_unicode, self.layout_temp])
		self.info_panel_vertical.addLayout(self.layout_headword)

		# two-column layout with aligned labels
		self.layout_phon_pos = new_qt_hbox(self,"layout_phon_pos")
		self.layout_phon = new_qt_vbox(self,"layout_phon")
		self.label_phon = new_qt_label(self,"label_phon")
		self.entry_phon = new_qt_entry(self, 'entry_phon', 'phā₄ kē₅')
		add_widget(self.layout_phon, [self.label_phon, self.entry_phon])
		self.layout_pos = new_qt_vbox(self,"layout_pos")
		self.label_pos = new_qt_label(self,"label_pos")
		self.combo_pos = new_qt_combo(self,'combo_pos',16)
		add_widget(self.layout_pos, [self.label_pos, self.combo_pos])
		add_layout(self.layout_phon_pos, [self.layout_phon, self.layout_pos])
		self.info_panel_vertical.addLayout(self.layout_phon_pos)
		# done

		self.label_definition = new_qt_label(self,"label_definition")
		self.definition_textarea = QtWidgets.QPlainTextEdit(self.layoutWidget)
		self.definition_textarea.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.definition_textarea.setFont(engfont)
		self.definition_textarea.setTabChangesFocus(True)
		self.definition_textarea.setObjectName("definition_textarea")
		add_widget(self.info_panel_vertical, [self.label_definition, self.definition_textarea])

		# gloss and taxonomy
		self.layout_gloss_taxonomy = new_qt_hbox(self,"layout_gloss_taxonomy")
		self.layout_gloss = new_qt_vbox(self,"layout_gloss")
		self.label_gloss = new_qt_label(self,"label_gloss")
		self.entry_gloss = new_qt_entry(self, 'entry_gloss', '')
		add_widget(self.layout_gloss, [self.label_gloss, self.entry_gloss])
		self.layout_taxonomy = new_qt_vbox(self,"layout_taxonomy")
		self.label_taxonomy = new_qt_label(self,"label_taxonomy")
		self.entry_taxonomy = new_qt_entry(self, 'entry_taxonomy', '')
		add_widget(self.layout_taxonomy, [self.label_taxonomy, self.entry_taxonomy])
		add_layout(self.layout_gloss_taxonomy, [self.layout_gloss, self.layout_taxonomy])
		self.info_panel_vertical.addLayout(self.layout_gloss_taxonomy)

		# example block
		self.example_layout = new_qt_hbox(self,"example_layout")
		self.label_example = new_qt_label(self,"label_example")
		self.example_layout.addWidget(self.label_example)
		self.example_layout_script = new_qt_hbox(self,"example_layout_script")
		self.label_example_script = new_qt_label(self,"label_example_script")
		self.example_script_entry = new_qt_entry(self, 'example_script_entry', '', 'pha')
		add_widget(self.example_layout_script, [self.label_example_script, self.example_script_entry])
		self.example_layout_phonemic = new_qt_hbox(self,'example_layout_phonemic')
		self.label_example_phonemic = new_qt_label(self,"label_example_phonemic")
		self.example_phonemic_entry = new_qt_entry(self, 'example_english_entry', '')
		add_widget(self.example_layout_phonemic, [self.label_example_phonemic, self.example_phonemic_entry])
		self.example_layout_english = new_qt_hbox(self,'example_layout_english')
		self.label_example_english = new_qt_label(self,"label_example_english")
		self.example_english_entry = new_qt_entry(self, 'example_english_entry', '')
		add_widget(self.example_layout_english, [self.label_example_english, self.example_english_entry])
		add_layout(self.info_panel_vertical, [self.example_layout, self.example_layout_script, self.example_layout_phonemic, self.example_layout_english])

		# self.alt_label = QtWidgets.QLabel(self.layoutWidget)
		# self.alt_label.setFrameShape(QtWidgets.QFrame.NoFrame)
		# self.alt_label.setFrameShadow(QtWidgets.QFrame.Plain)
		# self.alt_label.setObjectName("alt_label")
		# self.info_panel_vertical.addWidget(self.alt_label)
		# self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
		# self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
		# self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		# self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
		# self.horizontalLayout_10.setContentsMargins(0, 0, -1, -1)
		# self.horizontalLayout_10.setObjectName("horizontalLayout_10")
		#self.alt_entry = QtWidgets.QLineEdit(self.layoutWidget)
		#self.alt_entry.setObjectName("alt_entry")
		#self.horizontalLayout_10.addWidget(self.alt_entry)
		# self.horizontalLayout_5.addLayout(self.horizontalLayout_10)
		# self.horizontalLayout_1treeview.setAlternatingRowColors(True)1 = QtWidgets.QHBoxLayout()
		# self.horizontalLayout_11.setObjectName("horizontalLayout_11")
		# spacer_add_entry0 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		# self.horizontalLayout_11.addItem(spacer_add_entry0)
		# self.horizontalLayout_5.addLayout(self.horizontalLayout_11)
		# self.info_panel_vertical.addLayout(self.horizontalLayout_5)

		# notes
		self.label_notes = new_qt_label(self,"label_notes")
		self.notes_textarea = QtWidgets.QPlainTextEdit(self.layoutWidget)
		self.notes_textarea.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.notes_textarea.setTabChangesFocus(True)
		self.notes_textarea.setObjectName("notes_textarea")
		add_widget(self.info_panel_vertical, [self.label_notes, self.notes_textarea])

		# media
		self.layout_media = new_qt_hbox(self,'layout_media')
		self.layout_sound = new_qt_vbox(self,'layout_sound')
		self.label_sound = new_qt_label(self,"label_sound")
		self.sound_entry = new_qt_entry(self, 'sound_entry', '')
		add_widget(self.layout_sound, [self.label_sound, self.sound_entry])
		self.layout_photo = new_qt_vbox(self,'layout_photo')
		self.label_photo = new_qt_label(self,"label_photo","Photo")
		self.photo_entry = new_qt_entry(self, 'photo_entry', '')
		add_widget(self.layout_photo, [self.label_photo, self.photo_entry])
		add_layout(self.layout_media, [self.layout_sound, self.layout_photo])
		self.info_panel_vertical.addLayout(self.layout_media)

		# bottom buttons
		self.layout_bottom_buttons = new_qt_hbox(self,'layout_bottom_buttons')
		self.button_delete = new_button(self,'button_delete')
		spacer_bottom_buttons = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.button_save = new_button(self,"button_save")
		self.button_save.setObjectName("button_save")
		self.layout_bottom_buttons.addWidget(self.button_delete)
		self.layout_bottom_buttons.addItem(spacer_bottom_buttons)
		self.layout_bottom_buttons.addWidget(self.button_save)

		self.info_panel_vertical.addLayout(self.layout_bottom_buttons)

		self.layout_dictionary.addWidget(self.splitter)
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Ichō dictionary tool"))
		self.button_sync.setToolTip(_translate("MainWindow", "Send all of your changes to the database"))
		self.button_sync.setText(_translate("MainWindow", "Save to Database"))
		self.button_clone.setText(_translate("MainWindow", "Clone"))
		self.button_gloss_initial.setText(_translate("MainWindow", "Gloss"))
		self.button_gloss_reset.setText(_translate("MainWindow", "Reset"))
		self.button_help.setText(_translate("MainWindow", "Help"))
		self.button_about.setText(_translate("MainWindow", "About"))
		self.treeWidget.setSortingEnabled(False)
		self.treeWidget.headerItem().setText(1, _translate("MainWindow", "lexeme"))
		self.treeWidget.headerItem().setFont(1, engfont)
		self.treeWidget.headerItem().setText(2, _translate("MainWindow", "phonemic"))
		self.treeWidget.headerItem().setFont(2, engfont)
		self.treeWidget.headerItem().setText(3, _translate("MainWindow", "gloss"))
		self.treeWidget.headerItem().setFont(3, engfont)
		self.treeWidget.headerItem().setText(4, _translate("MainWindow", "unicode"))
		self.treeWidget.headerItem().setFont(4, engfont)
		self.button_add.setText(_translate("MainWindow", "Add new word"))
		self.label_word_count.setText(_translate("MainWindow", "0"))
		self.label_wordcount_text.setText(_translate("MainWindow", "words"))
		self.label_docid.setText(_translate("MainWindow", "<b>ID</b> for database"))
		# self.label_revisionid.setText(_translate("MainWindow", "")) # rev label
		self.label_lexeme.setText(_translate("MainWindow", "<b>Lexeme</b>"))
		self.label_unicode.setText(_translate("MainWindow", "<b>Unicode</b> (Myanmar letters)"))
		self.label_temp.setText(_translate("MainWindow", "auto-generated Unicode"))
		#self.nominal_entry.setPlaceholderText(_translate("MainWindow", "vsaiz"))
		#self.nominal_entry.setEnabled(False)
		self.entry_unicode.setEnabled(False)
		self.label_phon.setText(_translate("MainWindow", "<b>Phonemic</b>"))
		self.label_pos.setText(_translate("MainWindow", "<b>Part of speech</b>"))
		self.combo_pos.setItemText(0, _translate("MainWindow", "..."))
		self.combo_pos.setItemText(1, _translate("MainWindow", "adjective"))
		self.combo_pos.setItemText(2, _translate("MainWindow", "adposition"))
		self.combo_pos.setItemText(3, _translate("MainWindow", "adverb"))
		self.combo_pos.setItemText(4, _translate("MainWindow", "article"))
		self.combo_pos.setItemText(5, _translate("MainWindow", "classifier"))
		self.combo_pos.setItemText(6, _translate("MainWindow", "clitic"))
		self.combo_pos.setItemText(7, _translate("MainWindow", "conjunction"))
		self.combo_pos.setItemText(8, _translate("MainWindow", "contraction"))
		self.combo_pos.setItemText(9, _translate("MainWindow", "determiner"))
		self.combo_pos.setItemText(9, _translate("MainWindow", "exclamation"))
		self.combo_pos.setItemText(10, _translate("MainWindow", "interogative"))
		self.combo_pos.setItemText(11, _translate("MainWindow", "noun"))
		self.combo_pos.setItemText(12, _translate("MainWindow", "onom."))
		self.combo_pos.setItemText(13, _translate("MainWindow", "particle"))
		self.combo_pos.setItemText(14, _translate("MainWindow", "pronoun"))
		self.combo_pos.setItemText(15, _translate("MainWindow", "verb"))

		self.combo_filter.setItemText(0, _translate("MainWindow", "match anywhere"))
		self.combo_filter.setItemText(1, _translate("MainWindow", "exact match"))
		self.combo_filter.setItemText(2, _translate("MainWindow", "match at start"))
		self.combo_filter.setItemText(3, _translate("MainWindow", "match at end"))

		self.entry_filter_def.setToolTip(_translate("MainWindow", "Only applies to the English gloss"))
		self.entry_filter_def.setToolTip(_translate("MainWindow", "Filter by Tai Phake"))

		self.label_definition.setText(_translate("MainWindow", "<b>Definition</b>"))
		self.label_gloss.setText(_translate("MainWindow", "<b>Gloss</b> (a one-word definition)"))
		self.label_taxonomy.setText(_translate("MainWindow", "<b>Scientific name</b> in Latin"))
		#self.alt_label.setText(_translate("MainWindow", "<b>Song language</b>"))
		self.label_notes.setText(_translate("MainWindow", "<b>Notes</b>"))
		self.label_sound.setText(_translate("MainWindow", "<b>Sound</b> (file name)"))
		self.label_photo.setText(_translate("MainWindow", "<b>Photo</b> (file name)"))

		self.label_filter.setText(_translate("MainWindow", "<b>Search</b>"))
		# example labels
		self.label_example.setText(_translate("MainWindow", "<b>Example</b>"))
		self.label_example_script.setText(_translate("MainWindow", "Phake"))
		self.label_example_phonemic.setText(_translate("MainWindow", "Banchob"))
		self.label_example_english.setText(_translate("MainWindow", "English"))

		self.button_delete.setText(_translate("MainWindow", "Delete this word"))
		self.button_save.setText(_translate("MainWindow", "Save changes"))

import icons_rc
