# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Dec  5 23:38:01 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SupernoveString(object):
    def setupUi(self, SupernoveString):
        SupernoveString.setObjectName(_fromUtf8("SupernoveString"))
        SupernoveString.resize(499, 328)
        self.centralWidget = QtGui.QWidget(SupernoveString)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.x2b_btn_start = QtGui.QPushButton(self.centralWidget)
        self.x2b_btn_start.setGeometry(QtCore.QRect(390, 100, 99, 27))
        self.x2b_btn_start.setObjectName(_fromUtf8("x2b_btn_start"))
        self.x2b_txt_file = QtGui.QTextEdit(self.centralWidget)
        self.x2b_txt_file.setGeometry(QtCore.QRect(10, 70, 371, 31))
        self.x2b_txt_file.setObjectName(_fromUtf8("x2b_txt_file"))
        self.x2b_btn_select = QtGui.QPushButton(self.centralWidget)
        self.x2b_btn_select.setGeometry(QtCore.QRect(390, 70, 99, 27))
        self.x2b_btn_select.setObjectName(_fromUtf8("x2b_btn_select"))
        self.x2b_txt_xls = QtGui.QTextEdit(self.centralWidget)
        self.x2b_txt_xls.setGeometry(QtCore.QRect(10, 30, 371, 31))
        self.x2b_txt_xls.setObjectName(_fromUtf8("x2b_txt_xls"))
        self.x2b_btn_xls = QtGui.QPushButton(self.centralWidget)
        self.x2b_btn_xls.setGeometry(QtCore.QRect(390, 30, 99, 27))
        self.x2b_btn_xls.setObjectName(_fromUtf8("x2b_btn_xls"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 291, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.x2b_tips = QtGui.QLabel(self.centralWidget)
        self.x2b_tips.setGeometry(QtCore.QRect(10, 240, 351, 17))
        self.x2b_tips.setObjectName(_fromUtf8("x2b_tips"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 281, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.x2b_txt_file_2 = QtGui.QTextEdit(self.centralWidget)
        self.x2b_txt_file_2.setGeometry(QtCore.QRect(10, 170, 371, 31))
        self.x2b_txt_file_2.setObjectName(_fromUtf8("x2b_txt_file_2"))
        self.x2b_btn_select_2 = QtGui.QPushButton(self.centralWidget)
        self.x2b_btn_select_2.setGeometry(QtCore.QRect(390, 170, 99, 27))
        self.x2b_btn_select_2.setObjectName(_fromUtf8("x2b_btn_select_2"))
        self.x2b_btn_start_2 = QtGui.QPushButton(self.centralWidget)
        self.x2b_btn_start_2.setGeometry(QtCore.QRect(390, 200, 99, 27))
        self.x2b_btn_start_2.setObjectName(_fromUtf8("x2b_btn_start_2"))
        SupernoveString.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(SupernoveString)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 499, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        SupernoveString.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(SupernoveString)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        SupernoveString.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(SupernoveString)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        SupernoveString.setStatusBar(self.statusBar)

        self.retranslateUi(SupernoveString)
        QtCore.QObject.connect(self.x2b_btn_start, QtCore.SIGNAL(_fromUtf8("clicked()")), SupernoveString.xls2bin)
        QtCore.QObject.connect(self.x2b_btn_select, QtCore.SIGNAL(_fromUtf8("clicked()")), SupernoveString.selfolder)
        QtCore.QObject.connect(self.x2b_btn_xls, QtCore.SIGNAL(_fromUtf8("clicked()")), SupernoveString.selfile)
        QtCore.QObject.connect(self.x2b_btn_select_2, QtCore.SIGNAL(_fromUtf8("clicked()")), SupernoveString.selfolder2)
        QtCore.QObject.connect(self.x2b_btn_start_2, QtCore.SIGNAL(_fromUtf8("clicked()")), SupernoveString.bin2xls)
        QtCore.QMetaObject.connectSlotsByName(SupernoveString)

    def retranslateUi(self, SupernoveString):
        SupernoveString.setWindowTitle(_translate("SupernoveString", "SupernovaStr", None))
        self.x2b_btn_start.setText(_translate("SupernoveString", "开始", None))
        self.x2b_btn_select.setText(_translate("SupernoveString", "str目录选择", None))
        self.x2b_btn_xls.setText(_translate("SupernoveString", "excel选择", None))
        self.label.setText(_translate("SupernoveString", "1. 将excel转换为str rc bin", None))
        self.x2b_tips.setText(_translate("SupernoveString", "Hello World! --CVTE Supernova team", None))
        self.label_2.setText(_translate("SupernoveString", "2. 将str rc bin转换为excel", None))
        self.x2b_btn_select_2.setText(_translate("SupernoveString", "str目录选择", None))
        self.x2b_btn_start_2.setText(_translate("SupernoveString", "开始", None))

