from src import app, api,models, db

#application=Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is just a test'

@app.route('/smoke')
def smoke():
    return 'This is smoke'
#application.run()