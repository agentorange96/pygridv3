# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gui(object):
    def setupUi(self, gui):
        gui.setObjectName("gui")
        gui.resize(676, 485)
        self.centralwidget = QtWidgets.QWidget(gui)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_container = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_container.setGeometry(QtCore.QRect(10, 0, 651, 431))
        self.tab_container.setStyleSheet("QGroupBox {\n"
"        background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(235, 235, 235, 255), stop:1 rgba(255, 255, 255, 255));\n"
"        border: 1px solid gray;\n"
"        border-radius: 6px;\n"
"        border-width: 1px;\n"
"        margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border: 2px solid grey;\n"
"    border-radius: 3px;\n"
"    text-align: center;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0, y2:0, \n"
"                               stop:0 rgba(0, 200,0, 255), stop:1 rgba(220, 20,20, 255));\n"
"}\n"
"\n"
"\n"
"")
        self.tab_container.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_container.setObjectName("tab_container")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.group_fan_control = QtWidgets.QGroupBox(self.tab_main)
        self.group_fan_control.setGeometry(QtCore.QRect(10, 10, 251, 381))
        self.group_fan_control.setObjectName("group_fan_control")
        self.group_fan_0 = QtWidgets.QGroupBox(self.group_fan_control)
        self.group_fan_0.setGeometry(QtCore.QRect(10, 20, 231, 56))
        self.group_fan_0.setObjectName("group_fan_0")
        self.sld_fan_speed_0 = QtWidgets.QSlider(self.group_fan_0)
        self.sld_fan_speed_0.setEnabled(True)
        self.sld_fan_speed_0.setGeometry(QtCore.QRect(95, 20, 91, 29))
        self.sld_fan_speed_0.setMaximum(100)
        self.sld_fan_speed_0.setOrientation(QtCore.Qt.Horizontal)
        self.sld_fan_speed_0.setObjectName("sld_fan_speed_0")
        self.lbl_fan_speed_0 = QtWidgets.QLabel(self.group_fan_0)
        self.lbl_fan_speed_0.setGeometry(QtCore.QRect(190, 25, 41, 17))
        self.lbl_fan_speed_0.setObjectName("lbl_fan_speed_0")
        self.cb_fan_profile_0 = QtWidgets.QComboBox(self.group_fan_0)
        self.cb_fan_profile_0.setGeometry(QtCore.QRect(10, 20, 81, 27))
        self.cb_fan_profile_0.setMaxVisibleItems(3)
        self.cb_fan_profile_0.setMaxCount(3)
        self.cb_fan_profile_0.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_fan_profile_0.setObjectName("cb_fan_profile_0")
        self.cb_fan_profile_0.addItem("")
        self.cb_fan_profile_0.addItem("")
        self.cb_fan_profile_0.addItem("")
        self.group_fan_1 = QtWidgets.QGroupBox(self.group_fan_control)
        self.group_fan_1.setGeometry(QtCore.QRect(10, 80, 231, 56))
        self.group_fan_1.setObjectName("group_fan_1")
        self.sld_fan_speed_1 = QtWidgets.QSlider(self.group_fan_1)
        self.sld_fan_speed_1.setGeometry(QtCore.QRect(95, 20, 91, 29))
        self.sld_fan_speed_1.setMaximum(100)
        self.sld_fan_speed_1.setOrientation(QtCore.Qt.Horizontal)
        self.sld_fan_speed_1.setObjectName("sld_fan_speed_1")
        self.lbl_fan_speed_1 = QtWidgets.QLabel(self.group_fan_1)
        self.lbl_fan_speed_1.setGeometry(QtCore.QRect(190, 25, 41, 17))
        self.lbl_fan_speed_1.setObjectName("lbl_fan_speed_1")
        self.cb_fan_profile_1 = QtWidgets.QComboBox(self.group_fan_1)
        self.cb_fan_profile_1.setGeometry(QtCore.QRect(10, 20, 81, 27))
        self.cb_fan_profile_1.setMaxVisibleItems(3)
        self.cb_fan_profile_1.setMaxCount(3)
        self.cb_fan_profile_1.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_fan_profile_1.setObjectName("cb_fan_profile_1")
        self.cb_fan_profile_1.addItem("")
        self.cb_fan_profile_1.addItem("")
        self.cb_fan_profile_1.addItem("")
        self.group_fan_2 = QtWidgets.QGroupBox(self.group_fan_control)
        self.group_fan_2.setGeometry(QtCore.QRect(10, 140, 231, 56))
        self.group_fan_2.setObjectName("group_fan_2")
        self.sld_fan_speed_2 = QtWidgets.QSlider(self.group_fan_2)
        self.sld_fan_speed_2.setGeometry(QtCore.QRect(95, 20, 91, 29))
        self.sld_fan_speed_2.setMaximum(100)
        self.sld_fan_speed_2.setOrientation(QtCore.Qt.Horizontal)
        self.sld_fan_speed_2.setObjectName("sld_fan_speed_2")
        self.lbl_fan_speed_2 = QtWidgets.QLabel(self.group_fan_2)
        self.lbl_fan_speed_2.setGeometry(QtCore.QRect(190, 25, 41, 17))
        self.lbl_fan_speed_2.setObjectName("lbl_fan_speed_2")
        self.cb_fan_profile_2 = QtWidgets.QComboBox(self.group_fan_2)
        self.cb_fan_profile_2.setGeometry(QtCore.QRect(10, 20, 81, 27))
        self.cb_fan_profile_2.setMaxVisibleItems(3)
        self.cb_fan_profile_2.setMaxCount(3)
        self.cb_fan_profile_2.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_fan_profile_2.setObjectName("cb_fan_profile_2")
        self.cb_fan_profile_2.addItem("")
        self.cb_fan_profile_2.addItem("")
        self.cb_fan_profile_2.addItem("")
        self.group_fan_3 = QtWidgets.QGroupBox(self.group_fan_control)
        self.group_fan_3.setGeometry(QtCore.QRect(10, 200, 231, 56))
        self.group_fan_3.setObjectName("group_fan_3")
        self.sld_fan_speed_3 = QtWidgets.QSlider(self.group_fan_3)
        self.sld_fan_speed_3.setGeometry(QtCore.QRect(95, 20, 91, 29))
        self.sld_fan_speed_3.setMaximum(100)
        self.sld_fan_speed_3.setOrientation(QtCore.Qt.Horizontal)
        self.sld_fan_speed_3.setObjectName("sld_fan_speed_3")
        self.lbl_fan_speed_3 = QtWidgets.QLabel(self.group_fan_3)
        self.lbl_fan_speed_3.setGeometry(QtCore.QRect(190, 25, 41, 17))
        self.lbl_fan_speed_3.setObjectName("lbl_fan_speed_3")
        self.cb_fan_profile_3 = QtWidgets.QComboBox(self.group_fan_3)
        self.cb_fan_profile_3.setGeometry(QtCore.QRect(10, 20, 81, 27))
        self.cb_fan_profile_3.setMaxVisibleItems(3)
        self.cb_fan_profile_3.setMaxCount(3)
        self.cb_fan_profile_3.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_fan_profile_3.setObjectName("cb_fan_profile_3")
        self.cb_fan_profile_3.addItem("")
        self.cb_fan_profile_3.addItem("")
        self.cb_fan_profile_3.addItem("")
        self.group_fan_4 = QtWidgets.QGroupBox(self.group_fan_control)
        self.group_fan_4.setGeometry(QtCore.QRect(10, 260, 231, 56))
        self.group_fan_4.setObjectName("group_fan_4")
        self.sld_fan_speed_4 = QtWidgets.QSlider(self.group_fan_4)
        self.sld_fan_speed_4.setGeometry(QtCore.QRect(95, 20, 91, 29))
        self.sld_fan_speed_4.setMaximum(100)
        self.sld_fan_speed_4.setOrientation(QtCore.Qt.Horizontal)
        self.sld_fan_speed_4.setObjectName("sld_fan_speed_4")
        self.lbl_fan_speed_4 = QtWidgets.QLabel(self.group_fan_4)
        self.lbl_fan_speed_4.setGeometry(QtCore.QRect(190, 25, 41, 17))
        self.lbl_fan_speed_4.setObjectName("lbl_fan_speed_4")
        self.cb_fan_profile_4 = QtWidgets.QComboBox(self.group_fan_4)
        self.cb_fan_profile_4.setGeometry(QtCore.QRect(10, 20, 81, 27))
        self.cb_fan_profile_4.setMaxVisibleItems(3)
        self.cb_fan_profile_4.setMaxCount(3)
        self.cb_fan_profile_4.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_fan_profile_4.setObjectName("cb_fan_profile_4")
        self.cb_fan_profile_4.addItem("")
        self.cb_fan_profile_4.addItem("")
        self.cb_fan_profile_4.addItem("")
        self.group_fan_5 = QtWidgets.QGroupBox(self.group_fan_control)
        self.group_fan_5.setGeometry(QtCore.QRect(10, 320, 231, 56))
        self.group_fan_5.setObjectName("group_fan_5")
        self.sld_fan_speed_5 = QtWidgets.QSlider(self.group_fan_5)
        self.sld_fan_speed_5.setGeometry(QtCore.QRect(95, 20, 91, 29))
        self.sld_fan_speed_5.setMaximum(100)
        self.sld_fan_speed_5.setOrientation(QtCore.Qt.Horizontal)
        self.sld_fan_speed_5.setObjectName("sld_fan_speed_5")
        self.lbl_fan_speed_5 = QtWidgets.QLabel(self.group_fan_5)
        self.lbl_fan_speed_5.setGeometry(QtCore.QRect(190, 25, 41, 17))
        self.lbl_fan_speed_5.setObjectName("lbl_fan_speed_5")
        self.cb_fan_profile_5 = QtWidgets.QComboBox(self.group_fan_5)
        self.cb_fan_profile_5.setGeometry(QtCore.QRect(10, 20, 81, 27))
        self.cb_fan_profile_5.setMaxVisibleItems(3)
        self.cb_fan_profile_5.setMaxCount(3)
        self.cb_fan_profile_5.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_fan_profile_5.setObjectName("cb_fan_profile_5")
        self.cb_fan_profile_5.addItem("")
        self.cb_fan_profile_5.addItem("")
        self.cb_fan_profile_5.addItem("")
        self.group_fan_status = QtWidgets.QGroupBox(self.tab_main)
        self.group_fan_status.setGeometry(QtCore.QRect(270, 10, 221, 381))
        self.group_fan_status.setObjectName("group_fan_status")
        self.group_fan_stat_0 = QtWidgets.QGroupBox(self.group_fan_status)
        self.group_fan_stat_0.setGeometry(QtCore.QRect(10, 20, 201, 56))
        self.group_fan_stat_0.setObjectName("group_fan_stat_0")
        self.lbl_fan_rpm_0 = QtWidgets.QLabel(self.group_fan_stat_0)
        self.lbl_fan_rpm_0.setGeometry(QtCore.QRect(50, 25, 41, 17))
        self.lbl_fan_rpm_0.setObjectName("lbl_fan_rpm_0")
        self.lbl_fan_watt_0 = QtWidgets.QLabel(self.group_fan_stat_0)
        self.lbl_fan_watt_0.setGeometry(QtCore.QRect(140, 25, 21, 17))
        self.lbl_fan_watt_0.setObjectName("lbl_fan_watt_0")
        self.line = QtWidgets.QFrame(self.group_fan_stat_0)
        self.line.setGeometry(QtCore.QRect(120, 20, 20, 25))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lbl_fan_led_0 = QtWidgets.QLabel(self.group_fan_stat_0)
        self.lbl_fan_led_0.setGeometry(QtCore.QRect(10, 22, 25, 25))
        self.lbl_fan_led_0.setText("")
        self.lbl_fan_led_0.setPixmap(QtGui.QPixmap(":/resources/red_led.png"))
        self.lbl_fan_led_0.setScaledContents(True)
        self.lbl_fan_led_0.setObjectName("lbl_fan_led_0")
        self.label = QtWidgets.QLabel(self.group_fan_stat_0)
        self.label.setGeometry(QtCore.QRect(90, 25, 33, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.group_fan_stat_0)
        self.label_2.setGeometry(QtCore.QRect(170, 25, 21, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.group_fan_stat_1 = QtWidgets.QGroupBox(self.group_fan_status)
        self.group_fan_stat_1.setGeometry(QtCore.QRect(10, 80, 201, 56))
        self.group_fan_stat_1.setObjectName("group_fan_stat_1")
        self.lbl_fan_rpm_1 = QtWidgets.QLabel(self.group_fan_stat_1)
        self.lbl_fan_rpm_1.setGeometry(QtCore.QRect(50, 25, 41, 17))
        self.lbl_fan_rpm_1.setObjectName("lbl_fan_rpm_1")
        self.lbl_fan_watt_1 = QtWidgets.QLabel(self.group_fan_stat_1)
        self.lbl_fan_watt_1.setGeometry(QtCore.QRect(140, 25, 21, 17))
        self.lbl_fan_watt_1.setObjectName("lbl_fan_watt_1")
        self.line_2 = QtWidgets.QFrame(self.group_fan_stat_1)
        self.line_2.setGeometry(QtCore.QRect(120, 20, 20, 25))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lbl_fan_led_1 = QtWidgets.QLabel(self.group_fan_stat_1)
        self.lbl_fan_led_1.setGeometry(QtCore.QRect(10, 22, 25, 25))
        self.lbl_fan_led_1.setText("")
        self.lbl_fan_led_1.setPixmap(QtGui.QPixmap(":/resources/red_led.png"))
        self.lbl_fan_led_1.setScaledContents(True)
        self.lbl_fan_led_1.setObjectName("lbl_fan_led_1")
        self.label_3 = QtWidgets.QLabel(self.group_fan_stat_1)
        self.label_3.setGeometry(QtCore.QRect(90, 25, 33, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.group_fan_stat_1)
        self.label_4.setGeometry(QtCore.QRect(170, 25, 21, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.group_fan_stat_2 = QtWidgets.QGroupBox(self.group_fan_status)
        self.group_fan_stat_2.setGeometry(QtCore.QRect(10, 140, 201, 56))
        self.group_fan_stat_2.setObjectName("group_fan_stat_2")
        self.lbl_fan_rpm_2 = QtWidgets.QLabel(self.group_fan_stat_2)
        self.lbl_fan_rpm_2.setGeometry(QtCore.QRect(50, 25, 41, 17))
        self.lbl_fan_rpm_2.setObjectName("lbl_fan_rpm_2")
        self.lbl_fan_watt_2 = QtWidgets.QLabel(self.group_fan_stat_2)
        self.lbl_fan_watt_2.setGeometry(QtCore.QRect(140, 25, 21, 17))
        self.lbl_fan_watt_2.setObjectName("lbl_fan_watt_2")
        self.line_3 = QtWidgets.QFrame(self.group_fan_stat_2)
        self.line_3.setGeometry(QtCore.QRect(120, 20, 20, 25))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lbl_fan_led_2 = QtWidgets.QLabel(self.group_fan_stat_2)
        self.lbl_fan_led_2.setGeometry(QtCore.QRect(10, 22, 25, 25))
        self.lbl_fan_led_2.setText("")
        self.lbl_fan_led_2.setPixmap(QtGui.QPixmap(":/resources/red_led.png"))
        self.lbl_fan_led_2.setScaledContents(True)
        self.lbl_fan_led_2.setObjectName("lbl_fan_led_2")
        self.label_5 = QtWidgets.QLabel(self.group_fan_stat_2)
        self.label_5.setGeometry(QtCore.QRect(90, 25, 33, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.group_fan_stat_2)
        self.label_6.setGeometry(QtCore.QRect(170, 25, 21, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.group_fan_stat_3 = QtWidgets.QGroupBox(self.group_fan_status)
        self.group_fan_stat_3.setGeometry(QtCore.QRect(10, 200, 201, 56))
        self.group_fan_stat_3.setObjectName("group_fan_stat_3")
        self.lbl_fan_rpm_3 = QtWidgets.QLabel(self.group_fan_stat_3)
        self.lbl_fan_rpm_3.setGeometry(QtCore.QRect(50, 25, 41, 17))
        self.lbl_fan_rpm_3.setObjectName("lbl_fan_rpm_3")
        self.lbl_fan_watt_3 = QtWidgets.QLabel(self.group_fan_stat_3)
        self.lbl_fan_watt_3.setGeometry(QtCore.QRect(140, 25, 21, 17))
        self.lbl_fan_watt_3.setObjectName("lbl_fan_watt_3")
        self.line_4 = QtWidgets.QFrame(self.group_fan_stat_3)
        self.line_4.setGeometry(QtCore.QRect(120, 20, 20, 25))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.lbl_fan_led_3 = QtWidgets.QLabel(self.group_fan_stat_3)
        self.lbl_fan_led_3.setGeometry(QtCore.QRect(10, 22, 25, 25))
        self.lbl_fan_led_3.setText("")
        self.lbl_fan_led_3.setPixmap(QtGui.QPixmap(":/resources/red_led.png"))
        self.lbl_fan_led_3.setScaledContents(True)
        self.lbl_fan_led_3.setObjectName("lbl_fan_led_3")
        self.label_7 = QtWidgets.QLabel(self.group_fan_stat_3)
        self.label_7.setGeometry(QtCore.QRect(90, 25, 33, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.group_fan_stat_3)
        self.label_8.setGeometry(QtCore.QRect(170, 25, 21, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.group_fan_stat_4 = QtWidgets.QGroupBox(self.group_fan_status)
        self.group_fan_stat_4.setGeometry(QtCore.QRect(10, 260, 201, 56))
        self.group_fan_stat_4.setObjectName("group_fan_stat_4")
        self.lbl_fan_rpm_4 = QtWidgets.QLabel(self.group_fan_stat_4)
        self.lbl_fan_rpm_4.setGeometry(QtCore.QRect(50, 25, 41, 17))
        self.lbl_fan_rpm_4.setObjectName("lbl_fan_rpm_4")
        self.lbl_fan_watt_4 = QtWidgets.QLabel(self.group_fan_stat_4)
        self.lbl_fan_watt_4.setGeometry(QtCore.QRect(140, 25, 21, 17))
        self.lbl_fan_watt_4.setObjectName("lbl_fan_watt_4")
        self.line_5 = QtWidgets.QFrame(self.group_fan_stat_4)
        self.line_5.setGeometry(QtCore.QRect(120, 20, 20, 25))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.lbl_fan_led_4 = QtWidgets.QLabel(self.group_fan_stat_4)
        self.lbl_fan_led_4.setGeometry(QtCore.QRect(10, 22, 25, 25))
        self.lbl_fan_led_4.setText("")
        self.lbl_fan_led_4.setPixmap(QtGui.QPixmap(":/resources/red_led.png"))
        self.lbl_fan_led_4.setScaledContents(True)
        self.lbl_fan_led_4.setObjectName("lbl_fan_led_4")
        self.label_9 = QtWidgets.QLabel(self.group_fan_stat_4)
        self.label_9.setGeometry(QtCore.QRect(90, 25, 33, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.group_fan_stat_4)
        self.label_10.setGeometry(QtCore.QRect(170, 25, 21, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.group_fan_stat_5 = QtWidgets.QGroupBox(self.group_fan_status)
        self.group_fan_stat_5.setGeometry(QtCore.QRect(10, 320, 201, 56))
        self.group_fan_stat_5.setObjectName("group_fan_stat_5")
        self.lbl_fan_rpm_5 = QtWidgets.QLabel(self.group_fan_stat_5)
        self.lbl_fan_rpm_5.setGeometry(QtCore.QRect(50, 25, 41, 17))
        self.lbl_fan_rpm_5.setObjectName("lbl_fan_rpm_5")
        self.lbl_fan_watt_5 = QtWidgets.QLabel(self.group_fan_stat_5)
        self.lbl_fan_watt_5.setGeometry(QtCore.QRect(140, 25, 21, 17))
        self.lbl_fan_watt_5.setObjectName("lbl_fan_watt_5")
        self.line_6 = QtWidgets.QFrame(self.group_fan_stat_5)
        self.line_6.setGeometry(QtCore.QRect(120, 20, 20, 25))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.lbl_fan_led_5 = QtWidgets.QLabel(self.group_fan_stat_5)
        self.lbl_fan_led_5.setGeometry(QtCore.QRect(10, 22, 25, 25))
        self.lbl_fan_led_5.setText("")
        self.lbl_fan_led_5.setPixmap(QtGui.QPixmap(":/resources/red_led.png"))
        self.lbl_fan_led_5.setScaledContents(True)
        self.lbl_fan_led_5.setObjectName("lbl_fan_led_5")
        self.label_11 = QtWidgets.QLabel(self.group_fan_stat_5)
        self.label_11.setGeometry(QtCore.QRect(90, 25, 33, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.group_fan_stat_5)
        self.label_12.setGeometry(QtCore.QRect(170, 25, 21, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.grp_cpu = QtWidgets.QGroupBox(self.tab_main)
        self.grp_cpu.setGeometry(QtCore.QRect(500, 10, 141, 81))
        self.grp_cpu.setObjectName("grp_cpu")
        self.lcd_cpu_temp = QtWidgets.QLCDNumber(self.grp_cpu)
        self.lcd_cpu_temp.setGeometry(QtCore.QRect(20, 30, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lcd_cpu_temp.setFont(font)
        self.lcd_cpu_temp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_cpu_temp.setLineWidth(1)
        self.lcd_cpu_temp.setDigitCount(3)
        self.lcd_cpu_temp.setProperty("value", 100.0)
        self.lcd_cpu_temp.setObjectName("lcd_cpu_temp")
        self.label_13 = QtWidgets.QLabel(self.grp_cpu)
        self.label_13.setGeometry(QtCore.QRect(100, 27, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pb_cpu_temp = QtWidgets.QProgressBar(self.grp_cpu)
        self.pb_cpu_temp.setGeometry(QtCore.QRect(10, 20, 16, 51))
        self.pb_cpu_temp.setProperty("value", 80)
        self.pb_cpu_temp.setTextVisible(False)
        self.pb_cpu_temp.setOrientation(QtCore.Qt.Vertical)
        self.pb_cpu_temp.setObjectName("pb_cpu_temp")
        self.grp_cpu_2 = QtWidgets.QGroupBox(self.tab_main)
        self.grp_cpu_2.setGeometry(QtCore.QRect(500, 100, 141, 81))
        self.grp_cpu_2.setObjectName("grp_cpu_2")
        self.lcd_gpu_temp = QtWidgets.QLCDNumber(self.grp_cpu_2)
        self.lcd_gpu_temp.setGeometry(QtCore.QRect(20, 30, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lcd_gpu_temp.setFont(font)
        self.lcd_gpu_temp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_gpu_temp.setLineWidth(1)
        self.lcd_gpu_temp.setDigitCount(3)
        self.lcd_gpu_temp.setProperty("value", 100.0)
        self.lcd_gpu_temp.setObjectName("lcd_gpu_temp")
        self.label_14 = QtWidgets.QLabel(self.grp_cpu_2)
        self.label_14.setGeometry(QtCore.QRect(100, 27, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.pb_gpu_temp = QtWidgets.QProgressBar(self.grp_cpu_2)
        self.pb_gpu_temp.setGeometry(QtCore.QRect(10, 22, 16, 51))
        self.pb_gpu_temp.setProperty("value", 80)
        self.pb_gpu_temp.setTextVisible(False)
        self.pb_gpu_temp.setOrientation(QtCore.Qt.Vertical)
        self.pb_gpu_temp.setObjectName("pb_gpu_temp")
        self.tab_container.addTab(self.tab_main, "")
        self.tab_fan_config = QtWidgets.QWidget()
        self.tab_fan_config.setObjectName("tab_fan_config")
        self.tab_container.addTab(self.tab_fan_config, "")
        self.tab_general_config = QtWidgets.QWidget()
        self.tab_general_config.setObjectName("tab_general_config")
        self.tab_container.addTab(self.tab_general_config, "")
        gui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(gui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 22))
        self.menubar.setObjectName("menubar")
        gui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(gui)
        self.statusbar.setObjectName("statusbar")
        gui.setStatusBar(self.statusbar)

        self.retranslateUi(gui)
        self.tab_container.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(gui)

    def retranslateUi(self, gui):
        _translate = QtCore.QCoreApplication.translate
        gui.setWindowTitle(_translate("gui", "PyGrid V3"))
        self.group_fan_control.setTitle(_translate("gui", "Fan Control"))
        self.group_fan_0.setTitle(_translate("gui", "Fan #1"))
        self.lbl_fan_speed_0.setText(_translate("gui", "0%"))
        self.cb_fan_profile_0.setCurrentText(_translate("gui", "Manual"))
        self.cb_fan_profile_0.setItemText(0, _translate("gui", "Manual"))
        self.cb_fan_profile_0.setItemText(1, _translate("gui", "1"))
        self.cb_fan_profile_0.setItemText(2, _translate("gui", "3"))
        self.group_fan_1.setTitle(_translate("gui", "Fan #2"))
        self.lbl_fan_speed_1.setText(_translate("gui", "0%"))
        self.cb_fan_profile_1.setCurrentText(_translate("gui", "Manual"))
        self.cb_fan_profile_1.setItemText(0, _translate("gui", "Manual"))
        self.cb_fan_profile_1.setItemText(1, _translate("gui", "1"))
        self.cb_fan_profile_1.setItemText(2, _translate("gui", "3"))
        self.group_fan_2.setTitle(_translate("gui", "Fan #3"))
        self.lbl_fan_speed_2.setText(_translate("gui", "0%"))
        self.cb_fan_profile_2.setCurrentText(_translate("gui", "Manual"))
        self.cb_fan_profile_2.setItemText(0, _translate("gui", "Manual"))
        self.cb_fan_profile_2.setItemText(1, _translate("gui", "1"))
        self.cb_fan_profile_2.setItemText(2, _translate("gui", "3"))
        self.group_fan_3.setTitle(_translate("gui", "Fan #4"))
        self.lbl_fan_speed_3.setText(_translate("gui", "0%"))
        self.cb_fan_profile_3.setCurrentText(_translate("gui", "Manual"))
        self.cb_fan_profile_3.setItemText(0, _translate("gui", "Manual"))
        self.cb_fan_profile_3.setItemText(1, _translate("gui", "1"))
        self.cb_fan_profile_3.setItemText(2, _translate("gui", "3"))
        self.group_fan_4.setTitle(_translate("gui", "Fan #5"))
        self.lbl_fan_speed_4.setText(_translate("gui", "0%"))
        self.cb_fan_profile_4.setCurrentText(_translate("gui", "Manual"))
        self.cb_fan_profile_4.setItemText(0, _translate("gui", "Manual"))
        self.cb_fan_profile_4.setItemText(1, _translate("gui", "1"))
        self.cb_fan_profile_4.setItemText(2, _translate("gui", "3"))
        self.group_fan_5.setTitle(_translate("gui", "Fan #6"))
        self.lbl_fan_speed_5.setText(_translate("gui", "0%"))
        self.cb_fan_profile_5.setCurrentText(_translate("gui", "Manual"))
        self.cb_fan_profile_5.setItemText(0, _translate("gui", "Manual"))
        self.cb_fan_profile_5.setItemText(1, _translate("gui", "1"))
        self.cb_fan_profile_5.setItemText(2, _translate("gui", "3"))
        self.group_fan_status.setTitle(_translate("gui", "Fan Status"))
        self.group_fan_stat_0.setTitle(_translate("gui", "Fan #1"))
        self.lbl_fan_rpm_0.setText(_translate("gui", "0"))
        self.lbl_fan_watt_0.setText(_translate("gui", "0.0"))
        self.label.setText(_translate("gui", "RPM"))
        self.label_2.setText(_translate("gui", "W"))
        self.group_fan_stat_1.setTitle(_translate("gui", "Fan #2"))
        self.lbl_fan_rpm_1.setText(_translate("gui", "0"))
        self.lbl_fan_watt_1.setText(_translate("gui", "0.0"))
        self.label_3.setText(_translate("gui", "RPM"))
        self.label_4.setText(_translate("gui", "W"))
        self.group_fan_stat_2.setTitle(_translate("gui", "Fan #3"))
        self.lbl_fan_rpm_2.setText(_translate("gui", "0"))
        self.lbl_fan_watt_2.setText(_translate("gui", "0.0"))
        self.label_5.setText(_translate("gui", "RPM"))
        self.label_6.setText(_translate("gui", "W"))
        self.group_fan_stat_3.setTitle(_translate("gui", "Fan #4"))
        self.lbl_fan_rpm_3.setText(_translate("gui", "0"))
        self.lbl_fan_watt_3.setText(_translate("gui", "0.0"))
        self.label_7.setText(_translate("gui", "RPM"))
        self.label_8.setText(_translate("gui", "W"))
        self.group_fan_stat_4.setTitle(_translate("gui", "Fan #5"))
        self.lbl_fan_rpm_4.setText(_translate("gui", "0"))
        self.lbl_fan_watt_4.setText(_translate("gui", "0.0"))
        self.label_9.setText(_translate("gui", "RPM"))
        self.label_10.setText(_translate("gui", "W"))
        self.group_fan_stat_5.setTitle(_translate("gui", "Fan #6"))
        self.lbl_fan_rpm_5.setText(_translate("gui", "0"))
        self.lbl_fan_watt_5.setText(_translate("gui", "0.0"))
        self.label_11.setText(_translate("gui", "RPM"))
        self.label_12.setText(_translate("gui", "W"))
        self.grp_cpu.setTitle(_translate("gui", "CPU Temp"))
        self.label_13.setText(_translate("gui", "ºC"))
        self.grp_cpu_2.setTitle(_translate("gui", "GPU Temp"))
        self.label_14.setText(_translate("gui", "ºC"))
        self.tab_container.setTabText(self.tab_container.indexOf(self.tab_main), _translate("gui", "Main"))
        self.tab_container.setTabText(self.tab_container.indexOf(self.tab_fan_config), _translate("gui", "Fan Config"))
        self.tab_container.setTabText(self.tab_container.indexOf(self.tab_general_config), _translate("gui", "General Config"))

from . import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = QtWidgets.QMainWindow()
    ui = Ui_gui()
    ui.setupUi(gui)
    gui.show()
    sys.exit(app.exec_())
