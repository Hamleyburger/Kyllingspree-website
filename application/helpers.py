from flask import session
import texts
import config

def getSessionText():
    print("helpers.py getSessionText")
    print(session)
    if 'lan_code' in session:
        lan_code = session['lan_code']
        print("helpers.py setting lan_code to {}".format(session['lan_code']))
    else:
        lan_code = 'en'
        print("helpers.py setting lan_code to en")
    myDict = texts.getText(lan_code)
    print("helpers.py getting text from texts with lan_code: {}".format(lan_code))
    return myDict