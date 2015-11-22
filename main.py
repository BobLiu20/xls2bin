import sys
import os
#*********For QT ui
from PyQt4 import QtCore , QtGui
from qtui import Ui_MainWindow
#*********For Action interface
from XlsAndBin import XlsAndBin

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()    #note: instance, not the class
        self.ui.setupUi(self)
        self.XlsAndBin_Ins = XlsAndBin()

    def xls2bin(self, parent=None):
        self.ui.x2b_tips.setText("Start!")
        try:
            self.XlsAndBin_Ins.XlsAndBin_xls2bin(self.xlsdirectory,self.strfolder)
            self.ui.x2b_tips.setText("Finshed!")
        except:
            self.ui.x2b_tips.setText("what's wrong? call @Bob as soon.")

    def selfolder(self, parent=None):
        self.strfolder = QtGui.QFileDialog.getExistingDirectory(parent,
                    _fromUtf8("Please select your directory.(eg: str_default)"),
                    _fromUtf8("open file dialog"));
        self.ui.x2b_txt_file.setText(self.strfolder)
        if os.path.exists(self.strfolder) == False:
            self.ui.x2b_tips.setText("The str directory is wrong!")

    def selfile(self, parent=None):
        self.xlsdirectory = QtGui.QFileDialog.getOpenFileName(parent,
            _fromUtf8("excel file select"), "" , _fromUtf8("*.xls")
            )
        self.ui.x2b_txt_xls.setText(self.xlsdirectory)
        if os.path.exists(self.xlsdirectory) == False:
            self.ui.x2b_tips.setText("The excel file is wrong!")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
