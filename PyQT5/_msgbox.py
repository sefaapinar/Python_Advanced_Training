from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from _msgboxform import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,sef).__init__()

        self.ui = Ui.MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(self.showDialog)
    
    def showDialog(self):
        msg = QMessageBox()

        msg.setWindowTitle('Close Application')
        msg.setText('Are you sure ?')
        msg.setIcon(QMessageBox.warning)
        msg.setStandardButtons(QMessageBox.ok | QMessageBox.Cancel) 

        
        


        x = msg.exec_()

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

