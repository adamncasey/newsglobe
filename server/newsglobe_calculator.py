__author__ = 'alexandrecornet'

import datetime
import csv

class Calculator:

    def __init__(self):
        dataBase = open('countries.csv', 'rb')
        reader = csv.reader(dataBase, delimiter=';')
        self.countries = []
        for country in reader:
            name = country[0].lower()
            self.countries.append(name)

    def resetCount(self):
        self.count = {}
        for country in self.countries:
            self.count[country] = 0

    def computeCount(self, delta):
        outOfDate =  datetime.now() - delta
        for country in self.countries:
            times = []
            #times = db.get(country)
            for time in times:
                if time > outOfDate:
                    self.countries[country] += 1

    def scale(self):
        max = 0
        for x in self.count:
            if x > max:
                max = x

        for country in self.countries:
            self.count[country] /= max * 100
            