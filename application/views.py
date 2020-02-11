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

