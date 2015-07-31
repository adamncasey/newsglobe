#!/bin/python

import os
from flask import Flask
import mysql.connector

DB_USR = os.getenv('DB_USR', 'newsglobe')
DB_PASS = os.environ.get('DB_PASS', 'test')
DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_DB = os.environ.get('DB_DB', 'newsglobe')

app = Flask(__name__)
cnx = mysql.connector.connect(user=DB_USR,
                              password=DB_PASS,
                              host=DB_HOST,
                              database=DB_DB)
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

@app.route("/countrynews")
def country_news():
    return "stuff"

cnx.close()
