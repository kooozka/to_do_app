from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QStringListModel)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget, QDialogButtonBox)
import logic.task_manager as task_manager, logic.data_manager as data_manager, datetime
from add_task_window import Ui_AddTaskWindow
from edit_task_window import Ui_EditTaskWindow
from center_window import center

class Ui_MainWindow(object):
    def __init__(self, username, login_window) -> None:
        self.username = username
        self.login_window = login_window
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(990, 711)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(40, 120, 531, 431))
        font = QFont()
        font.setFamilies([u"MS Shell Dig 2"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.listView.setFont(font)
        self.listView.setStyleSheet(u"QListView {\n"
"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);\n"
"}\n"
"QListView::item:hover {\n"
"background-color: rgb(200, 255, 255);\n"
"}\n"
"QListView::item:selected {\n"
"background-color: rgb(170, 255, 255);\n"
"}")


        self.previousButton = QPushButton(self.centralwidget, clicked = lambda: self.previous_task())
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.setGeometry(QRect(40, 620, 111, 41))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.previousButton.setFont(font1)
        self.previousButton.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 255, 255);\n"
"}")
        self.nextButton = QPushButton(self.centralwidget, clicked = lambda: self.next_task())
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(840, 620, 111, 41))
        self.nextButton.setFont(font1)
        self.nextButton.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 255, 255);\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 30, 231, 51))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dig 2"])
        font2.setPointSize(36)
        font2.setBold(False)
        font2.setItalic(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"font: 36pt \"MS Shell Dig 2\"; color: rgb(255, 255, 255)")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(110, 90, 101, 25))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);\n")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 90, 61, 21))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dig 2"])
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"font: 13pt \"MS Shell Dig 2\"; color: rgb(255, 255, 255)")
        self.addButton = QPushButton(self.centralwidget, clicked = lambda: self.add_button_clicked())
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(350, 560, 61, 41))
        self.addButton.setFont(font1)
        self.addButton.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 255, 255);\n"
"}")
        self.removeButton = QPushButton(self.centralwidget, clicked = lambda: self.remove_button_clicked())
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setGeometry(QRect(510, 560, 61, 41))
        self.removeButton.setFont(font1)
        self.removeButton.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 255, 255);\n"
"}")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(596, 120, 20, 441))
        self.line.setStyleSheet(u"color: rgb(170, 255, 255);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.titleTextBrowser = QTextBrowser(self.centralwidget)
        self.titleTextBrowser.setObjectName(u"titleTextBrowser")
        self.titleTextBrowser.setGeometry(QRect(650, 130, 301, 41))
        self.titleTextBrowser.setFont(font)
        self.titleTextBrowser.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.descriptionTextBrowser = QTextBrowser(self.centralwidget)
        self.descriptionTextBrowser.setObjectName(u"descriptionTextBrowser")
        self.descriptionTextBrowser.setGeometry(QRect(650, 210, 301, 101))
        self.descriptionTextBrowser.setFont(font)
        self.descriptionTextBrowser.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.priorityTextBrowser = QTextBrowser(self.centralwidget)
        self.priorityTextBrowser.setObjectName(u"priorityTextBrowser")
        self.priorityTextBrowser.setGeometry(QRect(650, 350, 301, 41))
        self.priorityTextBrowser.setFont(font)
        self.priorityTextBrowser.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.deadlineTextBrowser = QTextBrowser(self.centralwidget)
        self.deadlineTextBrowser.setObjectName(u"deadlineTextBrowser")
        self.deadlineTextBrowser.setGeometry(QRect(650, 430, 301, 41))
        self.deadlineTextBrowser.setFont(font)
        self.deadlineTextBrowser.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.categoryTextBrowser = QTextBrowser(self.centralwidget)
        self.categoryTextBrowser.setObjectName(u"categoryTextBrowser")
        self.categoryTextBrowser.setGeometry(QRect(650, 510, 301, 41))
        self.categoryTextBrowser.setFont(font)
        self.categoryTextBrowser.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dig 2\";\n"
"color: rgb(0,0,0);")
        self.editPushButton = QPushButton(self.centralwidget, clicked = lambda: self.edit_button_clicked())
        self.editPushButton.setObjectName(u"editPushButton")
        self.editPushButton.setGeometry(QRect(430, 560, 61, 41))
        font4 = QFont()
        font4.setFamilies([u"MS Shell Dlg 2"])
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        self.editPushButton.setFont(font4)
        self.editPushButton.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 255, 255);\n"
