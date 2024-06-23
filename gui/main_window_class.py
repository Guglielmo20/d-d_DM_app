from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from gui.py import main_window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

