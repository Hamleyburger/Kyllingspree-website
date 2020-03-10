#!/usr/bin/env python

from application import app
from flask import Flask, jsonify, redirect, render_template, request, url_for, session

import texts
import smtplib
import config as cfg

#Load text in the right language:texts.getText("")


@app.route("/")
def index():
    print(app.config)
    lan_code = request.args.get("language")
    if lan_code:
        session['lan_code'] = lan_code
        print("lan_code is set to: {} from views.py '/'".format(session['lan_code']))
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
        sendMail(message, subject, email)

        return render_template("submitted.html", email=email, subject=subject, message=message)

    return render_template("contact.html")



#Sends e-mail with a message stating a message and the user provided e-mail address
def sendMail(usermessage, usersubject, useremail):

    #The e-mail for which the password must match
    sender_email = cfg.mySecrets['sender_email']
    #The recipient e-mail. Can be anything.
    rec_email = cfg.mySecrets['rec_email']
    #Password for sender e-mail. Can be a headache with two factor authorization.
    password = cfg.mySecrets['password']
    #Message containing user provided message and e-mail address
    message = "From: {}\n\n{}".format(useremail, usermessage)


    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender_email, password)
     
        msg = f'Subject: {usersubject}\n\n{message}'

        smtp.sendmail(sender_email, rec_email, msg)


        