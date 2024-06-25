from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from gui.py import login
from gui import main_window_class
import json
import os

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = login.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Loading resources
        self.load_resources()

        # Instance and launch of main window
        self.main_window = main_window_class.MainWindow(self.res_dict)
        self.ui.pushButton_3.clicked.connect(self.launch_application)

    def launch_application(self):
        self.main_window.show()
        self.close()

    def load_resources(self):
        with open(os.path.abspath(os.path.join(os.getcwd(), './res/races_subraces.json'))) as f:
            races_db = json.load(f)
        
        with open(os.path.abspath(os.path.join(os.getcwd(), './res/classes_subclasses.json'))) as f:
            class_db = json.load(f)

        with open(os.path.abspath(os.path.join(os.getcwd(), './res/db_characters.json'))) as f:
            db_characters = json.load(f)

        self.res_dict = {'classes': class_db,
                         'races': races_db,
                         'characters': db_characters}


