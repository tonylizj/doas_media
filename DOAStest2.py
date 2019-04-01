from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 1100)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pic1 = QtWidgets.QLabel(self.centralwidget)
        self.pic1.setGeometry(QtCore.QRect(0, 0, 350, 350))
        self.pic1.setFrameShape(QtWidgets.QFrame.Box)
        self.pic1.setText("")
        self.pic1.setObjectName("pic1")
        self.pic2 = QtWidgets.QLabel(self.centralwidget)
        self.pic2.setGeometry(QtCore.QRect(350, 0, 350, 350))
        self.pic2.setFrameShape(QtWidgets.QFrame.Box)
        self.pic2.setText("")
        self.pic2.setObjectName("pic2")
        self.pic3 = QtWidgets.QLabel(self.centralwidget)
        self.pic3.setGeometry(QtCore.QRect(700, 0, 350, 350))
        self.pic3.setFrameShape(QtWidgets.QFrame.Box)
        self.pic3.setText("")
        self.pic3.setObjectName("pic3")
        self.pic4 = QtWidgets.QLabel(self.centralwidget)
        self.pic4.setGeometry(QtCore.QRect(0, 350, 350, 350))
        self.pic4.setFrameShape(QtWidgets.QFrame.Box)
        self.pic4.setText("")
        self.pic4.setObjectName("pic4")
        self.pic5 = QtWidgets.QLabel(self.centralwidget)
        self.pic5.setGeometry(QtCore.QRect(350, 350, 350, 350))
        self.pic5.setFrameShape(QtWidgets.QFrame.Box)
        self.pic5.setText("")
        self.pic5.setObjectName("pic5")
        self.pic6 = QtWidgets.QLabel(self.centralwidget)
        self.pic6.setGeometry(QtCore.QRect(700, 350, 350, 350))
        self.pic6.setFrameShape(QtWidgets.QFrame.Box)
        self.pic6.setText("")
        self.pic6.setObjectName("pic6")
        self.pic7 = QtWidgets.QLabel(self.centralwidget)
        self.pic7.setGeometry(QtCore.QRect(0, 700, 350, 350))
        self.pic7.setFrameShape(QtWidgets.QFrame.Box)
        self.pic7.setText("")
        self.pic7.setObjectName("pic7")
        self.pic8 = QtWidgets.QLabel(self.centralwidget)
        self.pic8.setGeometry(QtCore.QRect(350, 700, 350, 350))
        self.pic8.setFrameShape(QtWidgets.QFrame.Box)
        self.pic8.setText("")
        self.pic8.setObjectName("pic8")
        self.pic9 = QtWidgets.QLabel(self.centralwidget)
        self.pic9.setGeometry(QtCore.QRect(700, 700, 350, 350))
        self.pic9.setFrameShape(QtWidgets.QFrame.Box)
        self.pic9.setText("")
        self.pic9.setObjectName("pic9")
        self.Btn1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn1_1.setGeometry(QtCore.QRect(0, 0, 350, 175))
        self.Btn1_1.setObjectName("Btn1_1")
        self.Btn1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn1_2.setGeometry(QtCore.QRect(0, 175, 350, 175))
        self.Btn1_2.setObjectName("Btn1_2")
        self.Btn2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn2_1.setGeometry(QtCore.QRect(350, 0, 350, 175))
        self.Btn2_1.setObjectName("Btn2_1")
        self.Btn2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn2_2.setGeometry(QtCore.QRect(350, 175, 350, 175))
        self.Btn2_2.setObjectName("Btn2_2")
        self.Btn3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn3_1.setGeometry(QtCore.QRect(700, 0, 350, 175))
        self.Btn3_1.setObjectName("Btn3_1")
        self.Btn3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn3_2.setGeometry(QtCore.QRect(700, 175, 350, 175))
        self.Btn3_2.setObjectName("Btn3_2")
        self.Btn4_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn4_1.setGeometry(QtCore.QRect(0, 350, 350, 175))
        self.Btn4_1.setObjectName("Btn4_1")
        self.Btn4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn4_2.setGeometry(QtCore.QRect(0, 525, 350, 175))
        self.Btn4_2.setObjectName("Btn4_2")
        self.Btn5_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn5_1.setGeometry(QtCore.QRect(350, 350, 350, 175))
        self.Btn5_1.setObjectName("Btn5_1")
        self.Btn5_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn5_2.setGeometry(QtCore.QRect(350, 525, 350, 175))
        self.Btn5_2.setObjectName("Btn5_2")
        self.Btn6_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn6_1.setGeometry(QtCore.QRect(700, 350, 350, 175))
        self.Btn6_1.setObjectName("Btn6_1")
        self.Btn6_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn6_2.setGeometry(QtCore.QRect(700, 525, 350, 175))
        self.Btn6_2.setObjectName("Btn6_2")
        self.Btn7_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn7_1.setGeometry(QtCore.QRect(0, 700, 350, 175))
        self.Btn7_1.setObjectName("Btn7_1")
        self.Btn7_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn7_2.setGeometry(QtCore.QRect(0, 875, 350, 175))
        self.Btn7_2.setObjectName("Btn7_2")
        self.Btn8_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn8_1.setGeometry(QtCore.QRect(350, 700, 350, 175))
        self.Btn8_1.setObjectName("Btn8_1")
        self.Btn8_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn8_2.setGeometry(QtCore.QRect(350, 875, 350, 175))
        self.Btn8_2.setObjectName("Btn8_2")
        self.Btn9_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn9_1.setGeometry(QtCore.QRect(700, 700, 350, 175))
        self.Btn9_1.setObjectName("Btn9_1")
        self.Btn9_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn9_2.setGeometry(QtCore.QRect(700, 875, 350, 175))
        self.Btn9_2.setObjectName("Btn9_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Btn1_1.clicked.connect(self.display1_1)
        self.Btn1_2.clicked.connect(self.display1_2)
        self.Btn2_1.clicked.connect(self.display2_1)
        self.Btn2_2.clicked.connect(self.display2_2)
        self.Btn3_1.clicked.connect(self.display3_1)
        self.Btn3_2.clicked.connect(self.display3_2)
        self.Btn4_1.clicked.connect(self.display4_1)
        self.Btn4_2.clicked.connect(self.display4_2)
        self.Btn5_1.clicked.connect(self.display5_1)
        self.Btn5_2.clicked.connect(self.display5_2)
        self.Btn6_1.clicked.connect(self.display6_1)
        self.Btn6_2.clicked.connect(self.display6_2)
        self.Btn7_1.clicked.connect(self.display7_1)
        self.Btn7_2.clicked.connect(self.display7_2)
        self.Btn8_1.clicked.connect(self.display8_1)
        self.Btn8_2.clicked.connect(self.display8_2)
        self.Btn9_1.clicked.connect(self.display9_1)
        self.Btn9_2.clicked.connect(self.display9_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DOAS MEDIA"))
        self.Btn1_1.setText(_translate("MainWindow", "Let go of dreams"))
        self.Btn1_2.setText(_translate("MainWindow", "Pursue dreams"))
        self.Btn2_1.setText(_translate("MainWindow", "Call her"))
        self.Btn2_2.setText(_translate("MainWindow", "Don't call"))
        self.Btn3_1.setText(_translate("MainWindow", "Sell the ovens"))
        self.Btn3_2.setText(_translate("MainWindow", "Don't sell"))
        self.Btn4_1.setText(_translate("MainWindow", "Change the orders"))
        self.Btn4_2.setText(_translate("MainWindow", "Help Charles"))
        self.Btn5_1.setText(_translate("MainWindow", "Don't give the money"))
        self.Btn5_2.setText(_translate("MainWindow", "Give the money"))
        self.Btn6_1.setText(_translate("MainWindow", "Continue treatment"))
        self.Btn6_2.setText(_translate("MainWindow", "Give up kids"))
        self.Btn7_1.setText(_translate("MainWindow", "Ignore them"))
        self.Btn7_2.setText(_translate("MainWindow", "Replace it"))
        self.Btn8_1.setText(_translate("MainWindow", "Don't talk to parents"))
        self.Btn8_2.setText(_translate("MainWindow", "Talk to parents"))
        self.Btn9_1.setText(_translate("MainWindow", "Lie to him"))
        self.Btn9_2.setText(_translate("MainWindow", "Tell the truth"))

    def display1_1(self):
        pixmap = QtGui.QPixmap('ah1.PNG').scaled(self.pic1.width(), self.pic1.height(), QtCore.Qt.KeepAspectRatio)
        self.pic1.setPixmap(pixmap)
        self.Btn1_1.deleteLater()
        self.Btn1_2.deleteLater()

    def display1_2(self):
        pixmap = QtGui.QPixmap('th1.PNG').scaled(self.pic1.width(), self.pic1.height(), QtCore.Qt.KeepAspectRatio)
        self.pic1.setPixmap(pixmap)
        self.Btn1_1.deleteLater()
        self.Btn1_2.deleteLater()

    def display2_1(self):
        pixmap = QtGui.QPixmap('ah2.PNG').scaled(self.pic2.width(), self.pic2.height(), QtCore.Qt.KeepAspectRatio)
        self.pic2.setPixmap(pixmap)
        self.Btn2_1.deleteLater()
        self.Btn2_2.deleteLater()

    def display2_2(self):
        pixmap = QtGui.QPixmap('th2.PNG').scaled(self.pic2.width(), self.pic2.height(), QtCore.Qt.KeepAspectRatio)
        self.pic2.setPixmap(pixmap)
        self.Btn2_1.deleteLater()
        self.Btn2_2.deleteLater()

    def display3_1(self):
        pixmap = QtGui.QPixmap('ah3.PNG').scaled(self.pic3.width(), self.pic3.height(), QtCore.Qt.KeepAspectRatio)
        self.pic3.setPixmap(pixmap)
        self.Btn3_1.deleteLater()
        self.Btn3_2.deleteLater()

    def display3_2(self):
        pixmap = QtGui.QPixmap('th3.PNG').scaled(self.pic3.width(), self.pic3.height(), QtCore.Qt.KeepAspectRatio)
        self.pic3.setPixmap(pixmap)
        self.Btn3_1.deleteLater()
        self.Btn3_2.deleteLater()

    def display4_1(self):
        pixmap = QtGui.QPixmap('ah4.PNG').scaled(self.pic4.width(), self.pic4.height(), QtCore.Qt.KeepAspectRatio)
        self.pic4.setPixmap(pixmap)
        self.Btn4_1.deleteLater()
        self.Btn4_2.deleteLater()

    def display4_2(self):
        pixmap = QtGui.QPixmap('th4.PNG').scaled(self.pic4.width(), self.pic4.height(), QtCore.Qt.KeepAspectRatio)
        self.pic4.setPixmap(pixmap)
        self.Btn4_1.deleteLater()
        self.Btn4_2.deleteLater()

    def display5_1(self):
        pixmap = QtGui.QPixmap('ah5.PNG').scaled(self.pic5.width(), self.pic5.height(), QtCore.Qt.KeepAspectRatio)
        self.pic5.setPixmap(pixmap)
        self.Btn5_1.deleteLater()
        self.Btn5_2.deleteLater()

    def display5_2(self):
        pixmap = QtGui.QPixmap('th5.PNG').scaled(self.pic5.width(), self.pic5.height(), QtCore.Qt.KeepAspectRatio)
        self.pic5.setPixmap(pixmap)
        self.Btn5_1.deleteLater()
        self.Btn5_2.deleteLater()

    def display6_1(self):
        pixmap = QtGui.QPixmap('ah6.PNG').scaled(self.pic6.width(), self.pic6.height(), QtCore.Qt.KeepAspectRatio)
        self.pic6.setPixmap(pixmap)
        self.Btn6_1.deleteLater()
        self.Btn6_2.deleteLater()

    def display6_2(self):
        pixmap = QtGui.QPixmap('th6.PNG').scaled(self.pic6.width(), self.pic6.height(), QtCore.Qt.KeepAspectRatio)
        self.pic6.setPixmap(pixmap)
        self.Btn6_1.deleteLater()
        self.Btn6_2.deleteLater()

    def display7_1(self):
        pixmap = QtGui.QPixmap('ah7.PNG').scaled(self.pic7.width(), self.pic7.height(), QtCore.Qt.KeepAspectRatio)
        self.pic7.setPixmap(pixmap)
        self.Btn7_1.deleteLater()
        self.Btn7_2.deleteLater()

    def display7_2(self):
        pixmap = QtGui.QPixmap('th7.PNG').scaled(self.pic7.width(), self.pic7.height(), QtCore.Qt.KeepAspectRatio)
        self.pic7.setPixmap(pixmap)
        self.Btn7_1.deleteLater()
        self.Btn7_2.deleteLater()

    def display8_1(self):
        pixmap = QtGui.QPixmap('ah8.PNG').scaled(self.pic8.width(), self.pic8.height(), QtCore.Qt.KeepAspectRatio)
        self.pic8.setPixmap(pixmap)
        self.Btn8_1.deleteLater()
        self.Btn8_2.deleteLater()

    def display8_2(self):
        pixmap = QtGui.QPixmap('th8.PNG').scaled(self.pic8.width(), self.pic8.height(), QtCore.Qt.KeepAspectRatio)
        self.pic8.setPixmap(pixmap)
        self.Btn8_1.deleteLater()
        self.Btn8_2.deleteLater()

    def display9_1(self):
        pixmap = QtGui.QPixmap('ah9.PNG').scaled(self.pic9.width(), self.pic9.height(), QtCore.Qt.KeepAspectRatio)
        self.pic9.setPixmap(pixmap)
        self.Btn9_1.deleteLater()
        self.Btn9_2.deleteLater()

    def display9_2(self):
        pixmap = QtGui.QPixmap('th9.PNG').scaled(self.pic9.width(), self.pic9.height(), QtCore.Qt.KeepAspectRatio)
        self.pic9.setPixmap(pixmap)
        self.Btn9_1.deleteLater()
        self.Btn9_2.deleteLater()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

