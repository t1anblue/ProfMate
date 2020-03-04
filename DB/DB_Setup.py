import os
import sys
import psycopg2

def connectPostgreSQL():
    connection = psycopg2.connect(database="profmate", user="python", password="python", \
    host = "34.74.217.167", port = "5432", sslmode = "require",\
    sslcert = "ssl-cert.crt", sslkey = "ssl-key.key")
    print ('connect successful!')
if __name__=='__main__':
    connectPostgreSQL()
