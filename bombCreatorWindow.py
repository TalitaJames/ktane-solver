# Form implementation generated from reading ui file 'bombCreatorWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.serial_lbl = QtWidgets.QLabel(self.centralwidget)
        self.serial_lbl.setGeometry(QtCore.QRect(30, 30, 220, 60))
        self.serial_lbl.setStyleSheet("font: 12pt \"OCR A Extended\";\n"
"background-color: rgb(247, 255, 160);")
        self.serial_lbl.setObjectName("serial_lbl")
        self.submit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.submit_btn.setGeometry(QtCore.QRect(620, 470, 151, 61))
        self.submit_btn.setStyleSheet("font: 12pt \"OCR A Extended\";")
        self.submit_btn.setObjectName("submit_btn")
        self.serial_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.serial_txt.setGeometry(QtCore.QRect(220, 30, 104, 60))
        self.serial_txt.setStyleSheet("font: 12pt \"OCR A Extended\";\n"
"background-color: rgb(247, 255, 160);")
        self.serial_txt.setObjectName("serial_txt")
        self.battery_lbl = QtWidgets.QLabel(self.centralwidget)
        self.battery_lbl.setGeometry(QtCore.QRect(30, 110, 220, 60))
        self.battery_lbl.setStyleSheet("font: 12pt \"OCR A Extended\";\n"
"background-color: rgb(212, 248, 255)")
        self.battery_lbl.setObjectName("battery_lbl")
        self.battery_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.battery_txt.setGeometry(QtCore.QRect(220, 110, 104, 60))
        self.battery_txt.setStyleSheet("font: 12pt \"OCR A Extended\";\n"
"background-color: rgb(212, 248, 255)")
        self.battery_txt.setObjectName("battery_txt")
        self.lit_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.lit_txt.setGeometry(QtCore.QRect(220, 190, 104, 60))
        self.lit_txt.setStyleSheet("font: 12pt \"OCR A Extended\";\n"
"background-color: rgb(255, 190, 196)")
        self.lit_txt.setObjectName("lit_txt")
        self.lit_lbl = QtWidgets.QLabel(self.centralwidget)
        self.lit_lbl.setGeometry(QtCore.QRect(30, 190, 220, 60))
        self.lit_lbl.setStyleSheet("font: 12pt \"OCR A Extended\";\n"
"background-color: rgb(255, 190, 196)")
        self.lit_lbl.setObjectName("lit_lbl")
        self.parallelPort_lbl = QtWidgets.QLabel(self.centralwidget)
        self.parallelPort_lbl.setGeometry(QtCore.QRect(30, 270, 291, 60))
        self.parallelPort_lbl.setStyleSheet("font: 12pt \"OCR A Extended\";\n"
"background-color: rgb(190, 255, 160);")
        self.parallelPort_lbl.setObjectName("parallelPort_lbl")
        self.parallelPort_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.parallelPort_checkBox.setGeometry(QtCore.QRect(240, 270, 81, 60))
        self.parallelPort_checkBox.setStyleSheet("font: 12pt \"OCR A Extended\";\n"
"background-color: rgb(190, 255, 160);")
        self.parallelPort_checkBox.setObjectName("parallelPort_checkBox")
        self.serial_lbl.raise_()
        self.submit_btn.raise_()
        self.serial_txt.raise_()
        self.battery_lbl.raise_()
        self.battery_txt.raise_()
        self.lit_lbl.raise_()
        self.lit_txt.raise_()
        self.parallelPort_lbl.raise_()
        self.parallelPort_checkBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.serial_lbl.setText(_translate("MainWindow", "Serial Number"))
        self.submit_btn.setText(_translate("MainWindow", "PushButton"))
        self.battery_lbl.setText(_translate("MainWindow", "Batteries"))
        self.lit_lbl.setText(_translate("MainWindow", "Lit Indicators"))
        self.parallelPort_lbl.setText(_translate("MainWindow", "Parallel port?"))
        self.parallelPort_checkBox.setText(_translate("MainWindow", "No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())