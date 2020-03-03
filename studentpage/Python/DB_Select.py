import psycopg2

try:
    connection = psycopg2.connect(database="profmate", user="python", password="python", host="34.74.217.167", port="5432")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select base.sectionid,base.lecture_name,base.studentid,Students.Family_Name,Students.Given_Name\
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
    where sectionid = '1001';"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from POOL table using cursor.fetchall")
    current_table = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in current_table:
        print("SectionID = ", row[0], )
        print("Lecture Name = ", row[1])
        print("Student ID = ", row[2])
        print("Family Name = ", row[3])
        print("Given Name = ", row[4], "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")