import os
import sys
import psycopg2

def connectPostgreSQL():
    conn = psycopg2.connect(database="profmate", user="admin", password="admin", host="34.74.217.167", port="5432")
    print ('connect successful!')
if __name__=='__main__':
    connectPostgreSQL()