from flask import Flask

application = Flask(__name__, static_folder="./static/dist", template_folder="./static")

from no_zero_days.app import routes