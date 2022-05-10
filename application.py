from src import application, api,models, db

#application=Flask(__name__)

@application.route('/')
def hello_world():
    return 'This is just a test'

@application.route('/testfun')
def testfun():
    return 'This is testfun'

if __name__ == "__main__":
    application.run()