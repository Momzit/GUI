import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtWidgets
from PyQt5 import *

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QWidget()

    l1=QtWidgets.QLabel("Catchy title here")
    l1.setGeometry(QtCore.QRect(280, 70, 231, 27))
    font = QtGui.QFont()
    font.setFamily("Snap ITC")
    font.setPointSize(16)
    l1.setFont(font)
    l1.setAlignment(QtCore.Qt.AlignCenter)

    vbox=QtWidgets.QVBoxLayout()
    vbox.addWidget(l1)

    hbox=QtWidgets.QHBoxLayout()
    b1=QtWidgets.QPushButton("Earth-Sun-Moon")
    b1.setGeometry(QtCore.QRect(530, 242, 251, 41))
    font = QtGui.QFont()
    font.setPointSize(14)
    b1.setFont(font)

    b2=QtWidgets.QPushButton("Launch Rocket")
    b2.setGeometry(QtCore.QRect(530, 242, 251, 41))
    b2.setFont(font)

    hbox.addWidget(b1)
    hbox.addStretch()
    hbox.addWidget(b2)
    vbox.addStretch()
    vbox.addLayout(hbox)
    win.setLayout(vbox)

    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())

def newwindow(self):
    self.

if __name__ == '__main__':
    window()
