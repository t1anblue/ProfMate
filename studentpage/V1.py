# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'V1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
#from student import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QAction
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import Python_DB


class Ui_MainWindow1(object):
    # def switch_page(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    #     MainWindow.hide()

    def setup(self, MainWindow):
        MainWindow.setObjectName("ProfMate")
        MainWindow.resize(581, 561)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon.fromTheme("ProfMate")
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_team_name = QtWidgets.QLabel(self.centralwidget)
        self.label_team_name.setGeometry(QtCore.QRect(180, 20, 300, 31))
        self.label_team_name.setObjectName("label_team_name")


        self.label_icon = QtWidgets.QLabel(self.centralwidget)
        self.label_icon.setGeometry(QtCore.QRect(80, -20, 91, 111))  ##(x,y,length,width)
        self.label_icon.setStyleSheet("image: url(:/Logo/MAC.png);")
        self.label_icon.setText("")
        self.label_icon.setObjectName("label_icon")

        # self.logo = QtWidgets.QLabel(self.centralwidget)
        # self.logo.setGeometry(QtCore.QRect(20, -20, 300, 100))
        # self.logo.setText("")
        # self.logo.setPixmap(QtGui.QPixmap("C:/capstone/studentpage/MAC.png"))
        #
        # self.logo.setObjectName("logo")



        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(330, 210, 181, 181))
        self.listWidget_2.setObjectName("listWidget_2")

        self.Percentage = QtWidgets.QProgressBar(self.centralwidget)
        self.Percentage.setGeometry(QtCore.QRect(170, 400, 118, 23))
        self.Percentage.setProperty("value", 90)
        self.Percentage.setObjectName("Percentage")
        self.label_section = QtWidgets.QLabel(self.centralwidget)
        self.label_section.setGeometry(QtCore.QRect(110, 110, 91, 31))
        self.label_section.setObjectName("label")
        self.label_absent = QtWidgets.QLabel(self.centralwidget)
        self.label_absent.setGeometry(QtCore.QRect(330, 180, 71, 16))
        self.label_absent.setObjectName("label_absent")
        self.label_attandance = QtWidgets.QLabel(self.centralwidget)
        self.label_attandance.setGeometry(QtCore.QRect(110, 180, 80, 16))
        self.label_attandance.setObjectName("label_attandance")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(430, 180, 81, 21))
        self.listView_2.setObjectName("listView_2")

        self.label_lecture = QtWidgets.QLabel(self.centralwidget)
        self.label_lecture.setGeometry(QtCore.QRect(110, 80, 91, 31))
        self.label_lecture.setObjectName("label_lecture")
        self.comboBox_course = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_course.setGeometry(QtCore.QRect(190, 85, 131, 22))
        self.comboBox_course.setObjectName("comboBox_course")
        self.comboBox_course.addItem("")
        self.comboBox_course.addItem("")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(210, 180, 81, 21))
        self.listView.setObjectName("listView")
        self.comboBox_section = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_section.setGeometry(QtCore.QRect(190, 117, 131, 22))
        self.comboBox_section.setObjectName("comboBox")
        self.comboBox_section.addItem("")
        self.comboBox_section.addItem("")
        self.comboBox_section.addItem("")
        self.comboBox_section.addItem("")
        self.comboBox_section.addItem("")
        self.comboBox_section.addItem("")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(110, 210, 181, 181))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 128, 218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 6, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 3, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)



        # self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        # self.listWidget.setGeometry(QtCore.QRect(110, 210, 181, 181))
        # self.listWidget.setObjectName("listWidget")



        self.view_attendance_btn = QtWidgets.QPushButton(self.centralwidget)
        self.view_attendance_btn.setGeometry(QtCore.QRect(410, 440, 120, 32))
        self.view_attendance_btn.setObjectName("view_attendance_btn")
        MainWindow.setCentralWidget(self.centralwidget)



        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_team_name.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#550022;\">McMaster </span><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#940049;\">ProfMate</span></p></body></html>"))
        self.label_section.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:9pt;\">Section :</span></p></body></html>"))
        self.label_absent.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:9pt; color:#ff0000;\">Absent</span></p></body></html>"))
        self.label_attandance.setText(_translate("MainWindow",
                                                 "<html><head/><body><p><span style=\" font-size:9pt; color:#0000ff;\">Attandance </span></p></body></html>"))
        self.label_lecture.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:9pt;\">Lecture :</span></p></body></html>"))
        self.comboBox_course.setItemText(0, _translate("MainWindow", "ENG 4OI6B"))
        self.comboBox_course.setItemText(1, _translate("MainWindow", "COMPENG 4TL4"))
        self.comboBox_section.setItemText(0, _translate("MainWindow", "Section 1001"))
        self.comboBox_section.setItemText(1, _translate("MainWindow", "Section 1002"))
        self.comboBox_section.setItemText(2, _translate("MainWindow", "Section 1003"))
        self.comboBox_section.setItemText(3, _translate("MainWindow", "Section 1004"))
        self.comboBox_section.setItemText(4, _translate("MainWindow", "Section 1005"))
        self.comboBox_section.setItemText(5, _translate("MainWindow", "Section 1006"))
        #  *******************************************************Modifications
        self.comboBox_course.currentTextChanged.connect(self.onComboBoxChanged)
