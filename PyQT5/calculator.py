import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow



class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,600,600)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayı Giriniz: ')
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,35)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('Sayı Giriniz: ')
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,35)


        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('Topla')
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.toplama)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText('Çıkar')
        self.btn_cikar.move(150,170)
        self.btn_topla.clicked.connect(self.cikar)

        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText('Çarp')
        self.btn_carp.move(150,210)
        self.btn_topla.clicked.connect(self.carp)
        

        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText('Böl')
        self.btn_bol.move(150,250)
        self.btn_topla.clicked.connect(self.bol)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('Ortalama')
        self.btn_topla.move(150,290)
        self.btn_topla.clicked.connect(self.ortalama)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText('SONUÇ:  ')
        self.lbl_sonuc.move(150,350)

    def toplama(self):
        result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        self.lbl_sonuc.setText('Sonuç :'+ str(result))

    def cikar(self):
        result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        self.lbl_sonuc.setText('Sonuç :'+ str(result))

    def carp(self):
        result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        self.lbl_sonuc.setText('Sonuç :'+ str(result))

    def bol(self):
        result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        self.lbl_sonuc.setText('Sonuç :'+ str(result))

    def ortalama(self):
        result = (int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())) /2
        self.lbl_sonuc.setText('Sonuç :'+ str(result))


    # def hesaplama(self):
    #     sender = self.sender()
    #     result = 0
    #     if sender == 'Toplama'
    #         result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
    #     else:



        
        
        
        


def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec())


app()



