# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1236, 823)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.createBomb_btn = QtWidgets.QPushButton(self.centralwidget)
        self.createBomb_btn.setGeometry(QtCore.QRect(20, 10, 211, 61))
        self.createBomb_btn.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.createBomb_btn.setObjectName("createBomb_btn")
        self.strikes_lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.strikes_lcdNumber.setGeometry(QtCore.QRect(1130, 10, 41, 51))
        self.strikes_lcdNumber.setDigitCount(1)
        self.strikes_lcdNumber.setObjectName("strikes_lcdNumber")
        self.strikes_lbl = QtWidgets.QLabel(self.centralwidget)
        self.strikes_lbl.setGeometry(QtCore.QRect(1010, 10, 141, 51))
        self.strikes_lbl.setStyleSheet("font: 14pt \"OCR A Extended\";")
        self.strikes_lbl.setObjectName("strikes_lbl")
        self.strike_btn = QtWidgets.QPushButton(self.centralwidget)
        self.strike_btn.setGeometry(QtCore.QRect(1180, 20, 41, 41))
        self.strike_btn.setStyleSheet("font: 10pt \"OCR A Extended\";")
        self.strike_btn.setObjectName("strike_btn")
        self.modules_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.modules_tab.setGeometry(QtCore.QRect(20, 120, 1191, 651))
        self.modules_tab.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.modules_tab.setTabsClosable(False)
        self.modules_tab.setTabBarAutoHide(False)
        self.modules_tab.setObjectName("modules_tab")
        self.simpleWires_tab = QtWidgets.QWidget()
        self.simpleWires_tab.setObjectName("simpleWires_tab")
        self.wires_btn = QtWidgets.QPushButton(self.simpleWires_tab)
        self.wires_btn.setGeometry(QtCore.QRect(570, 280, 93, 71))
        self.wires_btn.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.wires_btn.setObjectName("wires_btn")
        self.wires_txt = QtWidgets.QTextEdit(self.simpleWires_tab)
        self.wires_txt.setGeometry(QtCore.QRect(350, 260, 171, 87))
        self.wires_txt.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.wires_txt.setObjectName("wires_txt")
        self.wiresAnswer_lbl = QtWidgets.QLabel(self.simpleWires_tab)
        self.wiresAnswer_lbl.setGeometry(QtCore.QRect(710, 230, 221, 141))
        self.wiresAnswer_lbl.setText("")
        self.wiresAnswer_lbl.setObjectName("wiresAnswer_lbl")
        self.colourchart_pic = QtWidgets.QLabel(self.simpleWires_tab)
        self.colourchart_pic.setGeometry(QtCore.QRect(60, 170, 231, 231))
        self.colourchart_pic.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.colourchart_pic.setObjectName("colourchart_pic")
        self.wiresWireframe_pic = QtWidgets.QLabel(self.simpleWires_tab)
        self.wiresWireframe_pic.setGeometry(QtCore.QRect(950, 10, 231, 231))
        self.wiresWireframe_pic.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.wiresWireframe_pic.setObjectName("wiresWireframe_pic")
        self.modules_tab.addTab(self.simpleWires_tab, "")
        self.button_tab = QtWidgets.QWidget()
        self.button_tab.setObjectName("button_tab")
        self.text_grp = QtWidgets.QGroupBox(self.button_tab)
        self.text_grp.setGeometry(QtCore.QRect(460, 70, 331, 441))
        self.text_grp.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"text-decoration: underline;")
        self.text_grp.setObjectName("text_grp")
        self.text_splitter = QtWidgets.QSplitter(self.text_grp)
        self.text_splitter.setGeometry(QtCore.QRect(0, 40, 241, 411))
        self.text_splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.text_splitter.setObjectName("text_splitter")
        self.txt_abort_rbtn = QtWidgets.QRadioButton(self.text_splitter)
        self.txt_abort_rbtn.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.txt_abort_rbtn.setObjectName("txt_abort_rbtn")
        self.txt_detonate_rbtn = QtWidgets.QRadioButton(self.text_splitter)
        self.txt_detonate_rbtn.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.txt_detonate_rbtn.setObjectName("txt_detonate_rbtn")
        self.txt_hold_rbtn = QtWidgets.QRadioButton(self.text_splitter)
        self.txt_hold_rbtn.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.txt_hold_rbtn.setObjectName("txt_hold_rbtn")
        self.txt_press_rbtn = QtWidgets.QRadioButton(self.text_splitter)
        self.txt_press_rbtn.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.txt_press_rbtn.setObjectName("txt_press_rbtn")
        self.colour_grp = QtWidgets.QGroupBox(self.button_tab)
        self.colour_grp.setGeometry(QtCore.QRect(100, 70, 331, 441))
        self.colour_grp.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"text-decoration: underline;")
        self.colour_grp.setObjectName("colour_grp")
        self.colour_splitter = QtWidgets.QSplitter(self.colour_grp)
        self.colour_splitter.setGeometry(QtCore.QRect(26, 40, 241, 401))
        self.colour_splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.colour_splitter.setObjectName("colour_splitter")
        self.colour_r_rbtn = QtWidgets.QRadioButton(self.colour_splitter)
        self.colour_r_rbtn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(251, 49, 33);")
        self.colour_r_rbtn.setObjectName("colour_r_rbtn")
        self.colour_b_rbtn = QtWidgets.QRadioButton(self.colour_splitter)
        self.colour_b_rbtn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(120, 138, 226);")
        self.colour_b_rbtn.setObjectName("colour_b_rbtn")
        self.colour_w_rbtn = QtWidgets.QRadioButton(self.colour_splitter)
        self.colour_w_rbtn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255);")
        self.colour_w_rbtn.setObjectName("colour_w_rbtn")
        self.colour_o_rbtn = QtWidgets.QRadioButton(self.colour_splitter)
        self.colour_o_rbtn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(248, 235, 70);")
        self.colour_o_rbtn.setObjectName("colour_o_rbtn")
        self.modules_tab.addTab(self.button_tab, "")
        self.keypads_tab = QtWidgets.QWidget()
        self.keypads_tab.setObjectName("keypads_tab")
        self.modules_tab.addTab(self.keypads_tab, "")
        self.simonSays_tab = QtWidgets.QWidget()
        self.simonSays_tab.setObjectName("simonSays_tab")
        self.ss_btn_blue = QtWidgets.QPushButton(self.simonSays_tab)
        self.ss_btn_blue.setGeometry(QtCore.QRect(250, 180, 81, 81))
        self.ss_btn_blue.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(120, 138, 226);")
        self.ss_btn_blue.setObjectName("ss_btn_blue")
        self.ss_btn_red = QtWidgets.QPushButton(self.simonSays_tab)
        self.ss_btn_red.setGeometry(QtCore.QRect(210, 260, 81, 81))
        self.ss_btn_red.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(251, 49, 33);")
        self.ss_btn_red.setObjectName("ss_btn_red")
        self.ss_btn_yellow = QtWidgets.QPushButton(self.simonSays_tab)
        self.ss_btn_yellow.setGeometry(QtCore.QRect(290, 260, 81, 81))
        self.ss_btn_yellow.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(248, 235, 70);")
        self.ss_btn_yellow.setObjectName("ss_btn_yellow")
        self.ss_btn_green = QtWidgets.QPushButton(self.simonSays_tab)
        self.ss_btn_green.setGeometry(QtCore.QRect(250, 340, 81, 81))
        self.ss_btn_green.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(50, 165, 18);")
        self.ss_btn_green.setObjectName("ss_btn_green")
        self.modules_tab.addTab(self.simonSays_tab, "")
        self.whoOnFirst_tab = QtWidgets.QWidget()
        self.whoOnFirst_tab.setObjectName("whoOnFirst_tab")
        self.display_cBox = QtWidgets.QComboBox(self.whoOnFirst_tab)
        self.display_cBox.setGeometry(QtCore.QRect(220, 50, 211, 81))
        self.display_cBox.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.display_cBox.setObjectName("display_cBox")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.setItemText(6, "")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.display_cBox.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.whoOnFirst_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(220, 140, 211, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tl_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.tl_lbl.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"border-color: rgb(56, 56, 56);\n"
"background-color: rgb(255, 255, 255);")
        self.tl_lbl.setText("")
        self.tl_lbl.setObjectName("tl_lbl")
        self.gridLayout_2.addWidget(self.tl_lbl, 0, 0, 1, 1)
        self.tr_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.tr_lbl.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"border-color: rgb(56, 56, 56);\n"
