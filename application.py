from flask import Flask

application=Flask(__name__)

@application.route('/')
def hello_world():
    return 'This is just a test'

@application.route('/smoke')
def hello_world():
    return 'This is smoke'
#application.run()