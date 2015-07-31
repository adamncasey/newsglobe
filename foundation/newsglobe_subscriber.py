__author__ = 'steffenschmidt'

import feedparser

d = feedparser.parse('http://rss.cnn.com/rss/edition.rss');
print(d['feed']);
print d.entries;
for entry in d.entries:
    print entry.published_parsed
    print entry.published_parsed.find
