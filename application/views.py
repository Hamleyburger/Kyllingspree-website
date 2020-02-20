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

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        req = request.form

        email = req.get("email")
        subject = req.get("subject")
        message = req.get("message")

        print(req)

        return render_template("submitted.html", email=email, subject=subject, message=message)

    return render_template("contact.html")