"background-color: rgb(255, 255, 255);")
        self.tr_lbl.setText("")
        self.tr_lbl.setObjectName("tr_lbl")
        self.gridLayout_2.addWidget(self.tr_lbl, 0, 1, 1, 1)
        self.ml_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.ml_lbl.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"border-color: rgb(56, 56, 56);\n"
"background-color: rgb(255, 255, 255);")
        self.ml_lbl.setText("")
        self.ml_lbl.setObjectName("ml_lbl")
        self.gridLayout_2.addWidget(self.ml_lbl, 1, 0, 1, 1)
        self.mr_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.mr_lbl.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"border-color: rgb(56, 56, 56);\n"
"background-color: rgb(255, 255, 255);")
        self.mr_lbl.setText("")
        self.mr_lbl.setObjectName("mr_lbl")
        self.gridLayout_2.addWidget(self.mr_lbl, 1, 1, 1, 1)
        self.bl_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.bl_lbl.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"border-color: rgb(56, 56, 56);\n"
"background-color: rgb(255, 255, 255);")
        self.bl_lbl.setText("")
        self.bl_lbl.setObjectName("bl_lbl")
        self.gridLayout_2.addWidget(self.bl_lbl, 2, 0, 1, 1)
        self.br_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.br_lbl.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"border-color: rgb(56, 56, 56);\n"
