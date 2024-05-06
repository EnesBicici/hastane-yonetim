# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anapencere.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 365)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 161, 236))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.hastaneBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.hastaneBox.setFont(font)
        self.hastaneBox.setObjectName("hastaneBox")
        self.verticalLayout.addWidget(self.hastaneBox)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.bolumBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bolumBox.setFont(font)
        self.bolumBox.setObjectName("bolumBox")
        self.verticalLayout.addWidget(self.bolumBox)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.doktorBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.doktorBox.setFont(font)
        self.doktorBox.setObjectName("doktorBox")
        self.verticalLayout.addWidget(self.doktorBox)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.hastaBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.hastaBox.setFont(font)
        self.hastaBox.setObjectName("hastaBox")
        self.verticalLayout.addWidget(self.hastaBox)
        self.foto = QtWidgets.QLabel(self.centralwidget)
        self.foto.setGeometry(QtCore.QRect(340, 20, 200, 200))
        self.foto.setText("")
        self.foto.setPixmap(QtGui.QPixmap("../fotoğraflar/istanbul.png"))
        self.foto.setScaledContents(True)
        self.foto.setObjectName("foto")
        self.randevuButon = QtWidgets.QPushButton(self.centralwidget)
        self.randevuButon.setGeometry(QtCore.QRect(500, 260, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.randevuButon.setFont(font)
        self.randevuButon.setObjectName("randevuButon")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 240, 170, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tarih = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.tarih.setFont(font)
        self.tarih.setCalendarPopup(True)
        self.tarih.setObjectName("tarih")
        self.horizontalLayout.addWidget(self.tarih)
        self.saat = QtWidgets.QTimeEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.saat.setFont(font)
        self.saat.setMaximumTime(QtCore.QTime(17, 0, 0))
        self.saat.setMinimumTime(QtCore.QTime(9, 0, 0))
        self.saat.setObjectName("saat")
        self.horizontalLayout.addWidget(self.saat)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 21))
        self.menubar.setObjectName("menubar")
        self.menuAra = QtWidgets.QMenu(self.menubar)
        self.menuAra.setObjectName("menuAra")
        self.menuM_teri = QtWidgets.QMenu(self.menubar)
        self.menuM_teri.setObjectName("menuM_teri")
        self.menuKiralama = QtWidgets.QMenu(self.menubar)
        self.menuKiralama.setObjectName("menuKiralama")
        MainWindow.setMenuBar(self.menubar)
        self.doktorEkle = QtWidgets.QAction(MainWindow)
        self.doktorEkle.setObjectName("doktorEkle")
        self.doktorSil = QtWidgets.QAction(MainWindow)
        self.doktorSil.setObjectName("doktorSil")
        self.hastaEkle = QtWidgets.QAction(MainWindow)
        self.hastaEkle.setObjectName("hastaEkle")
        self.hastaSil = QtWidgets.QAction(MainWindow)
        self.hastaSil.setObjectName("hastaSil")
        self.randevuBilgi = QtWidgets.QAction(MainWindow)
        self.randevuBilgi.setObjectName("randevuBilgi")
        self.randevuIptal = QtWidgets.QAction(MainWindow)
        self.randevuIptal.setObjectName("randevuIptal")
        self.hastaListe = QtWidgets.QAction(MainWindow)
        self.hastaListe.setObjectName("hastaListe")
        self.menuAra.addAction(self.doktorEkle)
        self.menuAra.addAction(self.doktorSil)
        self.menuM_teri.addAction(self.hastaListe)
        self.menuM_teri.addAction(self.hastaEkle)
        self.menuM_teri.addAction(self.hastaSil)
        self.menuKiralama.addAction(self.randevuBilgi)
        self.menubar.addAction(self.menuAra.menuAction())
        self.menubar.addAction(self.menuM_teri.menuAction())
        self.menubar.addAction(self.menuKiralama.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Araç Kiralama"))
        self.label_6.setText(_translate("MainWindow", "Hastane"))
        self.label_2.setText(_translate("MainWindow", "Bölüm"))
        self.label_3.setText(_translate("MainWindow", "Doktor"))
        self.label.setText(_translate("MainWindow", "Hasta"))
        self.randevuButon.setText(_translate("MainWindow", "Randevu Al"))
        self.label_4.setText(_translate("MainWindow", "Tarih :"))
        self.menuAra.setTitle(_translate("MainWindow", "Doktor"))
        self.menuM_teri.setTitle(_translate("MainWindow", "Hasta"))
        self.menuKiralama.setTitle(_translate("MainWindow", "Randevu "))
        self.doktorEkle.setText(_translate("MainWindow", "Doktor Ekle"))
        self.doktorSil.setText(_translate("MainWindow", "Doktor Sil"))
        self.hastaEkle.setText(_translate("MainWindow", "Hasta Ekle"))
        self.hastaSil.setText(_translate("MainWindow", "Hasta Sil"))
        self.randevuBilgi.setText(_translate("MainWindow", "Randevu Bilgisi"))
        self.randevuIptal.setText(_translate("MainWindow", "Randevu İptal"))
        self.hastaListe.setText(_translate("MainWindow", "Hasta Listesi"))
