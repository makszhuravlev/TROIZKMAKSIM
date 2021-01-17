from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt
import sys
from PyQt5 import uic
import os
import random

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        path = "\\".join(os.getcwd().split("\\")[:-2]) + "\\yl\\A.ui"
        uic.loadUi(path, self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.onClicked)
        self.flag = False

    def onClicked(self):
        self.flag = True
        self.update()

    def paintEvent(self, e):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawRectangles(qp)
            qp.end()

    def drawRectangles(self, qp):
        qp.setPen(Qt.black)
        for i in range (100):
            qp.setBrush(QColor(248,255,1))
            qp.drawEllipse(random.randrange(0,800),random.randrange(0,800), random.randrange(0,100), random.randrange(0,100))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