"background-color: rgb(255, 255, 255);")
        self.br_lbl.setText("")
        self.br_lbl.setObjectName("br_lbl")
        self.gridLayout_2.addWidget(self.br_lbl, 2, 1, 1, 1)
        self.modules_tab.addTab(self.whoOnFirst_tab, "")
        self.memory_tab = QtWidgets.QWidget()
        self.memory_tab.setObjectName("memory_tab")
        self.modules_tab.addTab(self.memory_tab, "")
        self.morseCode = QtWidgets.QWidget()
        self.morseCode.setObjectName("morseCode")
        self.modules_tab.addTab(self.morseCode, "")
        self.compWires_tab = QtWidgets.QWidget()
        self.compWires_tab.setObjectName("compWires_tab")
        self.notes_txt = QtWidgets.QTextEdit(self.compWires_tab)
        self.notes_txt.setGeometry(QtCore.QRect(110, 370, 331, 201))
        self.notes_txt.setObjectName("notes_txt")
        self.pushButton = QtWidgets.QPushButton(self.compWires_tab)
        self.pushButton.setGeometry(QtCore.QRect(340, 540, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget1 = QtWidgets.QWidget(self.compWires_tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 140, 157, 155))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.red_cbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.red_cbox.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.red_cbox.setObjectName("red_cbox")
        self.verticalLayout.addWidget(self.red_cbox)
        self.blue_cbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.blue_cbox.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.blue_cbox.setObjectName("blue_cbox")
        self.verticalLayout.addWidget(self.blue_cbox)
        self.led_cbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.led_cbox.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.led_cbox.setObjectName("led_cbox")
        self.verticalLayout.addWidget(self.led_cbox)
        self.star_cbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.star_cbox.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.star_cbox.setObjectName("star_cbox")
        self.verticalLayout.addWidget(self.star_cbox)
        self.modules_tab.addTab(self.compWires_tab, "")
        self.wireSeq_tab = QtWidgets.QWidget()
        self.wireSeq_tab.setObjectName("wireSeq_tab")
        self.redA_btn = QtWidgets.QPushButton(self.wireSeq_tab)
        self.redA_btn.setGeometry(QtCore.QRect(220, 200, 93, 81))
        self.redA_btn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(251, 49, 33);")
        self.redA_btn.setObjectName("redA_btn")
        self.blueA_btn = QtWidgets.QPushButton(self.wireSeq_tab)
        self.blueA_btn.setGeometry(QtCore.QRect(330, 200, 93, 81))
        self.blueA_btn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(120, 138, 226);")
        self.blueA_btn.setObjectName("blueA_btn")
        self.redB_btn = QtWidgets.QPushButton(self.wireSeq_tab)
        self.redB_btn.setGeometry(QtCore.QRect(220, 290, 93, 81))
        self.redB_btn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(251, 49, 33);")
        self.redB_btn.setObjectName("redB_btn")
        self.redC_btn = QtWidgets.QPushButton(self.wireSeq_tab)
        self.redC_btn.setGeometry(QtCore.QRect(220, 380, 93, 81))
        self.redC_btn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(251, 49, 33);")
        self.redC_btn.setObjectName("redC_btn")
        self.blueB_btn = QtWidgets.QPushButton(self.wireSeq_tab)
        self.blueB_btn.setGeometry(QtCore.QRect(330, 290, 93, 81))
        self.blueB_btn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(120, 138, 226);")
        self.blueB_btn.setObjectName("blueB_btn")
        self.blackB_btn = QtWidgets.QPushButton(self.wireSeq_tab)
        self.blackB_btn.setGeometry(QtCore.QRect(440, 290, 93, 81))
        self.blackB_btn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 56, 56);\n"
