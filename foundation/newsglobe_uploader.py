__author__ = 'steffenschmidt'

import json
from db_auth import db_auth
#import MySQLdb
import datetime
import pymysql.cursors


def connect_db():

    return

def insert_country(country_code, id, publish_date, link):
    auth = db_auth()


# Connect to the database
    connection = pymysql.connect(host='remi.ee.ethz.ch',
                                user='steffsch',
                                password='-AJaRPLr',
                                db='steffsch',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    query = "INSERT INTO country_news_table " \
            "VALUES(%s,%i,%s,%s)"
    args = (country_code, id, publish_date, link)



    print "Connect" + cursor.execute(query, args)


timing = datetime.datetime(1991,5,7,3,0,0);
insert_country('GE',1,str(timing),'abc')


