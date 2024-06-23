from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from gui.py import login
from gui import main_window_class

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = login.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()



        # Instance and launch of main window
        self.main_window = main_window_class.MainWindow()
        self.ui.pushButton_3.clicked.connect(self.main_window.show)


