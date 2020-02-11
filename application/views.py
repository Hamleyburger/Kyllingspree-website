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
    title = "Daily ball reminders"
    text = "Oops! I seem to have dropped something on your laptop. We'd better remove it, right? (and throw it as far away as possible)<br>Humans, like the rest of us, occasionally need help sorting out their priorities. I can help with that. More time for the important things in life, you dig?"
    return render_template("servicelayout.html", image=image, title=title, text=text)

@app.route("/barking")
def barking():
    image = "kylbark.jpg"
    title = "Barking"
    text = "Enemies can oftentimes be warded off from a distance with no need to bite them. This, however, requires wit, persistence and volume – in all of which I excel. I can bark directly from my leash, from your garden fence (this works particularly well with neighbours and large vehicles) or from the comfort of your home. I can hear them coming from miles away. And they can hear me."
    return render_template("servicelayout.html", image=image, title=title, text=text)

@app.route("/biting")
def biting():
    image = "Kylbite.JPG"
    title = "Biting"
    text = "Cyclists – postmen – waitresses on cafés – other male dogs - often pose a significant threat to your well-being. How do you know if that’s the case? You usually don’t! But don’t worry - I can tell. No more barging into your personal space. No more hello-saying. I start by barking and growling. In this way I also prevent them from trying to negotiate.  If they keep approaching I bite. You will not be bothered by uninvited (or invited) guests ever again."
    return render_template("servicelayout.html", image=image, title=title, text=text)

@app.route("/chilling")
def chilling():
    image = "kylchill3.jpg"
    title = "Chilling out"
    text = "The reason we’re all here. Innit!"
    return render_template("servicelayout.html", image=image, title=title, text=text)

@app.route("/digging")
def digging():
    image = "kyldiglarge.jpg"
    title = "Digging"
    text = "Critters often live in holes. I help you dig them out. As a bonus service I decorate your furniture with fresh dirt straight from the wilderness."
    return render_template("servicelayout.html", image=image, title=title, text=text)

@app.route("/pulling")
def pulling():
    image = "kylpulllarge.jpg"
    title = "Pulling"
    text = "Who doesn’t want a helping hand (or four helping legs) for pushing forward more quickly? Combine with skateboard at your own risk."
    return render_template("servicelayout.html", image=image, title=title, text=text)