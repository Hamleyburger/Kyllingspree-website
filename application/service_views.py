#!/usr/bin/env python
from application import app
from flask import Flask, render_template, session
from .helpers import getSessionText

# Routes for all services in /services
@app.route("/ballreminders")
def ballreminders():
    image = "ballremind2.jpg"
    myDict = getSessionText()
    title = myDict['services.title.ballreminders']
    serviceText = myDict['services.description.ballreminders']
    return render_template("servicelayout.html", image=image, title=title, serviceText=serviceText)

@app.route("/barking")
def barking():
    image = "kylbark.jpg"
    myDict = getSessionText()
    title = myDict['services.title.barking']
    serviceText = myDict['services.description.barking']
    return render_template("servicelayout.html", image=image, title=title, serviceText=serviceText)

@app.route("/biting")
def biting():
    image = "Kylbite.JPG"
    myDict = getSessionText()
    title = myDict['services.title.biting']
    serviceText = myDict['services.description.biting']
    return render_template("servicelayout.html", image=image, title=title, serviceText=serviceText)

@app.route("/chilling")
def chilling():
    image = "kylchill3.jpg"
    myDict = getSessionText()
    title = myDict['services.title.chilling']
    serviceText = myDict['services.description.chilling']
    return render_template("servicelayout.html", image=image, title=title, serviceText=serviceText)

@app.route("/digging")
def digging():
    image = "kyldiglarge.jpg"
    myDict = getSessionText()
    title = myDict['services.title.digging']
    serviceText = myDict['services.description.digging']
    return render_template("servicelayout.html", image=image, title=title, serviceText=serviceText)

@app.route("/pulling")
def pulling():
    image = "kylpulllarge.jpg"
    myDict = getSessionText()
    title = myDict['services.title.pulling']
    serviceText = myDict['services.description.pulling']
    return render_template("servicelayout.html", image=image, title=title, serviceText=serviceText)