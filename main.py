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
        self.ui.createBomb_btn.clicked.connect(self.button_clicked)
    
    def button_clicked(self):
        self.main_window.close()
        
    
    



if __name__ == "__main__":
    window = Window()
    window.main_window.show()
    sys.exit(window.app.exec())


