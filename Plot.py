from __future__ import division
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
from PyQt5 import QtGui, QtWidgets
import sys
from visual import *


class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.button = QtWidgets.QPushButton("Plot")
        self.button.clicked.connect(self.plot)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        import numpy as np
        # scene = display(width=1000, height=1000)
        # Earth = sphere(pos=vec(200,0,0), radius=10, texture=textures.earth, make_trail=True)
        Earth = sphere(pos=vector(200,0,0), radius=10, material=materials.earth, make_trail=True)
        Sun = sphere(pos=vector(0,0,0), radius=100, color=color.yellow)
        # Sun = sphere(pos=vec(0,0,0), radius=100, color=color.yellow)

        Earth.v = vec(0,-8,0)
        for ii in range(1000):
            rate(100)

            rmag = np.sqrt(Earth.pos.x**2 + Earth.pos.y**2 + Earth.pos.z**2)
            F12 = (10000*(Sun.pos - Earth.pos))/rmag**3
            Earth.v += F12
            Earth.pos += Earth.v
        # box()
        # data = [random.random() for ii in range(25)]
        # ax = self.figure.add_subplot(1,1,1)
        # ax.hold(False)
        # ax.plot(data, '*-')
        self.canvas.draw()

app = QtWidgets.QApplication(sys.argv)
frame = Window()
frame.show()
app.exec_()
