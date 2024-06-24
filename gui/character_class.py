from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QComboBox
from gui.py import character
import os
import json

class Character(QDialog):
    def __init__(self, res_class, res_race):
        super().__init__()
        self.ui = character.Ui_Dialog()
        self.ui.setupUi(self)

        # Initialization
        self.class_db = res_class
        self.races_db = res_race
        self.ui.race.addItems(self.races_db.keys())
        self.ui.class0.addItems(self.class_db.keys())
        self.save = False

        self.db_characters = {}


    
        # Filtering Class / Race
        self.ui.race.currentTextChanged.connect(self.race_filter)
        self.ui.class0.currentTextChanged.connect(self.class_filter)

        # Saving / Closing 
        self.ui.buttonBox.accepted.connect(self.character_save)
        self.ui.buttonBox.rejected.connect(self.character_cancel)


    def character_save(self):
        """Save the data when Save is clicked and close the window."""
        self.db_characters = self.copy_data()
        self.save = True
        self.close()

    def character_cancel(self):
        """Close the window without saving."""
        self.save = False
        self.close()

    def closeEvent(self, event):
        """ Managing the X button click """
        pass

    def race_filter(self):
        """ Filter the sub-races according to the selected character race."""
        selected_race = self.ui.race.currentText()
        self.ui.subrace.clear()
        self.ui.subrace.addItems(self.races_db[selected_race]['subrace'])

    def class_filter(self):
        """ Filter the sub-class according to the selected character class."""
        selected_class = self.ui.class0.currentText()
        self.ui.subclass.clear()
        self.ui.subclass.addItems(self.class_db[selected_class]['subclass'])

    def copy_data(self):
        saved = {}
        list_save = ['group', 'subgroup', 'name', 'level', 
                     'race', 'subrace', 'class0', 'subclass',
                     'maxhp', 'maxhp_2', 'armorerclass', 'velocity',
                     'strenght', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        

        all_objects = self.findChildren(QDialog)
        print(all_objects)
        # Print all child widgets
        for obj in all_objects:
            print(obj)






        