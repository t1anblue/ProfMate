import psycopg2

def check_lec_att(lectureid):
    try:
        connection = psycopg2.connect(database="profmate", user="python", password="python", \
                                      host="34.74.217.167", port="5432", sslmode="require", \
                                      sslcert="ssl-cert.crt", sslkey="ssl-key.key")
        cursor = connection.cursor()
        postgreSQL_select_Query ="select sectionid,date,percentage from sections where lectureid = %s;"

        cursor.execute(postgreSQL_select_Query,(lectureid,))
        print("Selecting rows from table using cursor.fetchall")
        current_table = cursor.fetchall()
        for row in current_table:
            print("SectionID = ", row[0])
            print("Date= ", row[1])
            print("Attendance = ", row[2])
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
    # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#test
lecture_id = 101
check_lec_att(lecture_id)