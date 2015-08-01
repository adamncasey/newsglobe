__author__ = 'steffenschmidt'

import json
from db_auth import db_auth
import sqlite3
import dateutil.parser
import mysql.connector

import time as _time
class DB_Handler:






    def insert_country(self,country_code, time, link, source, title):

        # cursor = conn.execute("SELECT ID FROM news_country_table ORDER BY ID DESC").fetchone()
        # print cursor
        # if(cursor is None):
        #     id = 0
        # else:
        #     id = int(str(cursor)[1:2]) + 1
        conn =  mysql.connector.connect(user="newsworld",
                       password="Newsworld0",
                      host="kim.antoinegiraudmaillet.com",
                      database="newsworld")
        cursor = conn.cursor()
        time = dateutil.parser.parse(time);
        time = _time.mktime((time.year, time.month, time.day,time.hour, time.minute, time.second,-1, -1, -1))
        query = "INSERT INTO country_news_table VALUES (NULL, %s, FROM_UNIXTIME(%s), %s, %s, %s)"
        entry = (country_code, time, link, source, title)
        cursor.execute(query, entry)
        conn.commit()

    def insert_update(self,source, time):
        conn = mysql.connector.connect(host="kim.antoinegiraudmaillet.com", user="newsworld", passwd="Newsworld0", db="newsworld")
        cursor = conn.cursor()
        query = "INSERT INTO latest_update_table VALUES ( %s, FROM_UNIXTIME(%s))"
        time = dateutil.parser.parse(time)
        time = _time.mktime((time.year, time.month, time.day,time.hour, time.minute, time.second,-1, -1, -1))
        print time
        entry = (source, time)


        cursor.execute(query, entry)
        conn.commit()

    def insert_update(self,source, time):
        conn = mysql.connector.connect(host="kim.antoinegiraudmaillet.com", user="newsworld", passwd="Newsworld0", db="newsworld")
        cursor = conn.cursor()
        query = "UPDATE latest_update_table SET source = %s WHERE time = FROM_UNIXTIME(%s)"
        time = dateutil.parser.parse(time)
        time = _time.mktime((time.year, time.month, time.day,time.hour, time.minute, time.second,-1, -1, -1))
        print time
        entry = (source, time)


        cursor.execute(query, entry)
        conn.commit()

    def get_last_update(self,source):

        conn = mysql.connector.connect(host="kim.antoinegiraudmaillet.com", user="newsworld", passwd="Newsworld0", db="newsworld")
        cursor = conn.cursor()
        source = (source,)

        query = "SELECT time FROM latest_update_table WHERE source = %s"
        entry = (source)
        last_update = cursor.execute(query, entry)

        if last_update is None:
            return None

        for row in cursor:
            print "ROW:" + str(row[0])
            time = _time.mktime((row[0].year, row[0].month, row[0].day
                             ,row[0].hour, row[0].minute, row[0].second,-1, -1, -1))
        print time
        return time

    def delete_from_update(self):

        conn = mysql.connector.connect(host="kim.antoinegiraudmaillet.com", user="newsworld", passwd="Newsworld0", db="newsworld")
        cursor = conn.cursor()
        query = "DELETE FROM latest_update_table"

        last_update = cursor.execute((query))
        print last_update
        # return cursor

    def delete_from_news(self):

        conn = mysql.connector.connect(host="kim.antoinegiraudmaillet.com", user="newsworld", passwd="Newsworld0", db="newsworld")
        cursor = conn.cursor()
        query = "DELETE FROM country_news_table"

        last_update = cursor.execute((query))
        print last_update
#timing = datetime.datetime(1991,5,7,3,0,0);
#insert_country('GE',1,str(timing),'abc')


