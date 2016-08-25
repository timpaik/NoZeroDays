from flask import render_template
from no_zero_days import application


@application.route('/')
def index():
    return render_template('index.html')