# **********************************To be continued


        #*****************Modifications***********************
        # self.listWidget_2.addItem("This is a message")
        # self.listWidget_2.addItem("This is another message")

        self.view_attendance_btn.setText(_translate("MainWindow", "View Attendance"))
        self.view_attendance_btn.clicked.connect(self.view_attendance_btn_clicked)

    #  *******************************************************Modifications
    def onComboBoxChanged(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        if self.comboBox_course.currentText() == "ENG 4OI6B":
            self.comboBox_section.setItemText(0, _translate("MainWindow", "Section 1001"))
            self.comboBox_section.setItemText(1, _translate("MainWindow", "Section 1002"))
            self.comboBox_section.setItemText(2, _translate("MainWindow", "Section 1003"))
            self.comboBox_section.setItemText(3, _translate("MainWindow", "Section 1004"))
            self.comboBox_section.setItemText(4, _translate("MainWindow", "Section 1005"))
            self.comboBox_section.setItemText(5, _translate("MainWindow", "Section 1006"))
        elif self.comboBox_course.currentText() == "COMPENG 4TL4":
            self.comboBox_section.setItemText(0, _translate("MainWindow", "Section 2001"))
            self.comboBox_section.setItemText(1, _translate("MainWindow", "Section 2002"))
            self.comboBox_section.setItemText(2, _translate("MainWindow", "Section 2003"))
            self.comboBox_section.setItemText(3, _translate("MainWindow", "Section 2004"))
            self.comboBox_section.setItemText(4, _translate("MainWindow", "Section 2005"))
            self.comboBox_section.setItemText(5, _translate("MainWindow", "Section 2006"))

    ## self.version_student.isSignalConnected(self.close_win())

    def view_attendance_btn_clicked (self):
        # total=0
        # show=0
        # absent=0
        # self.display_show_up()
        # self.display_absent()
        absentstr = Python_DB.absent(101, 1001)
        self.listWidget_2.addItem(absentstr)
        # total=100*show/absent
        # print("Percentage = "+total)
        # self.Percentage.setProperty("value",total)

    def display_show_up(self):
        # filename = QFileDialog.getOpenFileName()
        # show=0
        # listInfo=[]
        path = 'C:/capstone/studentpage/show_up.txt'
        # print(path)
        # This is how to read a file
        with open(path,"r") as f:
            for listitem in f:
                # content=listitem
                # listInfo.append(content)
                # show=show+1
                print(listitem)
        # rself.updateShowUp(listInfo)

    # def updateShowUp(self,listInfo):
    #     self.lineEdit.setText('1111')
    #     self.lineEdit1.setText('2222')
    #     self.lineEdit2.setText('333')


    def display_absent(self):
        # absent=0
        # filename = QFileDialog.getOpenFileName()
        path = 'C:/capstone/studentpage/absent.txt'
        # print(path)
        # This is how to read a file
        with open(path, "r") as f:
            for listitem in f:
                # absent=absent+1
                print(listitem)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow1()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

import MAC_rc
