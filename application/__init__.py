from flask import Flask, session

app = Flask(__name__)

from application import views
from application import service_views
from .helpers import getSessionText
import config


@app.context_processor
def context_processor():
    text = getSessionText()
    return dict(text=text)