#!/usr/bin/env python2.7

import os
import json
from flask import Flask
import mysql.connector

DB_USR = os.getenv('DB_USR', 'newsworld')
DB_PASS = os.environ.get('DB_PASS', 'Newsworld0')
DB_HOST = os.environ.get('DB_HOST', 'kim.antoinegiraudmaillet.com')
DB_DB = os.environ.get('DB_DB', 'newsworld')

app = Flask(__name__)
cnx = mysql.connector.connect(user=DB_USR,
                              password=DB_PASS,
                              host=DB_HOST,
                              database=DB_DB)
print cnx

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/countrynews/<hours>")
def country_news(hours=24):
    print hours
    cursor = cnx.cursor()
    query = "SELECT country_code as country, COUNT(id) as count "
    query += "FROM country_news_table "
    query += "WHERE publish_date > DATE_SUB(NOW(), INTERVAL {} HOUR) ".format(hours)
    query += "GROUP BY country_code;"
    cursor.execute(query)
    response = {}

    for (country, count) in cursor:
        response[country] = count
    return json.dumps(response)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
