from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from gui.py import main_window
from gui import character_class

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)


        # Instance and launch of main window
        self.character = character_class.Character()
        self.ui.createNew.clicked.connect(self.character.show)
