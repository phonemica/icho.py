# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(400, 174)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
		Dialog.setSizePolicy(sizePolicy)
		Dialog.setMaximumSize(QtCore.QSize(450, 250))
		self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
		self.verticalLayout.setObjectName("verticalLayout")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem)
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_4.addItem(spacerItem1)
		self.close_button = QtWidgets.QPushButton(Dialog)
		self.close_button.setObjectName("close_button")
		self.horizontalLayout_4.addWidget(self.close_button)
		self.verticalLayout_2.addLayout(self.horizontalLayout_4)
		self.verticalLayout.addLayout(self.verticalLayout_2)

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Settings"))
		self.close_button.setText(_translate("Dialog", "Ok"))
