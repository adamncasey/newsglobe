__author__ = 'alexandrecornet'

import csv
import string

def addIntoDict(filename):
    dict = loadOldDict()
    appendNewData(filename,dict)
    write(dict)


def loadOldDict():
    dict = open('countries.csv', 'rb')
    reader = csv.reader(dict, )
    dict = {}

    for country in reader:
        name = country[0]
        dict[name]=[]
        for word in country:
            if word!='':
                dict[name].append(word)
    return dict

def appendNewData(filename, dict):
    newDataFile = open(filename, 'rb')
    newData = csv.reader(newDataFile, delimiter=';')

    for country in newData:
        name = country[0]
        if name in dict.keys():
            appendRow(dict, country)
        else:
            print country[0] + " not in dict"

def appendRow(dict, row):
    name = row[0]
    dictRow = dict[name]

    for item in row:
        for word in item.split(','):
            r = string.find(word, '(s)')
            if r == -1:
                appendWord(dictRow, word)
            else:
                sing = word.replace('(s)', '')
                appendWord(dictRow, sing)
                plural = word.replace('(', '')
                plural = plural.replace(')', '')
                appendWord(dictRow, plural)

def appendWord(dictRow, word):
    word = word
    if word != '':
        if not word in dictRow:
            dictRow.append(word)

def write(dict):
    outFile = open('countries_new.csv', 'w')
    oufFileWriter = csv.writer(outFile)

    for country in dict:
        row = []
        row.append(country)
        for word in dict[country]:
            if word!='':
                row.append(word)
        oufFileWriter.writerow(row)

dict = loadOldDict()
appendNewData('adjectives_demonyms.csv', dict)
write(dict)

word = 'French(s)'
