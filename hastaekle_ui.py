# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musteriekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(224, 190)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tcLine = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.tcLine.setFont(font)
        self.tcLine.setMaxLength(11)
        self.tcLine.setObjectName("tcLine")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tcLine)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.adLine = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.adLine.setFont(font)
        self.adLine.setText("")
        self.adLine.setMaxLength(30)
        self.adLine.setObjectName("adLine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.adLine)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.soyadLine = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.soyadLine.setFont(font)
        self.soyadLine.setText("")
        self.soyadLine.setMaxLength(30)
        self.soyadLine.setObjectName("soyadLine")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.soyadLine)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.telefonLine = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.telefonLine.setFont(font)
        self.telefonLine.setText("")
        self.telefonLine.setMaxLength(10)
        self.telefonLine.setObjectName("telefonLine")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.telefonLine)
        self.ekleButon = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ekleButon.setFont(font)
        self.ekleButon.setObjectName("ekleButon")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.ekleButon)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ekle"))
        self.label.setText(_translate("Form", "TC Kimlik:"))
        self.label_2.setText(_translate("Form", "Ad:"))
        self.label_3.setText(_translate("Form", "Soyad:"))
        self.label_4.setText(_translate("Form", "Telefon:"))
        self.ekleButon.setText(_translate("Form", "Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
