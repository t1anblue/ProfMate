import psycopg2

def absent(lectureid,sectionid):
    try:
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
        for row in current_table:
            print("Student ID = ", row[0])
            print("Family Name = ", row[1])
            print("Given Name = ", row[2], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
    # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# test function

lectureid = 101
sectionid = 1001
absent(lectureid,sectionid)