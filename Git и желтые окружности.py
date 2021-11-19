import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
from PyQt5.QtWidgets import QPushButton
import uic



class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('planner.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paintEvent())

    def draw(self):
        self.side = float(self.lineEdit.text())
        self.coef = float(self.lineEdit_2.text())
        self.n = int(self.lineEdit_3.text())
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))

            for _ in range(3):
                self.drawCircle(qp)
                DELTA = (self.side * (1 - self.coef)) / 2
                self.side *= self.coef
                self.x += DELTA
                self.y += DELTA
            qp.end()

    def drawCircle(self, qp):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())