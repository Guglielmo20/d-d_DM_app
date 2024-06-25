from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from gui.py import main_window
from gui import character_class

class MainWindow(QMainWindow):
    def __init__(self, res_dict):
        super().__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.classes_db = res_dict.get('classes')
        self.races_db = res_dict.get('races')
        self.db_character = res_dict.get('characters', {})

        self.ui.listCharacter.addItems([i for i in list(self.db_character)])

        # Instance and launch of main window
        self.character = character_class.Character(self.classes_db, self.races_db, self.db_character)
        self.ui.createNew.clicked.connect(self.character.show)
        # Update List
        self.ui.tabWidget.currentChanged.connect(self.update_list)
        

    def update_list(self):
        self.ui.listCharacter.clear()
        self.ui.listCharacter.addItems([i for i in list(self.db_character)])



