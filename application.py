from flask import Flask, jsonify, redirect, render_template, request, url_for


app = Flask(__name__)

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
    return render_template("services/ballreminders.html")

@app.route("/barking")
def barking():
    return render_template("services/barking.html")

@app.route("/biting")
def biting():
    return render_template("services/biting.html")

@app.route("/chilling")
def chilling():
    return render_template("services/chilling.html")

@app.route("/digging")
def digging():
    return render_template("services/digging.html")

@app.route("/pulling")
def pulling():
    return render_template("services/pulling.html")







if __name__ == "__main__":
    app.run()