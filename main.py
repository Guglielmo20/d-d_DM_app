import sys, os
sys.path.extend(["gui", "gui/py", os.path.join(os.path.dirname(os.path.abspath(__file__)), "gui", "gui/py")])
from PyQt5.QtWidgets import QApplication
from gui import login_class

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = login_class.Login()
    sys.exit(app.exec_())