#!/usr/bin/env python

from application import app
from flask import Flask, jsonify, redirect, render_template, request, url_for

import smtplib
import config as cfg


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
        sendMail(message, subject)

        return render_template("submitted.html", email=email, subject=subject, message=message)

    return render_template("contact.html")



def sendMail(usermessage, usersubject):

    sender_email = cfg.mySecrets['sender_email']
    rec_email = cfg.mySecrets['rec_email']
    password = cfg.mySecrets['password']


    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender_email, password)
     

        msg = f'Subject: {usersubject}\n\n{usermessage}'

        smtp.sendmail(sender_email, rec_email, msg)


