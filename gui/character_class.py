from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QComboBox, QLabel, QLineEdit, QMessageBox
from gui.py import character
import os
import json
from pprint import pprint

class Character(QDialog):
    def __init__(self, res_class, res_race, db_character):
        super().__init__()
        self.ui = character.Ui_Dialog()
        self.ui.setupUi(self)

        # Initialization
        self.class_db = res_class
        self.races_db = res_race
        self.ui.class0.addItems(self.class_db.keys())
        self.ui.race.addItems(self.races_db.keys())
        self.class_filter()
        self.race_filter()

        self.save = False
        self.db_characters = db_character

        # Filtering Class / Race
        self.ui.race.currentTextChanged.connect(self.race_filter)
        self.ui.class0.currentTextChanged.connect(self.class_filter)

        # Saving / Closing 
        self.ui.buttonBox.accepted.connect(self.character_save)
        self.ui.buttonBox.rejected.connect(self.character_cancel)


    def character_save(self):
        """Save the data when Save is clicked and close the window."""
        new_char = self.copy_data()
        if list(new_char)[0] not in list(self.db_characters):
            self.db_characters.update(new_char)
        else:
            self.show_error_message(f"Value '{list(new_char)[0]}' already exists!")
        with open(os.path.join(os.getcwd(), "./res/db_characters.json"), "w") as outfile:
            json.dump(self.db_characters, outfile, indent=4)
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
        values = {}

        # Save QLabel values
        # labels = self.findChildren(QLabel)
        # for label in labels:
        #     values[label.objectName()] = label.text()

        # Save QComboBox values
        comboboxes = self.findChildren(QComboBox)
        for combobox in comboboxes:
            values[combobox.objectName()] = combobox.currentText()

        # Save QLine values
        lines = self.findChildren(QLineEdit)
        for line in lines:
            values[line.objectName()] = line.text()
            if line.objectName() == 'name':
                name = line.text()

        new_char = {name: values}
        return new_char
    

    def show_error_message(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()
        






        