__author__ = 'steffenschmidt'

import json
from db_auth import db_auth
import sqlite3
#import datetime
#import pymysql.cursors

def insert_country(country_code, id, publish_date, link):
    auth = db_auth()



conn = sqlite3.connect('DB')
cursor = conn.execute("SELECT ID FROM news_country_table ORDER BY ID DESC").fetchone()
print cursor
if(cursor is None):
    id = 0
else:
    id = int(str(cursor)[1:2]) + 1
print id
conn.execute("INSERT INTO news_country_table VALUES ('GB',1000," + str(id) + ")")
conn.commit()
#timing = datetime.datetime(1991,5,7,3,0,0);
#insert_country('GE',1,str(timing),'abc')


