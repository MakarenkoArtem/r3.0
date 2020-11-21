import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic, QtCore, QtGui, QtWidgets


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.pushButton.clicked.connect(self.update_result)
        self.tableWidget.itemChanged.connect(self.item_changed)

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
            f"SELECT title FROM Degree_of_roast WHERE id={elem[3]}").fetchall()[0][0], self.cur.execute(
            f"SELECT title FROM type_coffee WHERE id={elem[4]}").fetchall()[0][0]] + list(elem[5:])
            for j, val in enumerate(s):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def item_changed(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
