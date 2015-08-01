__author__ = 'steffenschmidt'

import feedparser
import json
from newsglobe_parser import Parser
from newsglobe_uploader import DB_Handler

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

    #  year
    #  month
    #  day
    #  hour
    #  minute
    #  second
    return {'year': year, 'month': month, 'day':day, 'hour':hour, 'min': minute, 'sec': second};

def cnn_subscriber(cnn_url, source):
    handler = DB_Handler()
    d = feedparser.parse(cnn_url)
    print d.feed.published_parsed

    timestamp = cnn_time_parser(d.feed.published_parsed)
    print "Timestamp: " + str(timestamp)
    current_update = int(timestamp['year']) * 31556926 + int(timestamp['month']) * 2629744 + int(timestamp['day']) * 86400 + \
                   int(timestamp['hour']) * 3600 + int(timestamp['min']) * 60 + int(timestamp['sec'])
    print source
    last_update = handler.get_last_update(source)
    # pos = str(last_update).find(',')
    # last_update = last_update[1:pos]
    if last_update is not None:
        pos_back = str(last_update).find(",")
        last_update = int(str(last_update)[1:pos_back])

    if last_update == current_update:
        return

    handler.insert_update(source, current_update)
    cnn_top_json = [];
    for entry in d.entries:

        timestamp = cnn_time_parser(entry.published_parsed)
        link = entry.links.pop().href
        summary =  entry.summary_detail.value
        title = entry.title
        base_source = entry.summary_detail.base
        temp_json = {'timestamp': timestamp, 'link':link, 'summary': summary, 'title': title,
                                'base_source': base_source, 'source': source }
        parser = Parser()
        parser.process(temp_json)
        cnn_top_json.append(temp_json)

    return cnn_top_json


cnn_subscriber('http://rss.cnn.com/rss/edition.rss', 'cnn_top')
cnn_subscriber('http://rss.cnn.com/rss/edition_world.rss', 'cnn_world')
cnn_subscriber('http://rss.cnn.com/rss/edition_africa.rss', 'cnn_africa')
cnn_subscriber('http://rss.cnn.com/rss/edition_americas.rss', 'cnn_americas')
cnn_subscriber('http://rss.cnn.com/rss/edition_asia.rss', 'cnn_asia')
cnn_subscriber('http://rss.cnn.com/rss/edition_europe.rss', 'cnn_europe')
cnn_subscriber('http://rss.cnn.com/rss/edition_meast.rss', 'cnn_middle_east')
cnn_subscriber('http://rss.cnn.com/rss/edition_us.rss', 'cnn_us')
cnn_subscriber('http://rss.cnn.com/rss/money_news_international.rss', 'cnn_money')
cnn_subscriber('http://rss.cnn.com/rss/edition_technology.rss', 'cnn_technology')
cnn_subscriber('http://rss.cnn.com/rss/edition_space.rss', 'cnn_space')
cnn_subscriber('http://rss.cnn.com/rss/edition_entertainment.rss', 'cnn_entertainment')
cnn_subscriber('http://rss.cnn.com/rss/edition_sport.rss', 'cnn_sport')
cnn_subscriber('http://rss.cnn.com/rss/edition_football.rss', 'cnn_soccer')
cnn_subscriber('http://rss.cnn.com/rss/edition_golf.rss', 'cnn_golf')
cnn_subscriber('http://rss.cnn.com/rss/edition_motorsport.rss', 'cnn_motorsport')
cnn_subscriber('http://rss.cnn.com/rss/edition_tennis.rss', 'cnn_tennis')
cnn_subscriber('http://rss.cnn.com/rss/cnn_latest.rss', 'cnn_latest')

