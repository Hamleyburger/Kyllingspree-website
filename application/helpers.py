from flask import session
import texts

def getSessionText():
  if 'lan_code' in session:
      lan_code = session['lan_code']
  else:
      lan_code = 'en'
  myDict = texts.getText(lan_code)
  return myDict