"")
        self.blackB_btn.setObjectName("blackB_btn")
        self.blueC_btn = QtWidgets.QPushButton(self.wireSeq_tab)
        self.blueC_btn.setGeometry(QtCore.QRect(330, 380, 93, 81))
        self.blueC_btn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(120, 138, 226);")
        self.blueC_btn.setObjectName("blueC_btn")
        self.blackA_btn = QtWidgets.QPushButton(self.wireSeq_tab)
        self.blackA_btn.setGeometry(QtCore.QRect(440, 200, 93, 81))
        self.blackA_btn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 56, 56);\n"
"")
        self.blackA_btn.setObjectName("blackA_btn")
        self.blackC_btn = QtWidgets.QPushButton(self.wireSeq_tab)
        self.blackC_btn.setGeometry(QtCore.QRect(440, 380, 93, 81))
        self.blackC_btn.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 56, 56);\n"
"")
        self.blackC_btn.setObjectName("blackC_btn")
        self.count_lbl = QtWidgets.QLabel(self.wireSeq_tab)
        self.count_lbl.setGeometry(QtCore.QRect(110, 140, 111, 51))
        self.count_lbl.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.count_lbl.setObjectName("count_lbl")
        self.reset_btn = QtWidgets.QPushButton(self.wireSeq_tab)
        self.reset_btn.setGeometry(QtCore.QRect(560, 140, 93, 51))
        self.reset_btn.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.reset_btn.setObjectName("reset_btn")
        self.redCount_lbl = QtWidgets.QLabel(self.wireSeq_tab)
        self.redCount_lbl.setGeometry(QtCore.QRect(220, 140, 91, 51))
        self.redCount_lbl.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgba(251, 49, 33, 150);")
        self.redCount_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.redCount_lbl.setObjectName("redCount_lbl")
        self.blueCount_lbl = QtWidgets.QLabel(self.wireSeq_tab)
        self.blueCount_lbl.setGeometry(QtCore.QRect(330, 140, 91, 51))
        self.blueCount_lbl.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgba(120, 138, 226, 150)")
        self.blueCount_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.blueCount_lbl.setObjectName("blueCount_lbl")
        self.blackCount_lbl = QtWidgets.QLabel(self.wireSeq_tab)
        self.blackCount_lbl.setGeometry(QtCore.QRect(440, 140, 91, 51))
        self.blackCount_lbl.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgba(56, 56, 56, 175);\n"
