from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qtgui import QFont 
import sys

def window():

    app= QApplication(sys.argv)
    win= QMainWindow()
    win.setGeometry(150, 150, 500, 500)
    win.setWindowTitle("ABCC- Voice Based Coding")

    titleLabel = QtWidgets.QLabel(win)
    titleLabel.setText("ABCC")
    titleLabel.move(250, 250)
    titleLabel.setFont(QFont(Times, 25))

    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()