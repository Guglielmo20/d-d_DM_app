from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
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

        self.ui.push_character_add.clicked.connect(self.select_fromlist)

        #self.ui.tableWidget.cellClicked()
        

    def update_list(self):
        self.ui.listCharacter.clear()
        self.ui.listCharacter.addItems([i for i in list(self.db_character)])


    def select_fromlist(self):
        # Read the current value from QlistQudget
        current = self.ui.listCharacter.currentItem()
        if current is not None:
            selected = current.text()
            self.add_totable(selected)
        else:
            self.show_error_message('Please select a character.')


    def add_totable(self, selected):
        # Write the current value in QTableWidget
        row_position = self.ui.tableWidget.rowCount()

        selected = selected
        armclass = self.db_character[selected]['armorerclass']
        lifepoints = self.db_character[selected]['maxhp']
        for char in [self.ui.tableWidget.item(row, 1).text() for row in range(self.ui.tableWidget.rowCount())]:
            if selected == char:
                self.show_error_message(f'{selected} is already selected.')
                return
        self.ui.tableWidget.insertRow(row_position)
        # Compile all the table
        self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem('-'))
        self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(selected))
        self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(lifepoints))
        self.ui.tableWidget.setItem(row_position, 3, QTableWidgetItem(armclass))


    def show_error_message(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()

        