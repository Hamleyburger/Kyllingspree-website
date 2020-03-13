#!/usr/bin/env python

import csv
from application import views


myText = {}

# Keep this list updated if you add more translations:
validLan = ['en', 'da']
lan_code = "en"

def getText(lan_code):
    if (lan_code in validLan):
        with open('application/static/csvs/dict.{}.csv'.format(lan_code), newline='') as csvfile:
            textreader = csv.reader(csvfile, delimiter='$')
            for row in textreader:
                    myText[row[0]] = row[1]

            print("Language: {} - exist!".format(lan_code))
            return(myText)
    else:
        print("Language: {} - does not exits. You get English (en)!".format(lan_code))
        return(getText("en"))


