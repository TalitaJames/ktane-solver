from PyQt6 import QtWidgets
import sys

from PyQt6.QtWidgets import QApplication
import mainWindow 

class Window:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = mainWindow.Ui_MainWindow()
        self.ui.setupUi(self.main_window)
    
    
