from flask import Flask

application = Flask(__name__)

from no_zero_days.app import routes