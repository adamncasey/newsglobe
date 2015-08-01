#!/usr/bin/env python2.7

import os
import os.path
import json
from flask import Flask, send_from_directory
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
parent_dir = os.path.abspath(
    os.path.join(os.path.join(os.path.realpath(__file__), os.pardir), os.pardir))
print parent_dir
print cnx

@app.route('/ext/<path:path>')
def send_js(path):
    return send_from_directory('{}/frontend/'.format(parent_dir), path)


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
