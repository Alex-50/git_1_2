import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from Ui import Ui_MainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(600, 600)
        self.do_paint = False
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            self.x = randint(100, 500)
            self.y = randint(100, 500)
            self.r = randint(1, 90)
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        self.a = randint(0, 256)
        self.b = randint(0, 256)
        self.c = randint(0, 256)
        qp.setBrush(QColor(self.a, self.b, self.c))
        qp.drawEllipse(self.x - self.r, self.y - self.r, self.r, self.r)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
