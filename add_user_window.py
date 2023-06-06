# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddUserWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_AddUserWindow(object):
    def setupUi(self, AddUserWindow):
        if not AddUserWindow.objectName():
            AddUserWindow.setObjectName(u"AddUserWindow")
        AddUserWindow.resize(800, 600)
        self.centralwidget = QWidget(AddUserWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 80, 331, 41))
        font = QFont()
        font.setFamilies([u"MS Shell Dig 2"])
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 36pt \"MS Shell Dig 2\"; color: rgb(255, 255, 255)")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 140, 171, 31))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dig 2"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font: 16pt \"MS Shell Dig 2\"; color: rgb(255, 255, 255)")
        self.usernameLineEdit = QLineEdit(self.centralwidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(240, 220, 301, 41))
        self.usernameLineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.passwordLineEdit = QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(240, 300, 301, 41))
        self.passwordLineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.confirmPasswordLineEdit = QLineEdit(self.centralwidget)
        self.confirmPasswordLineEdit.setObjectName(u"confirmPasswordLineEdit")
        self.confirmPasswordLineEdit.setGeometry(QRect(240, 380, 301, 41))
        self.confirmPasswordLineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 200, 81, 31))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dig2"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 280, 81, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 360, 121, 31))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 450, 301, 41))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 255, 255);\n"
"}")
        AddUserWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(AddUserWindow)
        self.statusbar.setObjectName(u"statusbar")
        AddUserWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddUserWindow)

        QMetaObject.connectSlotsByName(AddUserWindow)
    # setupUi

    def retranslateUi(self, AddUserWindow):
        AddUserWindow.setWindowTitle(QCoreApplication.translate("AddUserWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AddUserWindow", u"Add new user", None))
        self.label_2.setText(QCoreApplication.translate("AddUserWindow", u"Input your data", None))
        self.usernameLineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("AddUserWindow", u"Username", None))
        self.label_5.setText(QCoreApplication.translate("AddUserWindow", u"Password", None))
        self.label_6.setText(QCoreApplication.translate("AddUserWindow", u"Confirm password", None))
        self.pushButton.setText(QCoreApplication.translate("AddUserWindow", u"Create an account", None))
    # retranslateUi

