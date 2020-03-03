import psycopg2

try:
    connection = psycopg2.connect(database="profmate", user="python", password="python", host="34.74.217.167", port="5432")
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
	where SectionID ='1001')\
	where SectionID ='1001';"

    cursor.execute(postgreSQL_update_Query)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record Updated successfully ")


except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
# closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
