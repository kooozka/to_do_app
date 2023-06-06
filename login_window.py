from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget, QMessageBox)
import data_manager, task_manager, datetime
#from to_do_app import Ui_MainWindow
from add_user_window import Ui_AddUserWindow
from center_window import center

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(800, 600)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 205, 81, 21))
        font = QFont()
        font.setFamilies([u"MS Shell Dig2"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.usernameLineEdit = QLineEdit(self.centralwidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(240, 220, 301, 41))
        self.usernameLineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 70, 131, 61))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dig 2"])
        font1.setPointSize(36)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font: 36pt \"MS Shell Dig 2\"; color: rgb(255, 255, 255)")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 140, 341, 31))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dig 2"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"font: 16pt \"MS Shell Dig 2\"; color: rgb(255, 255, 255)")
        self.passwordLineEdit = QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(240, 300, 301, 41))
        self.passwordLineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.centralwidget, clicked = lambda: self.log_in_button_clicked(LoginWindow))
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 370, 301, 41))
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
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 280, 81, 31))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.createAccountPushButton = QPushButton(self.centralwidget, clicked = lambda: self.createAccountPushButton(LoginWindow))
        self.createAccountPushButton.setObjectName(u"createAccountPushButton")
        self.createAccountPushButton.setGeometry(QRect(240, 460, 301, 41))
        self.createAccountPushButton.setStyleSheet(u"QPushButton {\n"
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
        self.label_2.setGeometry(QRect(280, 430, 221, 17))
        self.label_2.setStyleSheet(u"font: 12pt \"MS Shell Dig 2\"; color: rgb(255, 255, 255)")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"Sign in to your existing account", None))
        self.pushButton.setText(QCoreApplication.translate("LoginWindow", u"Log in", None))
        self.label_5.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.createAccountPushButton.setText(QCoreApplication.translate("LoginWindow", u"Create a new account", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Don't have an account yet?", None))
    # retranslateUi

    def show_incoming_task(self):
        errorDialog = QMessageBox()
        errorDialog.setWindowTitle("Information")
        taskManager = task_manager.TaskManager()
        taskManager.add_tasks(data_manager.get_user_tasks(self.usernameLineEdit.text()))
        nearest_task = taskManager.get_tasks_sorted_by_deadline()[0]
        deadline = datetime.datetime.strptime(nearest_task.deadline, "%Y-%m-%d %H:%M:%S")
        time_difference = (deadline - datetime.datetime.now()).total_seconds()
        if time_difference > 0:
            errorDialog.setText("Your incoming task " + nearest_task.title + " deadline in: " + str(time_difference/3600) + " hours")
        else:
            errorDialog.setText("Your task " + nearest_task.title + " finished " + str(round(abs(time_difference/3600), 2)) + " hours ago")
        errorDialog.setStandardButtons(QMessageBox.Ok)
        errorDialog.setDefaultButton(QMessageBox.Ok)
        errorDialog.exec()  

    def log_in_button_clicked(self, window):
        print(data_manager.login_success(self.usernameLineEdit.text(), self.passwordLineEdit.text()))
        if data_manager.login_success(self.usernameLineEdit.text(), self.passwordLineEdit.text()):
            window.close()
            self.window = QMainWindow()
            #self.ui = Ui_MainWindow(self.usernameLineEdit.text(), self.show_incoming_task)
            self.ui.setupUi(self.window)
            self.window.show()
            self.show_incoming_task()
        elif not self.usernameLineEdit.text() or not self.passwordLineEdit.text():
            errorDialog = QMessageBox()
            errorDialog.setWindowTitle("Error")
            errorDialog.setText("Fulfill all the data")
            errorDialog.setStandardButtons(QMessageBox.Ok)
            errorDialog.setDefaultButton(QMessageBox.Ok)
            errorDialog.exec()
        else:
            errorDialog = QMessageBox()
            errorDialog.setWindowTitle("Error")
            errorDialog.setText("Incorrect username or password")
            errorDialog.setStandardButtons(QMessageBox.Ok)
            errorDialog.setDefaultButton(QMessageBox.Ok)
            errorDialog.exec()

    def create_an_account_button_clicked(self, window):
        window.close()
        self.window = QMainWindow()
        self.ui = Ui_AddUserWindow()
        self.ui.setupUi(self.window)
        self.window.show()