"}")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(649, 110, 81, 21))
        font5 = QFont()
        font5.setFamilies([u"MS Shell Dig2"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(649, 190, 81, 21))
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(649, 330, 81, 21))
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(649, 410, 81, 21))
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(649, 490, 81, 21))
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"font: 10pt \"MS Shell Dig2\";\n"
"color: rgb(0,0,0);")
        self.logOutPushButton = QPushButton(self.centralwidget, clicked = lambda: self.login_window(MainWindow))
        self.logOutPushButton.setObjectName(u"logOutPushButton")
        self.logOutPushButton.setGeometry(QRect(890, 30, 61, 41))
        self.logOutPushButton.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 255, 255);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        center(MainWindow)
        self.get_tasks()
        self.listView.clicked.connect(self.fulfill_task_data)
        self.comboBox.currentIndexChanged.connect(self.get_tasks)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.previousButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ToDo App", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Deadline", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Priority", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sort by:", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"\u271a", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"\u2718", None))
        self.editPushButton.setText(QCoreApplication.translate("MainWindow", u"\u270e", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Priority", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Deadline", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.logOutPushButton.setText(QCoreApplication.translate("MainWindow", u"\u23cf", None))
    # retranslateUi

    def get_sorted_tasks(self, sorting_method):
        taskManager = task_manager.TaskManager()
        taskManager.add_tasks(data_manager.get_user_tasks(self.username))
        if sorting_method == "Priority":
            tasks = taskManager.get_tasks_sorted_by_priority()
        else:
            tasks = taskManager.get_tasks_sorted_by_deadline()
        return tasks
    
    def get_tasks(self):
        tasks = self.get_sorted_tasks(self.comboBox.currentText())
        tasks = [str(task) for task in tasks]
        self.listView.setModel(QStringListModel(tasks))

    def fulfill_task_data(self, index):
        taskManager = task_manager.TaskManager()
        taskManager.add_tasks(data_manager.get_user_tasks(self.username))
        current_sorting_method = self.comboBox.currentText()
        if current_sorting_method == "Deadline":
            tasks = taskManager.get_tasks_sorted_by_deadline()
            task = tasks[index.row()]
        else:
            tasks = taskManager.get_tasks_sorted_by_priority()
        task = tasks[index.row()]
        self.titleTextBrowser.setText(task.title)
        self.descriptionTextBrowser.setText(task.description)
        self.categoryTextBrowser.setText(task.category.name)
        self.deadlineTextBrowser.setText(str(task.deadline))
        self.priorityTextBrowser.setText(task.priority.name)
        self.check_previous_button()
        self.check_next_button()

    def next_task(self):
        currentIndex = self.listView.currentIndex()
        row = currentIndex.row()
        column = currentIndex.column()
        nextIndex = self.listView.model().index(row + 1, column)
        self.listView.setCurrentIndex(nextIndex)
        self.fulfill_task_data(nextIndex)

    def previous_task(self):
        currentIndex = self.listView.currentIndex()
        row = currentIndex.row()
        column = currentIndex.column()
        previousIndex = self.listView.model().index(row - 1, column)
        self.listView.setCurrentIndex(previousIndex)
        self.fulfill_task_data(previousIndex)

    def check_previous_button(self):
        if self.listView.currentIndex().row() == 0:
            self.previousButton.setEnabled(False)
        else:
            self.previousButton.setEnabled(True)

    def check_next_button(self):
        if self.listView.currentIndex().row() == self.listView.model().rowCount() - 1:
            self.nextButton.setEnabled(False)
        else:
            self.nextButton.setEnabled(True)

    def add_button_clicked(self):
        self.window = QMainWindow()
        self.ui = Ui_AddTaskWindow(self.get_tasks, self.username)
        self.ui.setupUi(self.window)
        self.window.show()

    def remove_button_clicked(self):
        taskManager = task_manager.TaskManager()
        taskManager.add_tasks(data_manager.get_user_tasks(self.username))
        current_sorting_method = self.comboBox.currentText()
        print(current_sorting_method)
        if current_sorting_method == "Priority":
            tasks = taskManager.get_tasks_sorted_by_priority()
        else:
            tasks = taskManager.get_tasks_sorted_by_deadline()
        data_manager.remove_task(tasks[self.listView.currentIndex().row()].task_id)
        self.get_tasks()

    def edit_button_clicked(self):
        current_sorting_method = self.comboBox.currentText()
        tasks = self.get_sorted_tasks(current_sorting_method)
        self.window = QMainWindow()
        self.ui = Ui_EditTaskWindow(tasks[self.listView.currentIndex().row()].task_id, self.titleTextBrowser.toPlainText(), self.descriptionTextBrowser.toPlainText(), self.deadlineTextBrowser.toPlainText(), self.categoryTextBrowser.toPlainText(), self.priorityTextBrowser.toPlainText(), self.username, self.get_tasks)
        self.ui.setupUi(self.window)
        self.window.show()    
