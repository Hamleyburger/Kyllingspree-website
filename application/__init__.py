from flask import Flask

app = Flask(__name__)

from application import views
from application import service_views
import texts


lan_code = "en"


@app.context_processor
def context_processor():
    text = texts.translatedText()
    return dict(text=text)