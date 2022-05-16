
from importlib.resources import path
from src import application,db
from flask import render_template
from src.models import Cars
import os



template_dir = os.path.join(os.path.dirname(__file__),'templates')

@application.route('/')
def hello_world():
    return render_template('Form_field.html')
    #return 'This is just a test 2344'

@application.route('/allcars')
def all_cars():
    cars=db.session.query(Cars)
    return render_template('All_cars.html', cars=cars)
    #return 'This is just a test 2344'