from application import app
from flask import Flask, jsonify, redirect, render_template, request, url_for


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Routes for all services in /services
@app.route("/ballreminders")
def ballreminders():
    image = "ballremind2.jpg"
    return render_template("services/ballreminders.html", image=image)

@app.route("/barking")
def barking():
    image = "kylbark.jpg"
    return render_template("services/barking.html", image=image)

@app.route("/biting")
def biting():
    image = "Kylbite.JPG"
    return render_template("services/biting.html", image=image)

@app.route("/chilling")
def chilling():
    image = "kylchill3.jpg"
    return render_template("services/chilling.html", image=image)

@app.route("/digging")
def digging():
    image = "kyldiglarge.jpg"
    return render_template("services/digging.html", image=image)

@app.route("/pulling")
def pulling():
    image = "kylpulllarge.jpg"
    return render_template("services/pulling.html", image=image)