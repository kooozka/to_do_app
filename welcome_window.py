from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import sys
from login_window import Ui_LoginWindow
from add_user_window import Ui_AddUserWindow
from center_window import center

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 584)
        MainWindow.setStyleSheet(u"QWidget#MainWindow{\n"
"background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 70, 221, 51))
        font = QFont()
        font.setFamilies([u"MS Shell Dig 2"])
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 36pt \"MS Shell Dig 2\"; color: rgb(255, 255, 255)")
        self.loginPushButton = QPushButton(self.centralwidget, clicked = lambda: self.log_in_button_clicked(MainWindow))
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setGeometry(QRect(260, 230, 251, 41))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.loginPushButton.setFont(font1)
        self.loginPushButton.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 255, 255);\n"
"}")
        self.createPushButton = QPushButton(self.centralwidget, clicked = lambda: self.create_an_account_button_clicked(MainWindow))
        self.createPushButton.setObjectName(u"createPushButton")
        self.createPushButton.setGeometry(QRect(260, 310, 251, 41))
        self.createPushButton.setFont(font1)
        self.createPushButton.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 255, 255);\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 130, 341, 31))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dig 2"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"font: 16pt \"MS Shell Dig 2\"; color: rgb(255, 255, 255)")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        center(MainWindow)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.loginPushButton.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.createPushButton.setText(QCoreApplication.translate("MainWindow", u"Create an account", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sign in or create a new account", None))
    # retranslateUi

    def log_in_button_clicked(self, window):
        window.close()
        self.window = QMainWindow()
        self.ui = Ui_LoginWindow(self.create_an_account_button_clicked, self.welcome)
        self.ui.setupUi(self.window)
        self.window.show()
    
    def create_an_account_button_clicked(self, window):
        window.close()
        self.window = QMainWindow()
        self.ui = Ui_AddUserWindow(self.log_in_button_clicked, self.welcome)
        self.ui.setupUi(self.window)
        self.window.show()

    def welcome(self, window):
        window.close()
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def run():
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())
