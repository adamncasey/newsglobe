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

def cnn_subscriber(cnn_url, source):

    d = feedparser.parse(cnn_url)

    cnn_top_json = [];
    for entry in d.entries:
        print entry
        timestamp = cnn_time_parser(entry.published_parsed)
        link = entry.links.pop().href
        summary =  entry.summary_detail.value
        title = entry.title
        base_source = entry.summary_detail.base
        temp_json = json.dumps({'timestamp': timestamp, 'link':link, 'summary': summary, 'title': title,
                                'base_source': base_source, 'source': source })
        cnn_top_json.append(temp_json)

    return cnn_top_json

print cnn_subscriber('http://rss.cnn.com/rss/edition.rss', 'cnn_top')
print cnn_subscriber('http://rss.cnn.com/rss/edition_world.rss', 'cnn_world')
print cnn_subscriber('http://rss.cnn.com/rss/edition_africa.rss', 'cnn_africa')
print cnn_subscriber('http://rss.cnn.com/rss/edition_americas.rss', 'cnn_americas')
print cnn_subscriber('http://rss.cnn.com/rss/edition_asia.rss', 'cnn_asia')
print cnn_subscriber('http://rss.cnn.com/rss/edition_europe.rss', 'cnn_europe')
print cnn_subscriber('http://rss.cnn.com/rss/edition_meast.rss', 'cnn_middle_east')
print cnn_subscriber('http://rss.cnn.com/rss/edition_us.rss', 'cnn_us')
print cnn_subscriber('http://rss.cnn.com/rss/money_news_international.rss', 'cnn_money')
print cnn_subscriber('http://rss.cnn.com/rss/edition_technology.rss', 'cnn_technology')
print cnn_subscriber('http://rss.cnn.com/rss/edition_space.rss', 'cnn_space')
print cnn_subscriber('http://rss.cnn.com/rss/edition_entertainment.rss', 'cnn_entertainment')
print cnn_subscriber('http://rss.cnn.com/rss/edition_sport.rss', 'cnn_sport')
print cnn_subscriber('http://rss.cnn.com/rss/edition_football.rss', 'cnn_soccer')
print cnn_subscriber('http://rss.cnn.com/rss/edition_golf.rss', 'cnn_golf')
print cnn_subscriber('http://rss.cnn.com/rss/edition_motorsport.rss', 'cnn_motorsport')
print cnn_subscriber('http://rss.cnn.com/rss/edition_tennis.rss', 'cnn_tennis')
print cnn_subscriber('http://travel.cnn.com/rss.xml', 'cnn_travel')
print cnn_subscriber('http://rss.cnn.com/rss/cnn_latest.rss', 'cnn_latest')
print cnn_subscriber('http://rss.cnn.com/rss/edition_connecttheworld.rss', 'cnn_ctw')
print cnn_subscriber('http://rss.cnn.com/rss/edition_worldsportblog.rss', 'cnn_world_sport')
