from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget, QMessageBox)

import task_manager, data_manager, datetime

class Ui_AddTaskWindow(object):
    def __init__(self, callback, username) -> None:
        self.callback = callback
        self.username = username
    def setupUi(self, AddTaskWindow):
        if not AddTaskWindow.objectName():
            AddTaskWindow.setObjectName(u"AddTaskWindow")
        AddTaskWindow.resize(509, 620)
        self.centralwidget = QWidget(AddTaskWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.titleLineEdit = QLineEdit(self.centralwidget)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(120, 60, 271, 41))
        font = QFont()
        font.setFamilies([u"MS Shell Dig 2"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.titleLineEdit.setFont(font)
        self.titleLineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.priorityComboBox = QComboBox(self.centralwidget)
        self.priorityComboBox.setObjectName(u"priorityComboBox")
        self.priorityComboBox.setGeometry(QRect(120, 280, 271, 41))
        self.priorityComboBox.setFont(font)
        self.priorityComboBox.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(120, 360, 271, 41))
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.categoryComboBox = QComboBox(self.centralwidget)
        self.categoryComboBox.setObjectName(u"categoryComboBox")
        self.categoryComboBox.setGeometry(QRect(120, 440, 271, 41))
        self.categoryComboBox.setFont(font)
        self.categoryComboBox.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.pushButton = QPushButton(self.centralwidget, clicked = lambda: self.get_task_data(AddTaskWindow))
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 510, 141, 41))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 255, 255);\n"
"}")
        self.descriptionTextEdit = QTextEdit(self.centralwidget)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setGeometry(QRect(120, 140, 271, 101))
        self.descriptionTextEdit.setFont(font)
        self.descriptionTextEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 40, 81, 21))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dig2"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(120, 120, 81, 21))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(120, 260, 81, 21))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(120, 340, 81, 21))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(120, 420, 81, 21))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.errorLabel = QLabel(self.centralwidget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(120, 490, 271, 21))
        self.errorLabel.setStyleSheet(u"font: 12pt \"MS Shell Dig 2\";  color: red;")
        AddTaskWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(AddTaskWindow)
        self.statusbar.setObjectName(u"statusbar")
        AddTaskWindow.setStatusBar(self.statusbar)

        self.fulfill_comboboxes()
        self.datetime_settings()

        self.retranslateUi(AddTaskWindow)

        QMetaObject.connectSlotsByName(AddTaskWindow)
    # setupUi

    def retranslateUi(self, AddTaskWindow):
        AddTaskWindow.setWindowTitle(QCoreApplication.translate("AddTaskWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("AddTaskWindow", u"Add", None))
        self.label_8.setText(QCoreApplication.translate("AddTaskWindow", u"Title", None))
        self.label_9.setText(QCoreApplication.translate("AddTaskWindow", u"Description", None))
        self.label_10.setText(QCoreApplication.translate("AddTaskWindow", u"Priority", None))
        self.label_11.setText(QCoreApplication.translate("AddTaskWindow", u"Deadline", None))
        self.label_12.setText(QCoreApplication.translate("AddTaskWindow", u"Category", None))
    # retranslateUi
    def fulfill_comboboxes(self):
        for priority in task_manager.Priority:
            self.priorityComboBox.addItem(priority.name)

        for category in task_manager.Categories:
            self.categoryComboBox.addItem(category.name)

    def datetime_settings(self):
        current_datetime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(current_datetime)

        self.dateTimeEdit.setMinimumDateTime(current_datetime)

    def get_task_data(self, window):
        title = self.titleLineEdit.text()
        description = self.descriptionTextEdit.toPlainText()
        category = self.categoryComboBox.currentText()
        priority = self.priorityComboBox.currentText()
        deadline = self.dateTimeEdit.dateTime().toPython()
        deadline = deadline.strftime("%d-%m-%Y %H:%M")
        deadline = datetime.datetime.strptime(deadline, "%d-%m-%Y %H:%M")
        if not title or not description:
            self.errorLabel.setText("Fulfill all the data")
        else:    
            data_manager.add_task(title, task_manager.Categories[category].value, description, task_manager.Priority[priority].value, deadline, self.username)
            window.close()
            self.callback()    

