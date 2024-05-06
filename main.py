from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtGui
from anapencere_ui import Ui_MainWindow
from hastane import Doktor,Hasta,Randevu
from datetime import date, timedelta
from hastaekle import HastaEkleSayfa
from hastasil import HastaSilSayfa
from hastaliste import HastaListeSayfa
from doktorekle import DoktorEkleSayfa
from doktorsil import DoktorSilSayfa
from randevuliste import RandevuListeSayfa
from veritabani import Veritabani
from datetime import datetime

class arayuz(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.qtprogram = Ui_MainWindow()
        self.qtprogram.setupUi(self)
        self.qtprogram.hastaneBox.currentIndexChanged.connect(self.bolum_liste_guncelle)
        self.qtprogram.bolumBox.currentIndexChanged.connect(self.doktor_liste_guncelle)
        Veritabani.query('SELECT ID, hastane FROM hastaneler')
        hastaneler = Veritabani.fetchall()
        for id, hastanee in hastaneler:
            self.qtprogram.hastaneBox.addItem(hastanee, id)
        self.hasta_liste_guncelle()
        bugun = date.today()
        self.qtprogram.tarih.setDate(bugun)
        self.qtprogram.tarih.setMinimumDate(bugun)
        self.qtprogram.tarih.setMaximumDate(bugun+timedelta(days=30))
        hastaeklesayfa = HastaEkleSayfa()
        hastaeklesayfa.hasta_ekle_sinyal.connect(self.hasta_liste_guncelle)
        self.qtprogram.hastaEkle.triggered.connect(lambda: hastaeklesayfa.show())
        hastasilsayfa = HastaSilSayfa()
        hastasilsayfa.hasta_sil_sinyal.connect(self.hasta_liste_guncelle)
        self.qtprogram.hastaSil.triggered.connect(lambda: hastasilsayfa.goster())
        hastalistesayfa = HastaListeSayfa()
        self.qtprogram.hastaListe.triggered.connect(lambda: hastalistesayfa.goster())
        doktoreklesayfa = DoktorEkleSayfa()
        self.qtprogram.doktorEkle.triggered.connect(lambda: doktoreklesayfa.goster())
        doktoreklesayfa.doktor_ekle_sinyal.connect(self.doktor_liste_guncelle)
        doktorsilsayfa = DoktorSilSayfa()
        self.qtprogram.doktorSil.triggered.connect(lambda: doktorsilsayfa.goster())
        doktorsilsayfa.doktor_sil_sinyal.connect(self.doktor_liste_guncelle)
        self.qtprogram.randevuButon.clicked.connect(self.randevual)
        randevulistesayfa = RandevuListeSayfa()
        self.qtprogram.randevuBilgi.triggered.connect(lambda: randevulistesayfa.goster())
        randevulistesayfa.randevu_iptal_sinyal.connect(Randevu.randevu_iptal)


    def hasta_liste_guncelle(self):
        self.qtprogram.hastaBox.clear()
        Veritabani.query('SELECT * FROM hastalar')
        hastalar = Veritabani.fetchall()
        if hastalar is None:
            return
        
        for hasta in hastalar:
            hastaa = Hasta(*hasta)
            self.qtprogram.hastaBox.addItem(f"{hastaa.isim} {hastaa.soyisim}", hastaa.id)


    def randevual(self):
        hastaindex = self.qtprogram.hastaBox.currentIndex()
        if hastaindex < 0:
            QMessageBox.warning(self, "Randevu", "Randevu almak için hasta eklemelisiniz.", QMessageBox.Ok)
            return
                
        yanit = QMessageBox.warning(self, "Randevu", "Randevu alma işlemini onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
    
        if yanit == QMessageBox.No:
            return
        
        doktorid = self.qtprogram.doktorBox.currentData()
        hastaid = self.qtprogram.hastaBox.currentData()
        tarih = self.qtprogram.tarih.date().toPyDate()
        saat = self.qtprogram.saat.time().toPyTime()
        Veritabani.query('SELECT * from randevular WHERE hastaid = ? AND doktorid = ? AND tarih = ?', (hastaid, doktorid, datetime.combine(tarih, saat)))
        randevuuu = Veritabani.fetchone()
        if randevuuu is not None: 
            QMessageBox.warning(self, "Randevu", "Seçtiğiniz Tarih ve Zamanda Uygun Randevu Bulunmamaktadır.", QMessageBox.Ok)
            return
        
        Randevu.randevu_al(hastaid, doktorid, datetime.combine(tarih, saat))
        QMessageBox.information(self, "Randevu", "Randevu Alındı.", QMessageBox.Ok)

    def bolum_liste_guncelle(self):
        self.qtprogram.bolumBox.clear()
        hastaneid = self.qtprogram.hastaneBox.currentData()
        Veritabani.query('SELECT bolumler, foto FROM hastaneler WHERE ID = ?', (hastaneid, ))
        hastanee = Veritabani.fetchone()
        for bolum in hastanee[0].split(','):
            self.qtprogram.bolumBox.addItem(bolum)
        self.qtprogram.foto.setPixmap(QtGui.QPixmap("fotograflar/"+hastanee[1]))

    def doktor_liste_guncelle(self):
        self.qtprogram.doktorBox.clear()
        bolumm = self.qtprogram.bolumBox.currentText()
        hastaneid = self.qtprogram.hastaneBox.currentData()

        Veritabani.query('SELECT * FROM doktorlar WHERE hastaneid = ? AND bolum = ?', (hastaneid, bolumm))
        doktorlar = Veritabani.fetchall()

        if doktorlar is None:
            return

        for doktor in doktorlar:
            doktorr = Doktor(*doktor)
            self.qtprogram.doktorBox.addItem(f"{doktorr.ad} {doktorr.soyad}", doktorr.id)  


app = QApplication([])
pencere = arayuz()
pencere.show()
app.exec_()
