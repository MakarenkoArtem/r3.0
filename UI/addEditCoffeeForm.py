# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, QWidget):
        QWidget.setObjectName("QWidget состава кофе")
        QWidget.setGeometry(QtCore.QRect(0, 0, 400, 292))
        QWidget.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton = QtWidgets.QPushButton(QWidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(QWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(QWidget)
        self.label.setGeometry(QtCore.QRect(16, 20, 141, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(QWidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(QWidget)
        self.label_2.setGeometry(QtCore.QRect(16, 50, 121, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(QWidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 50, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(QWidget)
        self.label_3.setGeometry(QtCore.QRect(16, 80, 121, 20))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(QWidget)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 80, 121, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(QWidget)
        self.label_4.setGeometry(QtCore.QRect(16, 110, 121, 20))
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QtWidgets.QComboBox(QWidget)
        self.comboBox_3.setGeometry(QtCore.QRect(210, 110, 121, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_5 = QtWidgets.QLabel(QWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 101, 20))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(QWidget)
        self.textEdit.setGeometry(QtCore.QRect(113, 170, 271, 71))
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(QWidget)
        self.label_6.setGeometry(QtCore.QRect(16, 140, 41, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(QWidget)
        self.label_7.setGeometry(QtCore.QRect(180, 140, 101, 20))
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(QWidget)
        self.spinBox.setGeometry(QtCore.QRect(70, 140, 91, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999999)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(QWidget)
        self.spinBox_2.setGeometry(QtCore.QRect(290, 140, 91, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(999999)
        self.spinBox_2.setObjectName("spinBox_2")

        self.retranslateUi(QWidget)
        QtCore.QMetaObject.connectSlotsByName(QWidget)

    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate
        QWidget.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Сохранить"))
        self.pushButton_2.setText(_translate("Form", "Отмена"))
        self.label.setText(_translate("Form", "Название кофе"))
        self.label_2.setText(_translate("Form", "Название сорта"))
        self.comboBox.setItemText(0, _translate("Form", "Арабика"))
        self.comboBox.setItemText(1, _translate("Form", "Робуста"))
        self.comboBox.setItemText(2, _translate("Form", "Либерика"))
        self.label_3.setText(_translate("Form", "Степень обжарки"))
        self.comboBox_2.setItemText(0, _translate("Form", "Очень темная"))
        self.comboBox_2.setItemText(1, _translate("Form", "Темная"))
        self.comboBox_2.setItemText(2, _translate("Form", "Средне-темная"))
        self.comboBox_2.setItemText(3, _translate("Form", "Средняя"))
        self.comboBox_2.setItemText(4, _translate("Form", "Светлая"))
        self.label_4.setText(_translate("Form", "Молотый/в зёрнах"))
        self.comboBox_3.setItemText(0, _translate("Form", "В зёрнах"))
        self.comboBox_3.setItemText(1, _translate("Form", "Молотый"))
        self.label_5.setText(_translate("Form", "Описание вкуса"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("Form", "Цена"))
        self.label_7.setText(_translate("Form", "Объем упаковки"))
