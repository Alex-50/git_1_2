import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main1.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
