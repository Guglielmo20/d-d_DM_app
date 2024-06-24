from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog
from gui.py import character

class Character(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = character.Ui_Dialog()
        self.ui.setupUi(self)


