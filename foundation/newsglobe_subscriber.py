__author__ = 'steffenschmidt'

import feedparser
import csv
import json
from newsglobe_parser import Parser
from newsglobe_uploader import DB_Handler
import dateutil.parser

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

def bbc_time_parser(timestamp):
    timestamp = dateutil.parser.parse(timestamp)

    timestamp = int(timestamp.year) * 31556926 + int(timestamp.month) * 2629744 + int(timestamp.day) * 86400 + \
                   int(timestamp.hour) * 3600 + int(timestamp.minute) * 60 + int(timestamp.second)
    return timestamp


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


def bbc_subscriber(bbc_url, source):
    handler = DB_Handler()
    d = feedparser.parse(bbc_url)


    timestamp = bbc_time_parser(d.feed.updated)
    print "Timestamp: " + str(timestamp)
    current_update = timestamp
    print source
    print d
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

def guardian_subscriber(guardian_url, source):

    handler = DB_Handler()
    d = feedparser.parse(guardian_url)
    print d

    timestamp = bbc_time_parser(d.feed.updated)
    print "Timestamp: " + str(timestamp)
    current_update = timestamp

    last_update = handler.get_last_update(source)
    # # pos = str(last_update).find(',')
    # # last_update = last_update[1:pos]
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
        handler.insert_country(source,timestamp,link)

        # summary =  entry.summary_detail.value
        # title = entry.title
        # base_source = entry.summary_detail.base
        # temp_json = {'timestamp': timestamp, 'link':link, 'summary': summary, 'title': title,
        #                         'base_source': base_source, 'source': source }
        # parser = Parser()
        # parser.process(temp_json)
        # cnn_top_json.append(temp_json)

    return


cnn_subscriber('http://rss.cnn.com/rss/edition.rss', 'cnn_top')
cnn_subscriber('http://rss.cnn.com/rss/edition_world.rss', 'cnn_world')
cnn_subscriber('http://rss.cnn.com/rss/edition_africa.rss', 'cnn_africa')
cnn_subscriber('http://rss.cnn.com/rss/edition_americas.rss', 'cnn_americas')
cnn_subscriber('http://rss.cnn.com/rss/edition_asia.rss', 'cnn_asia')
cnn_subscriber('http://rss.cnn.com/rss/edition_europe.rss', 'cnn_europe')
cnn_subscriber('http://rss.cnn.com/rss/edition_meast.rss', 'cnn_middle_east')
cnn_subscriber('http://rss.cnn.com/rss/edition_us.rss', 'cnn_us')
# cnn_subscriber('http://rss.cnn.com/rss/money_news_international.rss', 'cnn_money')
# cnn_subscriber('http://rss.cnn.com/rss/edition_technology.rss', 'cnn_technology')
# cnn_subscriber('http://rss.cnn.com/rss/edition_space.rss', 'cnn_space')
# cnn_subscriber('http://rss.cnn.com/rss/edition_entertainment.rss', 'cnn_entertainment')
# cnn_subscriber('http://rss.cnn.com/rss/edition_sport.rss', 'cnn_sport')
# cnn_subscriber('http://rss.cnn.com/rss/edition_football.rss', 'cnn_soccer')
# cnn_subscriber('http://rss.cnn.com/rss/edition_golf.rss', 'cnn_golf')
# cnn_subscriber('http://rss.cnn.com/rss/edition_motorsport.rss', 'cnn_motorsport')
# cnn_subscriber('http://rss.cnn.com/rss/edition_tennis.rss', 'cnn_tennis')
# cnn_subscriber('http://rss.cnn.com/rss/cnn_latest.rss', 'cnn_latest')

# bbc_subscriber('http://feeds.bbci.co.uk/news/rss.xml', 'bbc_top')
# bbc_subscriber('http://feeds.bbci.co.uk/news/world/rss.xml', 'bbc_world')
# bbc_subscriber('http://feeds.bbci.co.uk/news/business/rss.xml', 'bbc_business')
# bbc_subscriber('http://feeds.bbci.co.uk/news/science_and_environment/rss.xml', 'bbc_environment')
# bbc_subscriber('http://feeds.bbci.co.uk/news/technology/rss.xml', 'bbc_technology')
# bbc_subscriber('http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'bbc_entertainment')
# bbc_subscriber('http://feeds.bbci.co.uk/news/world/africa/rss.xml', 'bbc_afrika')
# bbc_subscriber('http://feeds.bbci.co.uk/news/world/asia/rss.xml', 'bbc_asia')
# bbc_subscriber('http://feeds.bbci.co.uk/news/world/europe/rss.xml', 'bbc_europe')
# bbc_subscriber('http://feeds.bbci.co.uk/news/world/latin_america/rss.xml', 'bbc_latin_america')
# bbc_subscriber('http://feeds.bbci.co.uk/news/world/middle_east/rss.xml', 'bbc_middle_east')
# bbc_subscriber('http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml', 'bbc_us_canada')
dataBase = open('countries.csv', 'rb')
reader = csv.reader(dataBase, delimiter=';')
for country in reader:
    print country[0].lower()
    guardian_subscriber('http://www.theguardian.com/world/' + country[0].lower() + '/rss', country[0].lower())