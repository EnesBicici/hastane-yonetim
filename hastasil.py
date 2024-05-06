from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from hastasil_ui import Ui_Form
from veritabani import Veritabani
from hastane import Hasta

class HastaSilSayfa(QWidget):
    hasta_sil_sinyal = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.hastasilform = Ui_Form()
        self.hastasilform.setupUi(self)
        self.hastasilform.silButon.clicked.connect(self.sil)

    def goster(self):
        self.hastasilform.musteriBox.clear()
        Veritabani.query('SELECT * FROM hastalar')
        hastalarsql = Veritabani.fetchall()
        self.show()

        if hastalarsql is None:
            return

        self.hastalar = []

        for hasta in hastalarsql:
            hastaa = Hasta(*hasta)
            self.hastalar.append(hastaa)
            self.hastasilform.musteriBox.addItem(f"{hastaa.isim} {hastaa.soyisim}", hastaa.id)

    def sil(self):
        indeks = self.hastasilform.musteriBox.currentIndex()
        if indeks < 0:
            return
        
        yanit = QMessageBox.warning(self, "Hasta Silme", "Hasta silme işlemini onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        if yanit == QMessageBox.No:
            return
        
        hasta = self.hastalar[indeks]

        hasta.sil()

        self.hastasilform.musteriBox.removeItem(indeks)
        self.hasta_sil_sinyal.emit()