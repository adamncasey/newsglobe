__author__ = 'alexandrecornet'

import csv

def loadDictionnary():
    countries = open('countries.csv', 'rb')
    reader = csv.reader(countries, delimiter=';')

loadDictionnary()