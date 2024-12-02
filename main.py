from PyQt5 import QtWidgets, QtGui
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.drawButton = QtWidgets.QPushButton(self.centralwidget)
        self.drawButton.setObjectName("drawButton")
        self.drawButton.setText("нарисоват")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.drawButton.clicked.connect(self.draw_circle)

        self.circles = []

    def draw_circle(self):
        diameter = random.randint(10, 100)
        color = self.random_color()
        self.circles.append((diameter, color))
        self.update()

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for diameter, color in self.circles:
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            painter.setBrush(QtGui.QColor(*color))
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
