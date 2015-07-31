__author__ = 'steffenschmidt'

import feedparser
import json

def cnn_time_parser(cnn_time_stamp):
    string_stamp = str(cnn_time_stamp)
    pos_year = string_stamp.find('=')
    year = string_stamp[pos_year+1:pos_year+5]

    string_stamp = string_stamp[pos_year+1:]
    pos_month = string_stamp.find('=')

    if string_stamp[pos_month+2] == ",":
        month = string_stamp[pos_month+1:pos_month+2]

    else:
        month = string_stamp[pos_month+1:pos_month+3]

    string_stamp = string_stamp[pos_month+1:]
    pos_day = string_stamp.find('=')

    if string_stamp[pos_day+2] == ",":
        day = string_stamp[pos_day+1:pos_day+2]

    else:
        day = string_stamp[pos_day+1:pos_day+3]

    string_stamp = string_stamp[pos_day+1:]
    pos_hour = string_stamp.find('=')

    if string_stamp[pos_hour+2] == ",":
        hour = string_stamp[pos_hour+1:pos_hour+2]

    else:
        hour = string_stamp[pos_hour+1:pos_hour+3]

    string_stamp = string_stamp[pos_hour+1:]
    pos_min = string_stamp.find('=')

    if string_stamp[pos_min+2] == ",":
        minute = string_stamp[pos_min+1:pos_min+2]

    else:
        minute = string_stamp[pos_min+1:pos_min+3]

    string_stamp = string_stamp[pos_min+1:]
    pos_sec = string_stamp.find('=')

    if string_stamp[pos_sec+2] == ",":
        second = string_stamp[pos_sec+1:pos_sec+2]

    else:
        second = string_stamp[pos_sec+1:pos_sec+3]

    # print year
    # print month
    # print day
    # print hour
    # print minute
    # print second
    return json.dumps({'year': year, 'month': month, 'day':day, 'hour':hour, 'min': minute, 'sec': second});



d = feedparser.parse('http://rss.cnn.com/rss/edition.rss')
print(d['feed'])
print d.entries
for entry in d.entries:
    print entry
    timestamp = cnn_time_parser(entry.published_parsed)
    link = entry.links.pop().href
    print link




