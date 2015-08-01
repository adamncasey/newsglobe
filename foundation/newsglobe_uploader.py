__author__ = 'steffenschmidt'

import json
from db_auth import db_auth
import sqlite3
#import datetime
import MySQLdb


class DB_Handler:
    def insert_country(self,country_code, time, link):
        conn = MySQLdb.connect(host="kim.antoinegiraudmaillet.com", user="newsworld", passwd="Newsworld0", db="newsworld")
        # cursor = conn.execute("SELECT ID FROM news_country_table ORDER BY ID DESC").fetchone()
        # print cursor
        # if(cursor is None):
        #     id = 0
        # else:
        #     id = int(str(cursor)[1:2]) + 1

        entry = [(country_code, time, link)]
        conn.executemany("INSERT INTO country_news_table VALUES ( %s, %s, %s)", entry)
        conn.commit()

    def insert_update(self,source, time):
        conn = MySQLdb.connect(host="kim.antoinegiraudmaillet.com", user="newsworld", passwd="Newsworld0", db="newsworld")


        entry = [(source, time)]
        conn.executemany("INSERT INTO last_update_table VALUES ( ?, ?)", entry)
        conn.commit()

    def get_last_update(self,source):
        conn = MySQLdb.connect(host="kim.antoinegiraudmaillet.com", user="newsworld", passwd="Newsworld0", db="newsworld")
        source = (source,)
        cursor = conn.execute("SELECT last_update FROM last_update_table WHERE source = ?", source).fetchone()
        print cursor
        # return cursor

#timing = datetime.datetime(1991,5,7,3,0,0);
#insert_country('GE',1,str(timing),'abc')


