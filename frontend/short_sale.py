# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend/short_sale.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_code = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_code.setGeometry(QtCore.QRect(180, 30, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_code.setFont(font)
        self.lineEdit_code.setObjectName("lineEdit_code")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 20, 190, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_amount.setGeometry(QtCore.QRect(180, 90, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_amount.setFont(font)
        self.lineEdit_amount.setObjectName("lineEdit_amount")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 20, 190, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 100, 190, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 180, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_display = QtWidgets.QLabel(self.centralwidget)
        self.label_display.setGeometry(QtCore.QRect(60, 270, 711, 391))
        self.label_display.setText("")
        self.label_display.setObjectName("label_display")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 100, 190, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 180, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(MainWindow.flush)
        self.pushButton.clicked.connect(MainWindow.loan)
        self.pushButton_5.clicked.connect(MainWindow.closeout)
        self.pushButton_2.clicked.connect(MainWindow.sell)
        self.pushButton_3.clicked.connect(MainWindow.buy)
        self.pushButton_6.clicked.connect(MainWindow.save)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "股票代码："))
        self.pushButton.setText(_translate("MainWindow", "融券"))
        self.label_2.setText(_translate("MainWindow", "仓位：￥"))
        self.pushButton_2.setText(_translate("MainWindow", "卖出"))
        self.pushButton_3.setText(_translate("MainWindow", "买入"))
        self.pushButton_4.setText(_translate("MainWindow", "刷新"))
        self.pushButton_5.setText(_translate("MainWindow", "平仓"))
        self.pushButton_6.setText(_translate("MainWindow", "导出"))
