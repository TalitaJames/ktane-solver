from hashlib import new
from PyQt6 import QtWidgets
import sys

from PyQt6.QtWidgets import QApplication
import bombCreatorWindow

class bombWindow:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = bombCreatorWindow.Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.ui.submit_btn.clicked.connect(self.submit_clicked)
        self.ui.parallelPort_checkBox.stateChanged.connect(self.parallel_clicked)
        
    
    def submit_clicked(self):
        serial = self.ui.serial_txt.toPlainText()
        battery = self.ui.battery_txt.toPlainText()
        lit = self.ui.lit_txt.toPlainText()
        parallel = self.ui.parallelPort_checkBox.isChecked()
        # self.main_window.close()
        
        newBomb = Bomb(serial, parallel, battery, lit)
        print(newBomb.__str__())
    
    def parallel_clicked(self):
        if self.ui.parallelPort_checkBox.isChecked():
            self.ui.parallelPort_checkBox.setText("Yes")
        else:
            self.ui.parallelPort_checkBox.setText("No")

class Bomb:
    def __init__(self, serialNum, parrallelPort, battery, Lit):
        self.serialNum = serialNum
        self.parrallelPort = parrallelPort
        self.battery = battery
        self.Lit = Lit
        self.strikeCount = 0
    
    def __str__(self):
        return "Bomb: serialNum: {}, parrallelPort: {}, Lit: {}, Strikes: {}".format(self.serialNum, self.parrallelPort, self.Lit, self.strikeCount)

    def __repr__(self):
        return self.__str__()
    
    def serialLastDigit(self):
        #True if last digit is even
        return self.serialNum[-1] % 2 ==0
    
    def serialContainsVowel(self):
        vowelCount = False
        for letter in self.serialNum:
            if letter in "aeiou":
                vowelCount = True
        return vowelCount
    
    def batteryCount(self):
        return self.battery
    
    def addStrike(self):
        self.strikeCount += 1
    
    def returnStrike(self):
        return self.strikeCount




if __name__ == "__main__":
    print("tester")
    window = bombWindow()
    window.main_window.show()
    sys.exit(window.app.exec())


