from veritabani import Veritabani

class Doktor:
    def __init__(self, id, hastaneid, ad, soyad, bolum) -> None:
        self.id = id
        self.hastaneid = hastaneid
        self.ad = ad
        self.soyad = soyad
        self.bolum = bolum

    @staticmethod
    def ekle(isim,soyisim,hastane,bolum):
        Veritabani.query('INSERT INTO doktorlar (hastaneid, ad, soyad, bolum) VALUES (?, ?, ?, ?)', (hastane, isim, soyisim, bolum))
    
    def sil(self):
        Veritabani.query('DELETE FROM doktorlar WHERE ID = ?', (self.id,))
        Randevu.randevu_iptal(None, None, self.id)
                

class Hasta:
    def __init__(self, id, tc,isim,soyisim,telefon) -> None:
        self.id = id
        self.tc = tc
        self.isim = isim
        self.soyisim = soyisim
        self.telefon = telefon

    @staticmethod
    def ekle(tc,isim,soyisim,telefon):
        Veritabani.query('INSERT INTO hastalar (TC, Ad, Soyad, Telefon) VALUES(?, ?, ?, ?)', (tc, isim ,soyisim, telefon))

    def sil(self):
        Veritabani.query('DELETE FROM hastalar WHERE ID = ?', (self.id,))
        Randevu.randevu_iptal(None, self.id)


class Randevu:
    @staticmethod
    def randevu_al(hastaid, doktorid, tarih):
        Veritabani.query('INSERT INTO randevular (hastaid, doktorid, tarih) VALUES(?, ?, ?)', (hastaid, doktorid, tarih))
    @staticmethod
    def randevu_iptal(index, hastaid=None, doktorid=None):
        if (index is not None):
            Veritabani.query('DELETE FROM randevular WHERE ID = ?', (index+1,))
        elif (hastaid is not None): 
            Veritabani.query('DELETE FROM randevular WHERE hastaid = ?', (hastaid,))
        elif (doktorid is not None): 
            Veritabani.query('DELETE FROM randevular WHERE doktorid = ?', (doktorid,))

