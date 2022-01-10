
from PyQt5 import QtWidgets
import sys
from radiobuttonform import Ui_MainWindow

from PyQt5.QtCore import Qt



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        self.ui.radioTurkiye.setChecked(True)



        self.ui.radioTurkiye.toggled.connect(self.onClicked)
        self.ui.radioAlmanya.toggled.connect(self.onClicked)
        self.ui.radioIspanya.toggled.connect(self.onClicked)
        self.ui.radioRusya.toggled.connect(self.onClicked)



        self.ui.lise.toggled.connect(self,onClickedEgitim)
        self.ui.ilkokul.toggled.connect(self,onClickedEgitim)
        self.ui.ilkokul.toggled.connect(self,onClickedEgitim)
        self.ui.ilkokul.toggled.connect(self,onClickedEgitim)






    def onClickedEgitim(self):

        rb = self.sender()
        if rb.isChecked():
            print('Seçilen radio :  ' + rb.text())




    def onClicked(self):

        rb = self.sender()
        if rb.isChecked():
                print('Seçilen radio :  ' + rb.text())


    # def getSelectedUlke(self):
    #     items = self.ui.gridLayout.

    
   










app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())