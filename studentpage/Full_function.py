import psycopg2

def addstudent(student_id,family_name,given_name)
	try:
		connection = psycopg2.connect(database="profmate", user="python", password="python",\
		host="34.74.217.167", port="5432", sslmode="require",\
		sslcert="ssl-cert.crt", sslkey="ssl-key.key")
		cursor = connection.cursor()
		postgreSQL_insert_Query = "insert into students(student_id,family_name,given_name)\
		Values(%s,%s,%s);"
		record_to_insert = (student_id,family_name,given_name)
		cursor.execute(postgreSQL_insert_Query, record_to_insert)

		connection.commit()
		count = cursor.rowcount
		print (count, "Record inserted successfully into Students table")

	except (Exception, psycopg2.Error) as error :
		if(connection):
			print("Failed to insert record into Students table", error)

	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

def insertpool(studentid,date,time):
    try:
        connection = psycopg2.connect(database="profmate", user="python", password="python",\
		host="34.74.217.167", port="5432", sslmode="require",\
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

#function test
#studentid = '001402794'
#date = '2020-Feb-29'
#time = '21:17:10'
#insertpool(studentid,date,time)



def register(student_id, family_name,given_name,lectureid):
    try:
        
		connection = psycopg2.connect(database="profmate", user="python", password="python",\
		host="34.74.217.167", port="5432", sslmode="require",\
		sslcert="ssl-cert.crt", sslkey="ssl-key.key")
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

#Testing			
#student_id = 1314
#family_name = 'onethree'
#given_name = 'onefour'
#lectureid = 101
#regist(student_id, family_name, given_name, lectureid)



def absent(lectureid,sectionid):
    try:
		connection = psycopg2.connect(database="profmate", user="python", password="python",\
		host="34.74.217.167", port="5432", sslmode="require",\
		sslcert="ssl-cert.crt", sslkey="ssl-key.key")
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

#lectureid = 101
#sectionid = 1001
#absent(lectureid,sectionid)



#update the attendance percentage in database with the section ID
def attendancepercent(sectionid):
	try:
		
		connection = psycopg2.connect(database="profmate", user="python", password="python",\
		host="34.74.217.167", port="5432", sslmode="require",\
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

		cursor.execute(postgreSQL_update_Query,(sectionid,sectionid,sectionid))

		connection.commit()
		count = cursor.rowcount
		print(count, "Record Updated successfully ")


        current_table = cursor.fetchall()

        print("Print each row and it's columns values")
        print(current_table)


	except (Exception, psycopg2.Error) as error:
		print("Error while fetching data from PostgreSQL", error)

	finally:
	# closing database connection.
		if (connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

