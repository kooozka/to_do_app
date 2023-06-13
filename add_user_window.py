from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget, QMessageBox)
from to_do_app_window import Ui_MainWindow
import data_manager, sqlite3
from center_window import center

class Ui_AddUserWindow(object):
    def __init__(self, login_window, welcome) -> None:
        self.login_window = login_window
        self.welcome = welcome
    def setupUi(self, AddUserWindow):
        if not AddUserWindow.objectName():
            AddUserWindow.setObjectName(u"AddUserWindow")
        AddUserWindow.resize(800, 647)
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
        self.usernameLineEdit.setGeometry(QRect(240, 210, 301, 41))
        self.usernameLineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.passwordLineEdit = QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(240, 290, 301, 41))
        self.passwordLineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.confirmPasswordLineEdit = QLineEdit(self.centralwidget)
        self.confirmPasswordLineEdit.setObjectName(u"confirmPasswordLineEdit")
        self.confirmPasswordLineEdit.setGeometry(QRect(240, 370, 301, 41))
        self.confirmPasswordLineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.confirmPasswordLineEdit.setEchoMode(QLineEdit.Password)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 190, 81, 31))
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
        self.label_5.setGeometry(QRect(240, 270, 81, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 350, 121, 31))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.pushButton = QPushButton(self.centralwidget, clicked = lambda: self.add_user(AddUserWindow))
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 460, 301, 41))
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
        self.errorLabel = QLabel(self.centralwidget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(240, 420, 301, 21))
        self.errorLabel.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\"; color: red;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 510, 301, 31))
        self.label_4.setStyleSheet(u"font: 11pt \"MS Shell Dig 2\"; color: rgb(255, 255, 255)")
        self.pushButton_2 = QPushButton(self.centralwidget, clicked = lambda: self.login_window(AddUserWindow))
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(239, 550, 301, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(180, 255, 255);\n"
"}")
        AddUserWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(AddUserWindow)
        self.statusbar.setObjectName(u"statusbar")
        AddUserWindow.setStatusBar(self.statusbar)

        center(AddUserWindow)

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
        self.errorLabel.setText("")
        self.label_4.setText(QCoreApplication.translate("AddUserWindow", u"Or log in if you already have an account", None))
        self.pushButton_2.setText(QCoreApplication.translate("AddUserWindow", u"Log in", None))
    # retranslateUi

    def add_user(self, window):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        confirmedPassword = self.confirmPasswordLineEdit.text()
        if not username or not password or not confirmedPassword:
            self.errorLabel.setText("Fulfill all the data")
        elif self.passwordLineEdit.text() == self.confirmPasswordLineEdit.text():
            try:
                data_manager.add_user(username, password)
                window.close()
                self.window = QMainWindow()
                self.ui = Ui_MainWindow(self.usernameLineEdit.text(), self.welcome)
                self.ui.setupUi(self.window)
                self.window.show()
            except(sqlite3.IntegrityError):
                self.errorLabel.setText("Such a user already exists")
        else:
            self.errorLabel.setText("Given passwords differ")


