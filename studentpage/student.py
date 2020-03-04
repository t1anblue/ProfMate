# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from picamera import PiCamera
from V1 import *
import Camera

sys.path.append('/home/pi/Desktop/ProfMate/')
import MainController
import database

#***************Unpleasent Bkend Modifications******************


student_info = []
camera = PiCamera()

# def generate_txt_do():
#     f = open('student_info.txt', 'wb')
#     f.write('h')
#     f.close()
# class filewrite:
#         file = open("student_info.txt", "w+")
#         for i in range(len(student_info)):
#             file.write(student)

class Ui_MainWindow(object):

    def takePhoto_btn_clicked(self):
        alert = QMessageBox()
        alert.setText("Smile!")
        Camera.take_picture(camera)
        path = '/home/pi/Desktop/ProfMate/pic.jpg'
        student_info.append(path)
        alert.exec_()


    def upload_confirm(self):

        self.pixmap = QtGui.QPixmap("checkMark.jpg")
        self.pixmap1 = self.pixmap.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
        self.confirm_logo.setPixmap(self.pixmap1)


    def upload_photo_button_clicked(self):

        student_info.clear()
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        # print(path)
        student_info.append(path)
        alert = QMessageBox()
        alert.setText("Photo uploaded successfully.")
        alert.exec_()
        self.upload_confirm()


        # This is how to read a file
        # with open(path,"r") as f:
        #     print(f.readline())

    def create_button_clicked(self):

        alert = QMessageBox()
        alert.setText("Account created successfully.")
        alert.exec_()

        student_info.append(self.firstName_Text.text())
        student_info.append(self.lastName_Text.text())
        student_info.append(self.studentID_Text.text())
        student_info.append(self.comboBox_course.currentText())

        with open("/home/pi/Desktop/ProfMate/student_info.txt",'w+') as filehandler:
            for listitem in student_info:
                filehandler.write('%s\n' % listitem)
            filehandler.close()
        # *******************Modified*************************

        #MainController.registration_controller()
        
        print('Finished')
        



    def switch_page1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setup(self.window)
        self.window.show()
        # MainWindow.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menubar.setObjectName("menubar")
        self.version = self.menubar.addMenu("go to")
        self.version_professor = QAction('Professor', self.version)
        self.version.addAction(self.version_professor)
        self.version_professor.triggered.connect(self.switch_page1)




        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 430, 421, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.upload_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.upload_btn.setObjectName("upload_btn")
        self.horizontalLayout_4.addWidget(self.upload_btn)
        self.create_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.create_btn.setObjectName("create_btn")

        self.confirm_logo = QtWidgets.QLabel(self.centralwidget)
        self.confirm_logo.setGeometry(QtCore.QRect(155, 410, 70, 70))
        self.confirm_logo.setText("")
        self.pixmap = QtGui.QPixmap()
        self.pixmap1 = self.pixmap.scaled(30,30,QtCore.Qt.KeepAspectRatio)
        self.confirm_logo.setPixmap(self.pixmap1)

        self.confirm_logo.setObjectName("logo2")



        self.horizontalLayout_4.addWidget(self.create_btn)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(180, 80, 462, 180))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("profmate_logo.png"))

        self.logo.setObjectName("logo")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(290, 300, 210, 94))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.firstName_Label = QtWidgets.QLabel(self.layoutWidget_2)
        self.firstName_Label.setObjectName("firstName_Label")
        self.horizontalLayout.addWidget(self.firstName_Label)
        self.firstName_Text = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.firstName_Text.setText("")
        self.firstName_Text.setObjectName("firstName_Text")
        self.horizontalLayout.addWidget(self.firstName_Text)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lastName_Label = QtWidgets.QLabel(self.layoutWidget_2)
        self.lastName_Label.setObjectName("lastName_Label")
        self.horizontalLayout_2.addWidget(self.lastName_Label)
        self.lastName_Text = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lastName_Text.setObjectName("lastName_Text")
        self.horizontalLayout_2.addWidget(self.lastName_Text)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.studentID_Label = QtWidgets.QLabel(self.layoutWidget_2)
        self.studentID_Label.setObjectName("studentID_Label")
        self.horizontalLayout_3.addWidget(self.studentID_Label)
        self.studentID_Text = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.studentID_Text.setObjectName("studentID_Text")
        self.horizontalLayout_3.addWidget(self.studentID_Text)
        self.verticalLayout.addLayout(self.horizontalLayout_3)



        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.course_Label = QtWidgets.QLabel(self.layoutWidget_2)
        self.course_Label.setObjectName("course_Label_2")
        self.horizontalLayout_6.addWidget(self.course_Label)
        self.comboBox_course = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_course.setObjectName("comboBox")
        self.comboBox_course.addItem("")
        self.comboBox_course.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_course)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.takePhoto_btn = QtWidgets.QPushButton(self.centralwidget)
        self.takePhoto_btn.setGeometry(QtCore.QRect(40, 130, 93, 28))
        self.takePhoto_btn.setObjectName("takePhoto_btn")

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
        # self.toProfessor_btn.setText(_translate("MainWindow", "Go to Pro page"))
        self.upload_btn.setText(_translate("MainWindow", "Upload Photo"))
        self.upload_btn.clicked.connect(self.upload_photo_button_clicked)
        self.create_btn.setText(_translate("MainWindow", "Create"))
        self.create_btn.clicked.connect(self.create_button_clicked)
        self.firstName_Label.setText(_translate("MainWindow", "First Name"))
        self.lastName_Label.setText(_translate("MainWindow", "Last Name"))
        self.studentID_Label.setText(_translate("MainWindow", "Student ID"))

        self.takePhoto_btn.setText(_translate("MainWindow", "Take a photo"))
        self.takePhoto_btn.clicked.connect(self.takePhoto_btn_clicked)

        self.course_Label.setText(_translate("MainWindow", "Course Code"))
        self.comboBox_course.setItemText(0, _translate("MainWindow", "ENG_4OI6B"))
        self.comboBox_course.setItemText(1, _translate("MainWindow", "COMPENG_4TL4"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
