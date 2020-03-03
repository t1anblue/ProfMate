# # -*- coding: utf-8 -*-
#
# """
# Py40 PyQt5 tutorial
#
# This example shows three labels on a window
# using absolute positioning.
#
# author: Jan Bodnar
# website: py40.com
# last edited: January 2015
# """
#
# import sys
# from PyQt5.QtWidgets import QWidget, QLabel, QApplication
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         lbl1 = QLabel('Zetcode', self)
#         lbl1.move(15, 10)
#
#         lbl2 = QLabel('tutorials', self)
#         lbl2.move(35, 40)
#
#         lbl3 = QLabel('for programmers', self)
#         lbl3.move(55, 70)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Absolute')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
import psycopg2

def absent(lectureid,sectionid):
    connection = psycopg2.connect(database="profmate", user="python", password="python", host="34.74.217.167",
                              port="5432")
    cursor = connection.cursor()
    postgreSQL_select_Query ="select * from lec_%s \
            where student_id not in (select base.studentid\
            from (select S.SectionID,Lectures.Lecture_Name,P.StudentID\
            from Sections As S\
            Join POOL as P\
            On (P.Time > S.Time_Start)\
            and (P.Time < S.Time_End)\
            Join Lectures\
            ON S.LectureID = Lectures.Lecture_ID\
            Order By SectionID) as base\
            join Students \
            ON base.studentid = Students.Student_ID\
            where sectionid = '%s' );"

    cursor.execute(postgreSQL_select_Query,(lectureid,sectionid))
    print("Selecting rows from POOL table using cursor.fetchall")
    current_table = cursor.fetchall()

    print("Print each row and it's columns values")

    longstring = str('')
    for row in current_table:
        # print("Student ID = ", row[0])
        # print("Family Name = ", row[1])
        # print("Given Name = ", row[2], "\n")
        longstring = "".join((longstring, "Student ID = ",str(row[0]),"\n"))
        longstring = "".join((longstring, "Family Name = ", row[1], "\n"))
        longstring = "".join((longstring, "Given Name = ", row[2], "\n"))

    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
    return longstring

if __name__ == '__main__':
    a = '234567890'
    b = 'Tester'
    c = 'One'
    # insert_students(a, b, c)
    print(absent(101, 1001))