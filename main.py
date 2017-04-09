# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from urllib import request
from PyQt5.QtGui import QDoubleValidator
import urllib.request, json
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 50, 61, 16))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(self.usdtobitcoin)
        self.textEdit.setValidator(QDoubleValidator(0.000001,99999.999999,6))

        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 60, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 60, 16))

        self.priceLabel = QtWidgets.QLabel(self.centralWidget)
        self.priceLabel.setGeometry(QtCore.QRect(400,10,200,100))
        self.priceLabel.setText("$ "+ str(self.bitcoinPriceGrab())+"/Bit")
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 170, 61, 16))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setValidator(QDoubleValidator(0.01, 999999.99, 2))

        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(140, 50, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_3.setGeometry(QtCore.QRect(180, 50, 61, 16))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.textChanged.connect(self.bitcointousd)
        self.textEdit_3.setReadOnly(True)


        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(250, 50, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(140, 170, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.textEdit_4 = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_4.setGeometry(QtCore.QRect(180, 170, 61, 16))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setReadOnly(True)


        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(250, 170, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.logopic = QtWidgets.QLabel(self.centralWidget)
        self.logopic.setGeometry(QtCore.QRect(280, 0, 111, 51))
        self.logopic.setText("")
        self.logopic.setPixmap(QtGui.QPixmap("/Users/zifengxia/Desktop/Logo2.png"))
        self.logopic.setScaledContents(True)
        self.logopic.setObjectName("logopic")
        self.buyBtn = QtWidgets.QPushButton(self.centralWidget)
        self.buyBtn.setGeometry(QtCore.QRect(70, 80, 81, 21))
        self.buyBtn.setObjectName("pushButton")
        #self.buyBtn.click().connect(self.buyBitCoin)

        self.priceLabel = QtWidgets.QLabel(self.centralWidget)
        self.priceLabel.setGeometry(QtCore.QRect(400,120,400,100))
        self.perUSD = round(1/self.bitcoinPriceGrab(),8)
        self.priceLabel.setText("$B"+ str(self.perUSD)+"/USD")

        self.sellBtn = QtWidgets.QPushButton(self.centralWidget)
        self.sellBtn.setGeometry(QtCore.QRect(70, 200, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.sellBtn.setFont(font)
        self.sellBtn.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuCapital_One_Cryptocurrency_Exchange = QtWidgets.QMenu(self.menuBar)
        self.menuCapital_One_Cryptocurrency_Exchange.setObjectName("menuCapital_One_Cryptocurrency_Exchange")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuCapital_One_Cryptocurrency_Exchange.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Amount "))
        self.label_2.setText(_translate("MainWindow", "USD -> BTC"))
        self.label_4.setText(_translate("MainWindow", "BTC -> USD"))
        self.label_5.setText(_translate("MainWindow", "Amount "))
        self.label_6.setText(_translate("MainWindow", "USD="))
        self.label_7.setText(_translate("MainWindow", "BTC"))
        self.label_8.setText(_translate("MainWindow", "BTC="))
        self.label_9.setText(_translate("MainWindow", "USD"))
        self.buyBtn.setText(_translate("MainWindow", "Buy"))
        self.sellBtn.setText(_translate("MainWindow", "Sell"))
        self.menuCapital_One_Cryptocurrency_Exchange.setTitle(_translate("MainWindow", "Capital One Cryptocurrency Exchange"))

    def usdtobitcoin(self):
        #set the bitcoin
        total = float(self.textEdit.text())/self.bitcoinPriceGrab()
        self.textEdit_3.setText(str(total))#put something in here
        print("USD to bitcoin")

    def bitcointousd(self):
        #set the bitcoin
        total = float(self.textEdit.text())*self.bitcoinPriceGrab()
        self.textEdit_4.setText(str(total))#put something in here
        print("bitcoin to USD")

    def bitcoinPriceGrab(self):
        with urllib.request.urlopen("https://blockchain.info/ticker") as url:
            data = json.loads(url.read().decode())

        return data['USD']['15m']
        total = float(self.textEdit2.text()) * self.bitcoinPriceGrab()
        self.textEdit_4.setText(str(total))  # put something in here




    def buyBitcoin(self):
        MainWindow.hide()
        #pass

    def sellBitcoin(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

