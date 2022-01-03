import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QToolTip
from PyQt5.QtGui import QIcon


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('First Application')
    win.setGeometry(200,200,700,700)
    win.setWindowIcon(QIcon('icon.jpg'))
    win.setToolTip('my tooltip')

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Adınız: ')
    lbl_name.move(50,30)


    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText('Soyadınız: ')
    lbl_surname.move(50,70)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(100,30)

    











    win.show()
    sys.exit(app.exec_())


window()

