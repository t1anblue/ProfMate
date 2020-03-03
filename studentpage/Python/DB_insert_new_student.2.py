import psycopg2

try:
    connection = psycopg2.connect(database="profmate", user="python", password="python", host="34.74.217.167", port="5432")
    cursor = connection.cursor()
    postgreSQL_insert_Query = "insert into students(student_id,family_name,given_name)\
    Values(%s,%s,%s);"
    record_to_insert = ('119','Tester','NoName')
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