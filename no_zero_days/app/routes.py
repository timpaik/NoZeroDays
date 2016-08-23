from no_zero_days import application


@application.route('/')
def index():
    return 'Hello World!'
