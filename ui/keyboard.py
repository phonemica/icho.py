# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keyboard.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 234)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(401, 234))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mv = QtWidgets.QPushButton(Dialog)
        self.mv.setMaximumSize(QtCore.QSize(40, 16777215))
        self.mv.setObjectName("mv")
        self.horizontalLayout.addWidget(self.mv)
        self.ny = QtWidgets.QPushButton(Dialog)
        self.ny.setMaximumSize(QtCore.QSize(40, 16777215))
        self.ny.setObjectName("ny")
        self.horizontalLayout.addWidget(self.ny)
        self.nr = QtWidgets.QPushButton(Dialog)
        self.nr.setMaximumSize(QtCore.QSize(40, 16777215))
        self.nr.setObjectName("nr")
        self.horizontalLayout.addWidget(self.nr)
        self.ng = QtWidgets.QPushButton(Dialog)
        self.ng.setMaximumSize(QtCore.QSize(40, 16777215))
        self.ng.setObjectName("ng")
        self.horizontalLayout.addWidget(self.ng)
        self.nn = QtWidgets.QPushButton(Dialog)
        self.nn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.nn.setObjectName("nn")
        self.horizontalLayout.addWidget(self.nn)
        self.qq = QtWidgets.QPushButton(Dialog)
        self.qq.setMaximumSize(QtCore.QSize(40, 16777215))
        self.qq.setObjectName("qq")
        self.horizontalLayout.addWidget(self.qq)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sh = QtWidgets.QPushButton(Dialog)
        self.sh.setMaximumSize(QtCore.QSize(40, 16777215))
        self.sh.setObjectName("sh")
        self.horizontalLayout_3.addWidget(self.sh)
        self.zh = QtWidgets.QPushButton(Dialog)
        self.zh.setMaximumSize(QtCore.QSize(40, 16777215))
        self.zh.setObjectName("zh")
        self.horizontalLayout_3.addWidget(self.zh)
        self.shr = QtWidgets.QPushButton(Dialog)
        self.shr.setMaximumSize(QtCore.QSize(40, 16777215))
        self.shr.setObjectName("shr")
        self.horizontalLayout_3.addWidget(self.shr)
        self.zhr = QtWidgets.QPushButton(Dialog)
        self.zhr.setMaximumSize(QtCore.QSize(40, 16777215))
        self.zhr.setObjectName("zhr")
        self.horizontalLayout_3.addWidget(self.zhr)
        self.xi = QtWidgets.QPushButton(Dialog)
        self.xi.setMaximumSize(QtCore.QSize(40, 16777215))
        self.xi.setObjectName("xi")
        self.horizontalLayout_3.addWidget(self.xi)
        self.zi = QtWidgets.QPushButton(Dialog)
        self.zi.setMaximumSize(QtCore.QSize(40, 16777215))
        self.zi.setObjectName("zi")
        self.horizontalLayout_3.addWidget(self.zi)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.phi = QtWidgets.QPushButton(Dialog)
        self.phi.setMaximumSize(QtCore.QSize(40, 16777215))
        self.phi.setObjectName("phi")
        self.horizontalLayout_5.addWidget(self.phi)
        self.beta = QtWidgets.QPushButton(Dialog)
        self.beta.setMaximumSize(QtCore.QSize(40, 16777215))
        self.beta.setObjectName("beta")
        self.horizontalLayout_5.addWidget(self.beta)
        self.theta = QtWidgets.QPushButton(Dialog)
        self.theta.setMaximumSize(QtCore.QSize(40, 16777215))
        self.theta.setObjectName("theta")
        self.horizontalLayout_5.addWidget(self.theta)
        self.dheta = QtWidgets.QPushButton(Dialog)
        self.dheta.setMaximumSize(QtCore.QSize(40, 16777215))
        self.dheta.setObjectName("dheta")
        self.horizontalLayout_5.addWidget(self.dheta)
        self.cha = QtWidgets.QPushButton(Dialog)
        self.cha.setMaximumSize(QtCore.QSize(40, 16777215))
        self.cha.setObjectName("cha")
        self.horizontalLayout_5.addWidget(self.cha)
        self.zha = QtWidgets.QPushButton(Dialog)
        self.zha.setMaximumSize(QtCore.QSize(40, 16777215))
        self.zha.setObjectName("zha")
        self.horizontalLayout_5.addWidget(self.zha)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.vv = QtWidgets.QPushButton(Dialog)
        self.vv.setMaximumSize(QtCore.QSize(40, 16777215))
        self.vv.setObjectName("vv")
        self.horizontalLayout_7.addWidget(self.vv)
        self.rr = QtWidgets.QPushButton(Dialog)
        self.rr.setMaximumSize(QtCore.QSize(40, 16777215))
        self.rr.setObjectName("rr")
        self.horizontalLayout_7.addWidget(self.rr)
        self.gh = QtWidgets.QPushButton(Dialog)
        self.gh.setMaximumSize(QtCore.QSize(40, 16777215))
        self.gh.setObjectName("gh")
        self.horizontalLayout_7.addWidget(self.gh)
        self.xh = QtWidgets.QPushButton(Dialog)
        self.xh.setMaximumSize(QtCore.QSize(40, 16777215))
        self.xh.setObjectName("xh")
        self.horizontalLayout_7.addWidget(self.xh)
        self.ayin = QtWidgets.QPushButton(Dialog)
        self.ayin.setMaximumSize(QtCore.QSize(40, 16777215))
        self.ayin.setObjectName("ayin")
        self.horizontalLayout_7.addWidget(self.ayin)
        self.hh = QtWidgets.QPushButton(Dialog)
        self.hh.setMaximumSize(QtCore.QSize(40, 16777215))
        self.hh.setObjectName("hh")
        self.horizontalLayout_7.addWidget(self.hh)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.key_custom1 = QtWidgets.QPushButton(Dialog)
        self.key_custom1.setMaximumSize(QtCore.QSize(40, 16777215))
        self.key_custom1.setObjectName("key_custom1")
        self.horizontalLayout_13.addWidget(self.key_custom1)
        self.key_custom2 = QtWidgets.QPushButton(Dialog)
        self.key_custom2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.key_custom2.setObjectName("key_custom2")
        self.horizontalLayout_13.addWidget(self.key_custom2)
        self.key_custom3 = QtWidgets.QPushButton(Dialog)
        self.key_custom3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.key_custom3.setObjectName("key_custom3")
        self.horizontalLayout_13.addWidget(self.key_custom3)
        self.key_custom4 = QtWidgets.QPushButton(Dialog)
        self.key_custom4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.key_custom4.setObjectName("key_custom4")
        self.horizontalLayout_13.addWidget(self.key_custom4)
        self.key_custom5 = QtWidgets.QPushButton(Dialog)
        self.key_custom5.setMaximumSize(QtCore.QSize(40, 16777215))
        self.key_custom5.setObjectName("key_custom5")
        self.horizontalLayout_13.addWidget(self.key_custom5)
        self.key_custom6 = QtWidgets.QPushButton(Dialog)
        self.key_custom6.setMaximumSize(QtCore.QSize(40, 16777215))
        self.key_custom6.setObjectName("key_custom6")
        self.horizontalLayout_13.addWidget(self.key_custom6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.bari = QtWidgets.QPushButton(Dialog)
        self.bari.setMaximumSize(QtCore.QSize(40, 16777215))
        self.bari.setObjectName("bari")
        self.horizontalLayout_11.addWidget(self.bari)
        self.baru = QtWidgets.QPushButton(Dialog)
        self.baru.setMaximumSize(QtCore.QSize(40, 16777215))
        self.baru.setObjectName("baru")
        self.horizontalLayout_11.addWidget(self.baru)
        self.uu = QtWidgets.QPushButton(Dialog)
        self.uu.setMaximumSize(QtCore.QSize(40, 16777215))
        self.uu.setObjectName("uu")
        self.horizontalLayout_11.addWidget(self.uu)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.ih = QtWidgets.QPushButton(Dialog)
        self.ih.setMaximumSize(QtCore.QSize(40, 16777215))
        self.ih.setObjectName("ih")
        self.horizontalLayout_10.addWidget(self.ih)
        self.yh = QtWidgets.QPushButton(Dialog)
        self.yh.setMaximumSize(QtCore.QSize(40, 16777215))
        self.yh.setObjectName("yh")
        self.horizontalLayout_10.addWidget(self.yh)
        self.oo = QtWidgets.QPushButton(Dialog)
        self.oo.setMaximumSize(QtCore.QSize(40, 16777215))
        self.oo.setObjectName("oo")
        self.horizontalLayout_10.addWidget(self.oo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.oe = QtWidgets.QPushButton(Dialog)
        self.oe.setMaximumSize(QtCore.QSize(40, 16777215))
        self.oe.setObjectName("oe")
        self.horizontalLayout_9.addWidget(self.oe)
        self.schwa = QtWidgets.QPushButton(Dialog)
        self.schwa.setMaximumSize(QtCore.QSize(40, 16777215))
        self.schwa.setObjectName("schwa")
        self.horizontalLayout_9.addWidget(self.schwa)
        self.ui = QtWidgets.QPushButton(Dialog)
        self.ui.setMaximumSize(QtCore.QSize(40, 16777215))
        self.ui.setObjectName("ui")
        self.horizontalLayout_9.addWidget(self.ui)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.eh = QtWidgets.QPushButton(Dialog)
        self.eh.setMaximumSize(QtCore.QSize(40, 16777215))
        self.eh.setObjectName("eh")
        self.horizontalLayout_8.addWidget(self.eh)
        self.vv_2 = QtWidgets.QPushButton(Dialog)
        self.vv_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.vv_2.setObjectName("vv_2")
        self.horizontalLayout_8.addWidget(self.vv_2)
        self.aw = QtWidgets.QPushButton(Dialog)
        self.aw.setMaximumSize(QtCore.QSize(40, 16777215))
        self.aw.setObjectName("aw")
        self.horizontalLayout_8.addWidget(self.aw)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.ae = QtWidgets.QPushButton(Dialog)
        self.ae.setMaximumSize(QtCore.QSize(40, 16777215))
        self.ae.setObjectName("ae")
        self.horizontalLayout_12.addWidget(self.ae)
        self.turna = QtWidgets.QPushButton(Dialog)
        self.turna.setMaximumSize(QtCore.QSize(40, 16777215))
        self.turna.setObjectName("turna")
        self.horizontalLayout_12.addWidget(self.turna)
        self.backa = QtWidgets.QPushButton(Dialog)
        self.backa.setMaximumSize(QtCore.QSize(40, 16777215))
        self.backa.setObjectName("backa")
        self.horizontalLayout_12.addWidget(self.backa)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ipa_entry = QtWidgets.QLineEdit(Dialog)
        self.ipa_entry.setObjectName("ipa_entry")
        self.horizontalLayout_4.addWidget(self.ipa_entry)
        self.single_entry = QtWidgets.QLineEdit(Dialog)
        self.single_entry.setMaximumSize(QtCore.QSize(40, 16777215))
        self.single_entry.setObjectName("single_entry")
        self.horizontalLayout_4.addWidget(self.single_entry)
        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setMinimumSize(QtCore.QSize(60, 0))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_4.addWidget(self.close_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        self.ae.clicked.connect(self.ipa_entry.update)
        self.aw.clicked.connect(self.ipa_entry.update)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "IPA Input"))
        self.mv.setText(_translate("Dialog", "ɱ"))
        self.ny.setText(_translate("Dialog", "ɳ"))
        self.nr.setText(_translate("Dialog", "ɲ"))
        self.ng.setText(_translate("Dialog", "ŋ"))
        self.nn.setText(_translate("Dialog", "ɴ"))
        self.qq.setText(_translate("Dialog", "ʔ"))
        self.sh.setText(_translate("Dialog", "ʃ"))
        self.zh.setText(_translate("Dialog", "ʒ"))
        self.shr.setText(_translate("Dialog", "ʂ"))
        self.zhr.setText(_translate("Dialog", "ʐ"))
        self.xi.setText(_translate("Dialog", "ɕ"))
        self.zi.setText(_translate("Dialog", "ʑ"))
        self.phi.setText(_translate("Dialog", "ɸ"))
        self.beta.setText(_translate("Dialog", "β"))
        self.theta.setText(_translate("Dialog", "θ"))
        self.dheta.setText(_translate("Dialog", "ð"))
        self.cha.setText(_translate("Dialog", "ç"))
        self.zha.setText(_translate("Dialog", "ʝ"))
        self.vv.setText(_translate("Dialog", "ʋ"))
        self.rr.setText(_translate("Dialog", "ɹ"))
        self.gh.setText(_translate("Dialog", "ɣ"))
        self.xh.setText(_translate("Dialog", "χ"))
        self.ayin.setText(_translate("Dialog", "ʕ"))
        self.hh.setText(_translate("Dialog", "ɦ"))
        self.key_custom1.setText(_translate("Dialog", " "))
        self.key_custom2.setText(_translate("Dialog", " "))
        self.key_custom3.setText(_translate("Dialog", " "))
        self.key_custom4.setText(_translate("Dialog", " "))
        self.key_custom5.setText(_translate("Dialog", " "))
        self.key_custom6.setText(_translate("Dialog", " "))
        self.bari.setText(_translate("Dialog", "ɨ"))
        self.baru.setText(_translate("Dialog", "ʉ"))
        self.uu.setText(_translate("Dialog", "ɯ"))
        self.ih.setText(_translate("Dialog", "ɪ"))
        self.yh.setText(_translate("Dialog", "ʏ"))
        self.oo.setText(_translate("Dialog", "ʊ"))
        self.oe.setText(_translate("Dialog", "ø"))
        self.schwa.setText(_translate("Dialog", "ə"))
        self.ui.setText(_translate("Dialog", "ɤ"))
        self.eh.setText(_translate("Dialog", "ɛ"))
        self.vv_2.setText(_translate("Dialog", "ʌ"))
        self.aw.setText(_translate("Dialog", "ɔ"))
        self.ae.setText(_translate("Dialog", "æ"))
        self.turna.setText(_translate("Dialog", "ɐ"))
        self.backa.setText(_translate("Dialog", "ɑ"))
        self.close_button.setText(_translate("Dialog", "Ok"))

