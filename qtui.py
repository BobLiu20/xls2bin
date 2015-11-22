# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Nov 22 23:20:02 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(499, 328)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.x2b_btn_start = QtGui.QPushButton(self.centralWidget)
        self.x2b_btn_start.setGeometry(QtCore.QRect(390, 110, 99, 27))
        self.x2b_btn_start.setObjectName(_fromUtf8("x2b_btn_start"))
        self.x2b_txt_file = QtGui.QTextEdit(self.centralWidget)
        self.x2b_txt_file.setGeometry(QtCore.QRect(10, 30, 371, 31))
        self.x2b_txt_file.setObjectName(_fromUtf8("x2b_txt_file"))
        self.x2b_btn_select = QtGui.QPushButton(self.centralWidget)
        self.x2b_btn_select.setGeometry(QtCore.QRect(390, 30, 99, 27))
        self.x2b_btn_select.setObjectName(_fromUtf8("x2b_btn_select"))
        self.x2b_txt_xls = QtGui.QTextEdit(self.centralWidget)
        self.x2b_txt_xls.setGeometry(QtCore.QRect(10, 70, 371, 31))
        self.x2b_txt_xls.setObjectName(_fromUtf8("x2b_txt_xls"))
        self.x2b_btn_xls = QtGui.QPushButton(self.centralWidget)
        self.x2b_btn_xls.setGeometry(QtCore.QRect(390, 70, 99, 27))
        self.x2b_btn_xls.setObjectName(_fromUtf8("x2b_btn_xls"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 291, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.x2b_tips = QtGui.QLabel(self.centralWidget)
        self.x2b_tips.setGeometry(QtCore.QRect(20, 110, 351, 17))
        self.x2b_tips.setText(_fromUtf8(""))
        self.x2b_tips.setObjectName(_fromUtf8("x2b_tips"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 499, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.x2b_btn_start, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.xls2bin)
        QtCore.QObject.connect(self.x2b_btn_select, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.selfolder)
        QtCore.QObject.connect(self.x2b_btn_xls, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.selfile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.x2b_btn_start.setText(_translate("MainWindow", "开始", None))
        self.x2b_btn_select.setText(_translate("MainWindow", "str目录选择", None))
        self.x2b_btn_xls.setText(_translate("MainWindow", "excel选择", None))
        self.label.setText(_translate("MainWindow", "1. 将Str的bin文件转换为excel", None))

