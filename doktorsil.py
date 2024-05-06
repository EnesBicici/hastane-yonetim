from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from doktorsil_ui import Ui_Form
from veritabani import Veritabani
from hastane import Doktor

class DoktorSilSayfa(QWidget):
    doktor_sil_sinyal = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.doktorsilform = Ui_Form()
        self.doktorsilform.setupUi(self)
        self.doktorsilform.silButon.clicked.connect(self.sil)
        self.doktorsilform.hastaneBox.currentIndexChanged.connect(self.bolum_liste_guncelle)
        self.doktorsilform.bolumBox.currentIndexChanged.connect(self.doktor_liste_guncelle)

    def goster (self):
        self.show()
        self.doktorsilform.hastaneBox.clear()
        Veritabani.query('SELECT ID, hastane FROM hastaneler')
        hastaneler = Veritabani.fetchall()
        for id, hastanee in hastaneler:
            self.doktorsilform.hastaneBox.addItem(hastanee, id)
    
    def bolum_liste_guncelle(self):
        self.doktorsilform.bolumBox.clear()
        hastaneid = self.doktorsilform.hastaneBox.currentData()
        if hastaneid is None:
            return
        Veritabani.query('SELECT bolumler FROM hastaneler WHERE ID = ?', (hastaneid, ))
        hastanee = Veritabani.fetchone()
        for bolum in hastanee[0].split(','):
            self.doktorsilform.bolumBox.addItem(bolum)

    def doktor_liste_guncelle(self):
        self.doktorsilform.doktorBox.clear()
        bolumm = self.doktorsilform.bolumBox.currentText()
        hastaneid = self.doktorsilform.hastaneBox.currentData()
        if hastaneid is None:
            return

        Veritabani.query('SELECT * FROM doktorlar WHERE hastaneid = ? AND bolum = ?', (hastaneid, bolumm))
        doktorlarsql = Veritabani.fetchall()

        if doktorlarsql is None:
            return
        
        self.doktorlar = []

        for doktor in doktorlarsql:
            doktorr = Doktor(*doktor)
            self.doktorlar.append(doktorr)
            self.doktorsilform.doktorBox.addItem(f"{doktorr.ad} {doktorr.soyad}", doktorr.id)  


    def sil(self):
        yanit = QMessageBox.warning(self, "Doktor silme", "Doktor silme işlemini onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        
        if yanit == QMessageBox.No:
            return
        
        index = self.doktorsilform.doktorBox.currentIndex()
        doktorid = self.doktorsilform.doktorBox.currentData()
        doktor = next((dr for dr in self.doktorlar if dr.id == doktorid), None)
        doktor.sil()
        self.doktor_sil_sinyal.emit()
        self.doktorsilform.doktorBox.removeItem(index)

        
        