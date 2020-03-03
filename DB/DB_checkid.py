import psycopg2

def checkid(studentid,lectureid):
    try:
        connection = psycopg2.connect(database="profmate", user="python", password="python", \
                                      host="34.74.217.167", port="5432", sslmode="require", \
                                      sslcert="ssl-cert.crt", sslkey="ssl-key.key")
        cursor = connection.cursor()
        postgreSQL_select_Query ="select count(1) from lec_%s\
		where student_id = %s;"

        cursor.execute(postgreSQL_select_Query,(lectureid,studentid))
        print("Selecting rows from POOL table using cursor.fetchall")
        current_table = cursor.fetchall()
        for row in current_table:
            print(" Existence", row[0])

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
    # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

student = 1402794
section = 101
checkid(student,section)
