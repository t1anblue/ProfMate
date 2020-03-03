import psycopg2

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

#function test
studentid = '001402794'
date = '2020-Feb-20'
time = '21:17:11'
insertpool(studentid,date,time)
