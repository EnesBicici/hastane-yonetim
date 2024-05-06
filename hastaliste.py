from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from hastaliste_ui import Ui_Form
from PyQt5 import QtCore
from veritabani import Veritabani

class HastaListeSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.hastalisteform = Ui_Form()
        self.hastalisteform.setupUi(self)

    def goster(self):
        tablo = self.hastalisteform.hastaTable
        Veritabani.query('SELECT TC, Ad, Soyad, Telefon FROM hastalar')
        hastalar = Veritabani.fetchall()
        tablo.setRowCount(0)
        self.show()
        if hastalar is None:
            return
        tablo.setRowCount(len(hastalar))
        satir = 0
        tablo.setColumnWidth(0, 80)
        tablo.setColumnWidth(1, 140)
        tablo.setColumnWidth(2, 140)
        tablo.setColumnWidth(3, 80)


        for hasta in hastalar:
            tc = QTableWidgetItem(hasta[0])
            ad = QTableWidgetItem(hasta[1])
            soyad = QTableWidgetItem(hasta[2])
            telefon = QTableWidgetItem(hasta[3])
            #Hepsinin yazısını ortala
            tc.setTextAlignment(QtCore.Qt.AlignCenter)
            ad.setTextAlignment(QtCore.Qt.AlignCenter)
            soyad.setTextAlignment(QtCore.Qt.AlignCenter)
            telefon.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, 0, tc)
            tablo.setItem(satir, 1, ad)
            tablo.setItem(satir, 2, soyad)
            tablo.setItem(satir, 3, telefon)

        #tablo.resizeColumnsToContents()