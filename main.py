from PyQt6 import QtWidgets
import sys

from PyQt6.QtWidgets import QApplication
import mainWindow
import bomb

class Window:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = mainWindow.Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.ui.createBomb_btn.clicked.connect(self.button_clicked)
        self.ui.strike_btn.clicked.connect(self.strike_clicked)
        
    
    def strike_clicked(self):
        self.ui.strikes_lcdNumber.display() # TODO Work out how the bomb object will interact with this
        pass
    
    def button_clicked(self): # TODO close the window and open the bomb one
        # self.main_window.close()
        windowBomb = bomb.bombWindow()
        windowBomb.main_window.show()
        
        
    
    



if __name__ == "__main__":
    window = Window()
    window.main_window.show()
    sys.exit(window.app.exec())


