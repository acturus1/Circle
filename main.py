import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)
        self.drawButton = self.findChild(QtWidgets.QPushButton, 'drawButton')
        self.drawButton.clicked.connect(self.draw_circle)

        self.circles = []

    def draw_circle(self):
        diameter = random.randint(1, 100)
        self.circles.append(diameter)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for diameter in self.circles:
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            painter.setBrush(QColor('yellow'))
            painter.drawEllipse(x, y, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
