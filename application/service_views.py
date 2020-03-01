#!/usr/bin/env python
from application import app
from flask import Flask, render_template
import texts

myDict = texts.translatedText()

# Routes for all services in /services
@app.route("/ballreminders")
def ballreminders():
    image = "ballremind2.jpg"
    title = myDict['services.title.ballreminders']
    serviceText = myDict['services.description.ballreminders']
    return render_template("servicelayout.html", image=image, title=title, serviceText=serviceText)

@app.route("/barking")
def barking():
    image = "kylbark.jpg"
    title = myDict['services.title.barking']
    serviceText = myDict['services.description.barking']
    return render_template("servicelayout.html", image=image, title=title, serviceText=serviceText)

@app.route("/biting")
def biting():
    image = "Kylbite.JPG"
    title = myDict['services.title.biting']
    serviceText = myDict['services.description.biting']
    return render_template("servicelayout.html", image=image, title=title, serviceText=serviceText)

@app.route("/chilling")
def chilling():
    image = "kylchill3.jpg"
    title = myDict['services.title.chilling']
    serviceText = myDict['services.description.chilling']
    return render_template("servicelayout.html", image=image, title=title, serviceText=serviceText)

@app.route("/digging")
def digging():
    image = "kyldiglarge.jpg"
    title = myDict['services.title.digging']
    serviceText = myDict['services.description.digging']
    return render_template("servicelayout.html", image=image, title=title, serviceText=serviceText)

@app.route("/pulling")
def pulling():
    image = "kylpulllarge.jpg"
    title = myDict['services.title.pulling']
    serviceText = myDict['services.description.pulling']
    return render_template("servicelayout.html", image=image, title=title, serviceText=serviceText)