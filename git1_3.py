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
        self.initUI()
        self.flag = False

    def initUI(self):
        self.setFixedSize(800, 800)
        self.setWindowTitle('Colours')
        self.btn = QPushButton("Paint", self)
        self.btn.move(100, 100)
        self.btn.clicked.connect(self.onClicked)
        self.show()
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
            qp.setBrush(QColor(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
            qp.drawEllipse(*[random.randrange(0,800),random.randrange(0,800)], random.randrange(0,100), random.randrange(0,100))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
