import psycopg2
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
		Select percentage from sections\
		where SectionID ='%s'; "

		cursor.execute(postgreSQL_update_Query,(sectionid,sectionid,sectionid))
		print("Selecting rows from POOL table using cursor.fetchall")
		current_table = cursor.fetchall()

		print("Print each row and it's columns values")
		for row in current_table:
			print("Percentage = ", row[0])
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

#test case
#attendancepercent(1001)