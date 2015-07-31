__author__ = 'alexandrecornet'

import csv

class Parser:

    def __init__(self):
        dataBase = open('countries.csv', 'rb')
        reader = csv.reader(dataBase, delimiter=';')
        self.table = {}
        for country in reader:
            isCountryName = 1
            for city in country:
                if isCountryName==0:
                    if city!='':
                        self.table[city]=country[0]
                isCountryName=0