#!/usr/bin/env python

import csv
from application import views


myText = {}
validLan = ['en', 'da']
lan_code = "en"

def setLan(lanc):
    global lan_code
    lan_code = lanc


def getText(lan_code):
    if (lan_code in validLan):
        with open('dict.{}.csv'.format(lan_code), newline='') as csvfile:
            textreader = csv.reader(csvfile, delimiter='$')
            for row in textreader:
                    myText[row[0]] = row[1]

            print("Language: {} - exist!".format(lan_code))
            return(myText)
    else:
        print("Language: {} - does not exits. You get English (en)!".format(lan_code))
        return(getText("en"))

def translatedText():
    return getText(lan_code)






"""
mydict = {'nav.service': 'tjenester', 'nav.contact': 'kontakt', 'nav.pricing': 'priser'}
# For python 2, skip the "newline" argument: open('dict.csv','w")
with open('dict.csv', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file, delimiter = '$')
    for key, value in mydict.items():
       writer.writerow([key, value])
"""