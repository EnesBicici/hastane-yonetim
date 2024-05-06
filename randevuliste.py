from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from randevuTablo_ui import Ui_Form
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from veritabani import Veritabani
from datetime import datetime
from hastane import *

class RandevuListeSayfa(QWidget):
    randevu_iptal_sinyal = pyqtSignal(int)
    def __init__(self) -> None:
        super().__init__()
        self.randevulisteform = Ui_Form()
        self.randevulisteform.setupUi(self)
        self.randevulisteform.iptalButon.clicked.connect(self.randevuiptal)

    def goster(self):
        tablo = self.randevulisteform.randevuTablo

        Veritabani.query('SELECT hastaid, doktorid, tarih FROM randevular')
        randevular = Veritabani.fetchall()
        tablo.setRowCount(0)
        self.show()
        if randevular is None:
            return
        
        tablo.setRowCount(len(randevular))
        satir = 0
        tablo.setColumnWidth(0, 140)
        tablo.setColumnWidth(1, 100)
        tablo.setColumnWidth(2, 100)
        tablo.setColumnWidth(3, 100)
        tablo.setColumnWidth(4, 80)
        tablo.setColumnWidth(5, 60)

        for hastaid, doktorid, tarih in randevular:
            Veritabani.query('SELECT * from hastalar WHERE ID = ?', (hastaid,))
            hastasql = Veritabani.fetchone()
            Veritabani.query('SELECT * FROM doktorlar WHERE ID = ?', (doktorid,))
            doktorsql = Veritabani.fetchone()

            hasta = Hasta(*hastasql)
            doktor = Doktor(*doktorsql)

            Veritabani.query('SELECT hastane FROM hastaneler WHERE ID = ?', (doktor.hastaneid,))
            hastane = Veritabani.fetchone()[0]
            hastacell = QTableWidgetItem(hasta.isim + " " + hasta.soyisim)
            hastanecell = QTableWidgetItem(hastane)
            bolumcell = QTableWidgetItem(doktor.bolum)
            doktorcell = QTableWidgetItem(doktor.ad + " " + doktor.soyad)
            tarih = datetime.strptime(tarih, '%Y-%m-%d %H:%M:%S')
            tarihcell = QTableWidgetItem(tarih.strftime("%d.%m.%Y"))
            saatcell= QTableWidgetItem(tarih.strftime("%H:%M"))

            #Hepsinin yazısını ortala
            hastacell.setTextAlignment(QtCore.Qt.AlignCenter)
            hastanecell.setTextAlignment(QtCore.Qt.AlignCenter)
            bolumcell.setTextAlignment(QtCore.Qt.AlignCenter)
            doktorcell.setTextAlignment(QtCore.Qt.AlignCenter)
            tarihcell.setTextAlignment(QtCore.Qt.AlignCenter)
            saatcell.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, 0, hastacell)
            tablo.setItem(satir, 1, hastanecell)
            tablo.setItem(satir, 2, bolumcell)
            tablo.setItem(satir, 3, doktorcell)
            tablo.setItem(satir, 4, tarihcell)
            tablo.setItem(satir, 5, saatcell)

            satir+=1

        #tablo.resizeColumnsToContents()

    def randevuiptal(self):
        if self.randevulisteform.randevuTablo.rowCount() < 1: 
            return
        seciliindex = self.randevulisteform.randevuTablo.currentRow()
        yanit = QMessageBox.warning(self, " Randevu İptal", "Randevu İptal işlemini onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        
        if yanit == QMessageBox.No:
            return
        
        self.randevu_iptal_sinyal.emit(seciliindex)
        Randevu.randevu_iptal(seciliindex)
        self.randevulisteform.randevuTablo.removeRow(seciliindex)
        