"color: rgb(255, 255, 255);")
        self.blackCount_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.blackCount_lbl.setObjectName("blackCount_lbl")
        self.status_lbl = QtWidgets.QLabel(self.wireSeq_tab)
        self.status_lbl.setGeometry(QtCore.QRect(220, 470, 311, 51))
        self.status_lbl.setStyleSheet("font: 16pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255);")
        self.status_lbl.setText("")
        self.status_lbl.setObjectName("status_lbl")
        self.modules_tab.addTab(self.wireSeq_tab, "")
        self.mazes_tab = QtWidgets.QWidget()
        self.mazes_tab.setObjectName("mazes_tab")
        self.modules_tab.addTab(self.mazes_tab, "")
        self.passwords_tab = QtWidgets.QWidget()
        self.passwords_tab.setObjectName("passwords_tab")
        self.modules_tab.addTab(self.passwords_tab, "")
        self.Knobs_tab = QtWidgets.QWidget()
        self.Knobs_tab.setObjectName("Knobs_tab")
        self.whichKnobs_group = QtWidgets.QGroupBox(self.Knobs_tab)
        self.whichKnobs_group.setGeometry(QtCore.QRect(100, 80, 351, 261))
        self.whichKnobs_group.setStyleSheet("font: 16pt \"OCR A Extended\";")
        self.whichKnobs_group.setObjectName("whichKnobs_group")
        self.splitter = QtWidgets.QSplitter(self.whichKnobs_group)
        self.splitter.setGeometry(QtCore.QRect(40, 70, 139, 141))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.all_rbtn = QtWidgets.QRadioButton(self.splitter)
        self.all_rbtn.setObjectName("all_rbtn")
        self.left6_rbtn = QtWidgets.QRadioButton(self.splitter)
        self.left6_rbtn.setObjectName("left6_rbtn")
        self.topRow_rbtn = QtWidgets.QRadioButton(self.splitter)
        self.topRow_rbtn.setObjectName("topRow_rbtn")
        self.widget = QtWidgets.QWidget(self.Knobs_tab)
        self.widget.setGeometry(QtCore.QRect(910, 280, 241, 111))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.knob11_cbox = QtWidgets.QCheckBox(self.widget)
        self.knob11_cbox.setText("")
        self.knob11_cbox.setObjectName("knob11_cbox")
        self.gridLayout.addWidget(self.knob11_cbox, 0, 0, 1, 1)
        self.knob21_cbox = QtWidgets.QCheckBox(self.widget)
        self.knob21_cbox.setText("")
        self.knob21_cbox.setObjectName("knob21_cbox")
        self.gridLayout.addWidget(self.knob21_cbox, 0, 1, 1, 1)
        self.knob31_cbox = QtWidgets.QCheckBox(self.widget)
        self.knob31_cbox.setText("")
        self.knob31_cbox.setObjectName("knob31_cbox")
        self.gridLayout.addWidget(self.knob31_cbox, 0, 2, 1, 1)
        self.knob41_cbox = QtWidgets.QCheckBox(self.widget)
        self.knob41_cbox.setText("")
        self.knob41_cbox.setObjectName("knob41_cbox")
        self.gridLayout.addWidget(self.knob41_cbox, 0, 3, 1, 1)
        self.knob51_cbox = QtWidgets.QCheckBox(self.widget)
        self.knob51_cbox.setText("")
        self.knob51_cbox.setObjectName("knob51_cbox")
        self.gridLayout.addWidget(self.knob51_cbox, 0, 4, 1, 1)
        self.knob60_cbox = QtWidgets.QCheckBox(self.widget)
        self.knob60_cbox.setText("")
        self.knob60_cbox.setObjectName("knob60_cbox")
        self.gridLayout.addWidget(self.knob60_cbox, 0, 5, 1, 1)
        self.knob12_cbox = QtWidgets.QCheckBox(self.widget)
        self.knob12_cbox.setText("")
        self.knob12_cbox.setObjectName("knob12_cbox")
        self.gridLayout.addWidget(self.knob12_cbox, 1, 0, 1, 1)
        self.knob22_cbox = QtWidgets.QCheckBox(self.widget)
        self.knob22_cbox.setText("")
        self.knob22_cbox.setObjectName("knob22_cbox")
        self.gridLayout.addWidget(self.knob22_cbox, 1, 1, 1, 1)
        self.knob32_cbox = QtWidgets.QCheckBox(self.widget)
        self.knob32_cbox.setText("")
        self.knob32_cbox.setObjectName("knob32_cbox")
        self.gridLayout.addWidget(self.knob32_cbox, 1, 2, 1, 1)
        self.knob42_cbox = QtWidgets.QCheckBox(self.widget)
        self.knob42_cbox.setText("")
        self.knob42_cbox.setObjectName("knob42_cbox")
        self.gridLayout.addWidget(self.knob42_cbox, 1, 3, 1, 1)
        self.knob52_cbox = QtWidgets.QCheckBox(self.widget)
        self.knob52_cbox.setText("")
        self.knob52_cbox.setObjectName("knob52_cbox")
        self.gridLayout.addWidget(self.knob52_cbox, 1, 4, 1, 1)
        self.knob62_cbox = QtWidgets.QCheckBox(self.widget)
        self.knob62_cbox.setText("")
        self.knob62_cbox.setObjectName("knob62_cbox")
        self.gridLayout.addWidget(self.knob62_cbox, 1, 5, 1, 1)
        self.modules_tab.addTab(self.Knobs_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1236, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.modules_tab.setCurrentIndex(11)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createBomb_btn.setText(_translate("MainWindow", "Create Bomb"))
        self.strikes_lbl.setText(_translate("MainWindow", "Strikes"))
        self.strike_btn.setText(_translate("MainWindow", "+1"))
        self.wires_btn.setText(_translate("MainWindow", "Go!"))
        self.colourchart_pic.setText(_translate("MainWindow", "Colour chart pic"))
        self.wiresWireframe_pic.setText(_translate("MainWindow", "Simple wires wireframe"))
        self.modules_tab.setTabText(self.modules_tab.indexOf(self.simpleWires_tab), _translate("MainWindow", "Simple Wires"))
        self.text_grp.setTitle(_translate("MainWindow", "Text"))
        self.txt_abort_rbtn.setText(_translate("MainWindow", "Abort"))
        self.txt_detonate_rbtn.setText(_translate("MainWindow", "Detonate"))
        self.txt_hold_rbtn.setText(_translate("MainWindow", "Hold"))
        self.txt_press_rbtn.setText(_translate("MainWindow", "Press"))
        self.colour_grp.setTitle(_translate("MainWindow", "Colour"))
        self.colour_r_rbtn.setText(_translate("MainWindow", "Red"))
        self.colour_b_rbtn.setText(_translate("MainWindow", "Blue"))
        self.colour_w_rbtn.setText(_translate("MainWindow", "White"))
        self.colour_o_rbtn.setText(_translate("MainWindow", "Other"))
        self.modules_tab.setTabText(self.modules_tab.indexOf(self.button_tab), _translate("MainWindow", "The Button"))
        self.modules_tab.setTabText(self.modules_tab.indexOf(self.keypads_tab), _translate("MainWindow", "Keypads"))
        self.ss_btn_blue.setText(_translate("MainWindow", "B"))
        self.ss_btn_red.setText(_translate("MainWindow", "R"))
        self.ss_btn_yellow.setText(_translate("MainWindow", "Y"))
        self.ss_btn_green.setText(_translate("MainWindow", "G"))
        self.modules_tab.setTabText(self.modules_tab.indexOf(self.simonSays_tab), _translate("MainWindow", "Simon Says"))
        self.display_cBox.setItemText(0, _translate("MainWindow", "YES"))
        self.display_cBox.setItemText(1, _translate("MainWindow", "FIRST"))
        self.display_cBox.setItemText(2, _translate("MainWindow", "DISPLAY"))
        self.display_cBox.setItemText(3, _translate("MainWindow", "OKAY"))
        self.display_cBox.setItemText(4, _translate("MainWindow", "SAYS"))
        self.display_cBox.setItemText(5, _translate("MainWindow", "NOTHING"))
        self.display_cBox.setItemText(7, _translate("MainWindow", "BLANK"))
        self.display_cBox.setItemText(8, _translate("MainWindow", "NO"))
        self.display_cBox.setItemText(9, _translate("MainWindow", "LED"))
        self.display_cBox.setItemText(10, _translate("MainWindow", "LEAD"))
        self.display_cBox.setItemText(11, _translate("MainWindow", "READ"))
        self.display_cBox.setItemText(12, _translate("MainWindow", "RED"))
        self.display_cBox.setItemText(13, _translate("MainWindow", "REED"))
        self.display_cBox.setItemText(14, _translate("MainWindow", "LEED"))
        self.display_cBox.setItemText(15, _translate("MainWindow", "HOLD ON"))
        self.display_cBox.setItemText(16, _translate("MainWindow", "YOU"))
        self.display_cBox.setItemText(17, _translate("MainWindow", "YOU ARE"))
        self.display_cBox.setItemText(18, _translate("MainWindow", "YOUR"))
        self.display_cBox.setItemText(19, _translate("MainWindow", "YOU\'RE"))
        self.display_cBox.setItemText(20, _translate("MainWindow", "UR"))
        self.display_cBox.setItemText(21, _translate("MainWindow", "THERE"))
        self.display_cBox.setItemText(22, _translate("MainWindow", "THEY\'RE"))
        self.display_cBox.setItemText(23, _translate("MainWindow", "THEIR"))
        self.display_cBox.setItemText(24, _translate("MainWindow", "THEY ARE"))
        self.display_cBox.setItemText(25, _translate("MainWindow", "SEE"))
        self.display_cBox.setItemText(26, _translate("MainWindow", "C"))
        self.display_cBox.setItemText(27, _translate("MainWindow", "CEE"))
        self.modules_tab.setTabText(self.modules_tab.indexOf(self.whoOnFirst_tab), _translate("MainWindow", "Who\'s On First"))
        self.modules_tab.setTabText(self.modules_tab.indexOf(self.memory_tab), _translate("MainWindow", "Memory"))
        self.modules_tab.setTabText(self.modules_tab.indexOf(self.morseCode), _translate("MainWindow", "Morse Code"))
        self.pushButton.setText(_translate("MainWindow", "Clear Notes"))
        self.red_cbox.setText(_translate("MainWindow", "Red"))
        self.blue_cbox.setText(_translate("MainWindow", "Blue"))
        self.led_cbox.setText(_translate("MainWindow", "LED"))
        self.star_cbox.setText(_translate("MainWindow", "★"))
        self.modules_tab.setTabText(self.modules_tab.indexOf(self.compWires_tab), _translate("MainWindow", "Complicated Wires"))
        self.redA_btn.setText(_translate("MainWindow", "A"))
        self.blueA_btn.setText(_translate("MainWindow", "A"))
        self.redB_btn.setText(_translate("MainWindow", "B"))
        self.redC_btn.setText(_translate("MainWindow", "C"))
        self.blueB_btn.setText(_translate("MainWindow", "B"))
        self.blackB_btn.setText(_translate("MainWindow", "B"))
        self.blueC_btn.setText(_translate("MainWindow", "C"))
        self.blackA_btn.setText(_translate("MainWindow", "A"))
        self.blackC_btn.setText(_translate("MainWindow", "C"))
        self.count_lbl.setText(_translate("MainWindow", "Count:"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.redCount_lbl.setText(_translate("MainWindow", "0"))
        self.blueCount_lbl.setText(_translate("MainWindow", "0"))
        self.blackCount_lbl.setText(_translate("MainWindow", "0"))
        self.modules_tab.setTabText(self.modules_tab.indexOf(self.wireSeq_tab), _translate("MainWindow", "Wire Sequences"))
        self.modules_tab.setTabText(self.modules_tab.indexOf(self.mazes_tab), _translate("MainWindow", "Mazes"))
        self.modules_tab.setTabText(self.modules_tab.indexOf(self.passwords_tab), _translate("MainWindow", "Passwords"))
        self.whichKnobs_group.setTitle(_translate("MainWindow", "Which knobs to check?"))
        self.all_rbtn.setText(_translate("MainWindow", "All"))
        self.left6_rbtn.setText(_translate("MainWindow", "Left 6"))
        self.topRow_rbtn.setText(_translate("MainWindow", "Top Row"))
        self.modules_tab.setTabText(self.modules_tab.indexOf(self.Knobs_tab), _translate("MainWindow", "Knobs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
