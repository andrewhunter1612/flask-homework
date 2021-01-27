from flask import render_template
from application import app
from application.models.calculator import *


@app.route("/")
def home_page():
    return render_template('index.html', title="Calculator")