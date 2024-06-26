#!/usr/bin/env python3
'''A basic flask app'''
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFUALT_LOCALE = "en"
    BABEL_DEFUALT_TIMEZONE = "UTC"

app.config.from_object(Config)

@app.route('/')
def home():
    '''returns our home template'''
    return render_template('0-index.html')

if __name__== '__main__':
    app.run(debug=True)
