# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 50, 451, 621))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.exportAnswerButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.exportAnswerButton.setObjectName("exportAnswerButton")
        self.gridLayout.addWidget(self.exportAnswerButton, 5, 2, 1, 1)
        self.getAnswerButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.getAnswerButton.setObjectName("getAnswerButton")
        self.gridLayout.addWidget(self.getAnswerButton, 4, 2, 1, 1)
        self.getQuestionButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.getQuestionButton.setToolTipDuration(4)
        self.getQuestionButton.setObjectName("getQuestionButton")
        self.gridLayout.addWidget(self.getQuestionButton, 4, 1, 1, 1)
        self.questionTextEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.questionTextEdit.setReadOnly(True)
        self.questionTextEdit.setObjectName("questionTextEdit")
        self.gridLayout.addWidget(self.questionTextEdit, 3, 1, 1, 1)
        self.exportQuestionButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.exportQuestionButton.setObjectName("exportQuestionButton")
        self.gridLayout.addWidget(self.exportQuestionButton, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.answerTextEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.answerTextEdit.setReadOnly(True)
        self.answerTextEdit.setObjectName("answerTextEdit")
        self.gridLayout.addWidget(self.answerTextEdit, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 30, 158, 52))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(650, 170, 71, 41))
        self.label_4.setObjectName("label_4")
        self.numberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numberLineEdit.setGeometry(QtCore.QRect(750, 180, 121, 21))
        self.numberLineEdit.setObjectName("numberLineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(650, 100, 131, 31))
        self.checkBox.setObjectName("checkBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(650, 240, 161, 31))
        self.label_5.setObjectName("label_5")
        self.rangeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rangeLineEdit.setGeometry(QtCore.QRect(820, 240, 51, 21))
        self.rangeLineEdit.setObjectName("rangeLineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小学四则运算出题工具"))
        self.label.setText(_translate("MainWindow", "题目："))
        self.exportAnswerButton.setText(_translate("MainWindow", "导出参考答案"))
        self.getAnswerButton.setText(_translate("MainWindow", "显示参考答案"))
        self.getQuestionButton.setText(_translate("MainWindow", "出题"))
        self.exportQuestionButton.setText(_translate("MainWindow", "导出题目"))
        self.label_2.setText(_translate("MainWindow", "参考答案："))
        self.label_3.setText(_translate("MainWindow", "设置"))
        self.label_4.setText(_translate("MainWindow", "出题数量\n"
"(默认300)"))
        self.numberLineEdit.setText(_translate("MainWindow", "300"))
        self.checkBox.setText(_translate("MainWindow", "除法有余数"))
        self.label_5.setText(_translate("MainWindow", "运算数范围        0 -\n"
"(默认100)"))
        self.rangeLineEdit.setText(_translate("MainWindow", "100"))

