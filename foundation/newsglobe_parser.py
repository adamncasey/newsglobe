__author__ = 'alexandrecornet'

import csv

class Parser:

    def __init__(self):
        dataBase = open('countries.csv', 'rb')
        reader = csv.reader(dataBase, delimiter=';')
        self.table = {}
        for country in reader:
            for city in country:
                if city!='':
                    self.table[city.lower()]=country[0].lower()

    def process(self, news):
        news['countries'] = []

        title = news['title'].split(' ')
        summary = news['summary'].split(' ')

        for string in [title, summary]:
            for word in string:
                if  word.lower() in self.table.keys():
                    news['countries'].append(self.table[word.lower()])