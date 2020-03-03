#----------Connect to DB--------------

import os
import sys
import psycopg2


def register(student_id, family_name,given_name,lectureid):
    try:
        connection = psycopg2.connect(database="profmate", user="python", password="python", \
        host="34.74.217.167", port="5432", sslmode="require", \
        sslcert = "ssl-cert.crt", sslkey = "ssl-key.key")
        cursor = connection.cursor()
        postgreSQL_insert_Query = "insert into students(student_id,family_name,given_name)\
        Values(%s,%s,%s); \
        insert into lec_%s(student_id,family_name,given_name) values(%s,%s,%s);"

        record_to_insert = (student_id,family_name,given_name,lectureid,student_id,family_name,given_name)
        cursor.execute(postgreSQL_insert_Query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into Students table")

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record into table", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



#--------- 选择缺席学生-----#


def absent(lectureid,sectionid):
    try:
        connection = psycopg2.connect(database="profmate", user="python", password="python", \
        host="34.74.217.167", port="5432", sslmode="require", \
        sslcert = "ssl-cert.crt", sslkey = "ssl-key.key")
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

        long_string = ""
        for row in current_table:
            # print("Student ID = ", row[0])
            # print("Family Name = ", row[1])
            # print("Given Name = ", row[2], "\n")
            long_string = "".join((long_string, "Student ID = ",str(row[0]),"\n"))
            long_string = "".join((long_string, "Family Name = ", row[1], "\n"))
            long_string = "".join((long_string, "Given Name = ", row[2], "\n\n"))
        txt = open("absent.txt", "w")
        txt.write(long_string)
        txt.close()


    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
    # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            return long_string


#-------------insert into pool --------#


def insertpool(studentid,date,time):
    try:
        connection = psycopg2.connect(database="profmate", user="python", password="python", \
                                      host="34.74.217.167", port="5432", sslmode="require", \
                                      sslcert="ssl-cert.crt", sslkey="ssl-key.key")
        cursor = connection.cursor()
        postgreSQL_insert_Query = "insert into POOL(StudentID,Date,Time)\
        Values(%s,%s,%s);"
        # The new insert value add here:
        #  record_to_insert = ('001402794','2019-Nov-14','09:17:10')
        record_to_insert = (studentid,date,time)
        cursor.execute(postgreSQL_insert_Query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into pool table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into pool table", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# ************************************Modifications*************************************


def insert_students(student_id,family_name,given_name):
    try:
        connection = psycopg2.connect(database="profmate", user="python", password="python", \
                                      host="34.74.217.167", port="5432", sslmode="require", \
                                      sslcert="ssl-cert.crt", sslkey="ssl-key.key")
        cursor = connection.cursor()
        postgreSQL_insert_Query = "insert into students(student_id,family_name,given_name)\
        Values(%s,%s,%s);"
        # The new insert value add here:
        #  record_to_insert = ('001402794','2019-Nov-14','09:17:10')
        record_to_insert = (student_id,family_name,given_name)
        cursor.execute(postgreSQL_insert_Query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into students table")
        txt = open("insert_students.txt", "a")
        txt.write(" ".join(record_to_insert))
        txt.write("\n")
        txt.close()

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into students table", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def attendance(lectureid,sectionid):
    try:
        connection = psycopg2.connect(database="profmate", user="python", password="python", \
                                      host="34.74.217.167", port="5432", sslmode="require", \
                                      sslcert="ssl-cert.crt", sslkey="ssl-key.key")
        cursor = connection.cursor()
        postgreSQL_select_Query ="select * from lec_%s \
        where student_id in (select base.studentid\
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
        current_table = cursor.fetchall()

        long_string = ""
        for row in current_table:
            long_string = "".join((long_string, "Student ID = ",str(row[0]),"\n"))
            long_string = "".join((long_string, "Family Name = ", row[1], "\n"))
            long_string = "".join((long_string, "Given Name = ", row[2], "\n\n"))
        txt = open("present.txt", "w")
        txt.write(long_string)
        txt.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
    # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            return long_string


def attendance_percent(sectionid):
    try:

        connection = psycopg2.connect(database="profmate", user="python", password="python", \
                                      host="34.74.217.167", port="5432", sslmode="require", \
                                      sslcert="ssl-cert.crt", sslkey="ssl-key.key")
        cursor = connection.cursor()
        postgreSQL_update_Query = "update Sections\
            set Attendance =(select count(*) \
            from (select S.SectionID,Lectures.Lecture_Name,P.StudentID\
            from Sections As S\
            Join POOL as P\
            On (P.Time > S.Time_Start)\
            and (P.Time < S.Time_End)\
            Join Lectures\
            ON S.LectureID = Lectures.Lecture_ID\
            Order By SectionID) as DataPool\
            where SectionID ='%s')\
            where SectionID ='%s';\
            select percentage from sections \
            where SectionID = '%s';"

        cursor.execute(postgreSQL_update_Query, (sectionid, sectionid, sectionid))

        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        current_table = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in current_table:
            percent = row[0]


    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            return percent


#function test
if __name__ == '__main__':
    a = '234567890'
    b = 'Tester'
    c = 'One'
    print(attendance_percent(1001))
    # print(present(101, 1001))
