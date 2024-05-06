from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from doktorekle_ui import Ui_Form
from PyQt5.QtGui import QIntValidator
from veritabani import Veritabani
from hastane import Doktor

class DoktorEkleSayfa(QWidget):
    doktor_ekle_sinyal = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.doktorekleform = Ui_Form()
        self.doktorekleform.setupUi(self)
        self.doktorekleform.ekleButon.clicked.connect(self.ekle)
        self.doktorekleform.hastaneBox.currentIndexChanged.connect(self.bolum_liste_guncelle)

    def goster (self):
        self.show()
        if self.doktorekleform.hastaneBox.count() < 1:
            Veritabani.query('SELECT ID, hastane FROM hastaneler')
            hastaneler = Veritabani.fetchall()
            for id, hastanee in hastaneler:
                self.doktorekleform.hastaneBox.addItem(hastanee, id)
    
    def bolum_liste_guncelle(self):
        self.doktorekleform.bolumBox.clear()
        hastaneid = self.doktorekleform.hastaneBox.currentData()
        Veritabani.query('SELECT bolumler FROM hastaneler WHERE ID = ?', (hastaneid, ))
        hastanee = Veritabani.fetchone()
        for bolum in hastanee[0].split(','):
            self.doktorekleform.bolumBox.addItem(bolum)

    def ekle(self):
        yanit = QMessageBox.warning(self, "Doktor Ekleme", "Doktor ekleme işlemini onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        
        if yanit == QMessageBox.No:
            return
        
        ad = self.doktorekleform.adLine.text()
        soyad = self.doktorekleform.soyadLine.text()
        hastane = self.doktorekleform.hastaneBox.currentData()
        bolum = self.doktorekleform.bolumBox.currentText()
        
        Doktor.ekle(ad, soyad, hastane, bolum)
        self.doktor_ekle_sinyal.emit()
        
        