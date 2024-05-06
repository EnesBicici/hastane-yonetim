from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from hastaekle_ui import Ui_Form
from PyQt5.QtGui import QIntValidator
from hastane import Hasta

class HastaEkleSayfa(QWidget):
    hasta_ekle_sinyal = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.hastaekleform = Ui_Form()
        self.hastaekleform.setupUi(self)
        sadecenumerik = QIntValidator()
        self.hastaekleform.tcLine.setValidator(sadecenumerik)
        self.hastaekleform.telefonLine.setValidator(sadecenumerik)
        self.hastaekleform.ekleButon.clicked.connect(self.ekle)

    def ekle(self):
        yanit = QMessageBox.warning(self, "Hasta Ekleme", "Hasta ekleme işlemini onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        
        if yanit == QMessageBox.No:
            return
        
        tc = self.hastaekleform.tcLine.text()
        ad = self.hastaekleform.adLine.text()
        soyad = self.hastaekleform.soyadLine.text()
        telefon = self.hastaekleform.telefonLine.text()
        Hasta.ekle(tc, ad, soyad, telefon)
        self.hasta_ekle_sinyal.emit()