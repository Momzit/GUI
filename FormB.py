# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormB.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# from MainWindow import Ui_MainWindow

class Ui_Form(object):
    # def Main(self):
    #     self.window = QtWidgets.QMainWindow()   #Here you define the type of window you opening, in my case it is a widget
    #     self.ui = Ui_MainWindow()      #Class from the widget form
    #     self.ui.setupUi(self.window)     #Function we want to load from the widget
    #     Form.hide()             #When we open the new window, hide the main one
    #     self.window.show()              #This just shows the window

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(890, 831)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 30, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(270, 110, 601, 301))
        self.graphicsView.setObjectName("graphicsView")

        #Reset button
        self.Rest = QtWidgets.QPushButton(Form)
        self.Rest.setGeometry(QtCore.QRect(740, 430, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Rest.setFont(font)
        self.Rest.setObjectName("Rest")

        #Start button
        self.Start = QtWidgets.QPushButton(Form)
        self.Start.setGeometry(QtCore.QRect(270, 432, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Start.setFont(font)
        self.Start.setObjectName("Start")

        #MainScreen button
        self.MainScreen = QtWidgets.QPushButton(Form)
        self.MainScreen.setGeometry(QtCore.QRect(130, 372, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.MainScreen.setFont(font)
        self.MainScreen.setObjectName("MainScreen")
        # self.MainScreen.clicked.connect(self.Main)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 150, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 180, 181, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.textEdit_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(510, 430, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2.setBuddy(self.textEdit)
        self.label_3.setBuddy(self.textEdit_2)
        self.label_4.setBuddy(self.textEdit_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.Rest.setText(_translate("Form", "Reset"))
        self.Start.setText(_translate("Form", "Start"))
        self.MainScreen.setText(_translate("Form", "Main Screen"))
        self.label_5.setText(_translate("Form", "Velocity"))
        self.label_2.setText(_translate("Form", "X:"))
        self.label_3.setText(_translate("Form", "Y:"))
        self.label_4.setText(_translate("Form", "Z:"))
        self.pushButton.setText(_translate("Form", "Pause"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
