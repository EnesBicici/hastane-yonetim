import sqlite3

class veritabani:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='hastaneler'")
        tablo_var_mi = self.cursor.fetchone()

        if not tablo_var_mi:  # Tablo yok
            self.cursor.execute('CREATE TABLE IF NOT EXISTS hastaneler (ID INTEGER PRIMARY KEY AUTOINCREMENT, hastane TEXT, bolumler TEXT, foto TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS doktorlar (ID INTEGER PRIMARY KEY AUTOINCREMENT, hastaneid INTEGER, ad TEXT, soyad TEXT, bolum TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS hastalar (ID INTEGER PRIMARY KEY AUTOINCREMENT, TC TEXT, ad TEXT, soyad TEXT, telefon TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS randevular (ID INTEGER PRIMARY KEY AUTOINCREMENT, hastaid INTEGER, doktorid INTEGER, tarih TIMESTAMP)')

            hastane_tuple = [
                ('Sadi Konuk', 'Nöroloji,Kardiyoloji', 'sadi.png'),
                ('Medipol', 'Dahiliye,Göz', 'medipol.png'),
                ('Samsun', 'Nöroloji,Dahiliye', 'samsun.png'),
                ('İstanbul', 'Göz,Kardiyoloji', 'istanbul.png')
            ]

            doktor_tuple = [
                (4, 'Ahmet', 'Ak', 'Kardiyoloji'),
                (1, 'Yasin', 'Balık', 'Kardiyoloji'),
                (1, 'Leyla', 'Türk', 'Kardiyoloji'),
                (3, 'Mehmet', 'Yıldırım', 'Nöroloji'),
                (3, 'Ceyda', 'Sönmez', 'Nöroloji'),
                (1, 'Hasan', 'Aslan', 'Nöroloji'),
                (2, 'Su', 'Yeşil', 'Dahiliye'),
                (3, 'Beyza', 'Şimşek', 'Dahiliye'),
                (2, 'Murat', 'Erkan', 'Dahiliye'),
                (2, 'Erdem', 'Yücesan', 'Göz'),
                (4, 'Muharrem', 'Altunışık', 'Göz'),
                (2, 'Gökhan', 'Halimoğlu', 'Göz')
            ]

            self.cursor.executemany('INSERT INTO hastaneler (hastane, bolumler, foto) VALUES (?, ?, ?)', hastane_tuple)
            self.cursor.executemany('INSERT INTO doktorlar (hastaneid, ad, soyad, bolum) VALUES (?, ?, ?, ?)', doktor_tuple)
            self.connection.commit()

    def query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        return self.cursor
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()
    
Veritabani = veritabani('sql.db')
