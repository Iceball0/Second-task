import sys
import random as rand
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.btn.clicked.connect(self.run)
        self.start = False

    def run(self):
        self.start = True
        self.repaint()

    def paintEvent(self, event):
        if self.start:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(rand.randint(2, 5)):
            size = rand.randint(10, 100)
            x, y = rand.randint(50, 470), rand.randint(160, 380)
            qp.drawEllipse(x, y, size, size)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
