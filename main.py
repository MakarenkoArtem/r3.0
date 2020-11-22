import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QDialog
from PyQt5 import uic, QtCore, QtGui, QtWidgets
import sys
sys.path.insert(0, 'UI')
from UI.addEditCoffeeForm import Ui_Form
from main import Ui_Form1

class Change(QDialog, Ui_Form):
    def __init__(self, title):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffee.sqlite")
        self.cur = self.con.cursor()
        self.title = title
        if title != '':
            self.given()
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.work)

    def given(self):
        result = self.cur.execute(
            f"SELECT * FROM coffee WHERE title='{self.title}'").fetchall()[0]
        if not result:
            return
        for i, elem in enumerate(result[1:]):
            if i == 0:
                self.lineEdit.setText(elem)
            elif i == 1:
                self.comboBox.setCurrentIndex(elem - 1)
            elif i == 2:
                self.comboBox_2.setCurrentIndex(elem - 1)
            elif i == 3:
                self.comboBox_3.setCurrentIndex(elem - 1)
            elif i == 4:
                self.textEdit.setPlainText(elem)
            elif i == 5:
                self.spinBox.setValue(elem)
            elif i == 6:
                self.spinBox_2.setValue(elem)

    def work(self):
        if self.title == '':
            self.cur.execute(
                f"""INSERT INTO Coffee(title, grade, Degree_of_roast, type, taste, price, volume) VALUES('{self.lineEdit.text().capitalize()}', {self.comboBox.currentIndex() + 1}, {self.comboBox_2.currentIndex() + 1}, {self.comboBox_3.currentIndex() + 1}, '{self.textEdit.toPlainText()}', {self.spinBox.value()}, {self.spinBox_2.value()})""")
        else:
            self.cur.execute(
                f"""UPDATE Coffee
                SET title = '{self.lineEdit.text().capitalize()}', grade = {self.comboBox.currentIndex() + 1}, Degree_of_roast = {self.comboBox_2.currentIndex() + 1}, type = {self.comboBox_3.currentIndex() + 1}, taste = '{self.textEdit.toPlainText()}', price = {self.spinBox.value()}, volume = {self.spinBox_2.value()}
                WHERE title = '{self.title}'""")
        self.con.commit()
        self.con.close()
        self.close()


class MyWidget(QMainWindow, Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffee.sqlite")
        self.cur = self.con.cursor()
        self.pushButton.clicked.connect(self.update_result)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.pushButton_2.clicked.connect(self.change)
        self.pushButton_3.clicked.connect(self.change)
        self.pushButton_4.clicked.connect(self.delete)


    def delete(self):
        title = self.plainTextEdit.toPlainText().split('=')[-1].capitalize()
        result = self.cur.execute(f"SELECT * FROM coffee WHERE title='{title}'").fetchall()
        if not result:
            return
        valid = QMessageBox.question(
            self, 'Удаление кофе', "Действительно хотите удалить " + title,
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            self.cur.execute(f"DELETE FROM coffee WHERE title IN ('{title}')")
            self.con.commit()
        self.update_result()

    def change(self):
        title = self.plainTextEdit.toPlainText().split('=')[-1].capitalize()
        result = self.cur.execute(
            f"SELECT * FROM coffee WHERE title='{title}'").fetchall()
        if not result or self.sender() == self.pushButton_3:
            title = ''
        Change(title).exec_()
        self.update_result()

    def update_result(self):
        result = self.cur.execute(
            f"SELECT * FROM coffee WHERE title='{self.plainTextEdit.toPlainText().split('=')[-1].capitalize()}'").fetchall()
        self.tableWidget.setRowCount(len(result))
        if not result:
            return
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            s = list(elem[:2]) + [self.cur.execute(
                f"SELECT title FROM grades WHERE id={elem[2]}").fetchall()[0][0], self.cur.execute(
                f"SELECT title FROM Degree_of_roast WHERE id={elem[3]}").fetchall()[0][0],
                                  self.cur.execute(
                                      f"SELECT title FROM type_coffee WHERE id={elem[4]}").fetchall()[
                                      0][0]] + list(elem[5:])
            for j, val in enumerate(s):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def item_changed(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
