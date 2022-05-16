import config
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os



template_dir = template_dir = os.path.abspath('src/pages/templates')


application=Flask(__name__ ,template_folder=template_dir)
application.config.from_object(config.Config)
api=Api(application)
db=SQLAlchemy(application)



from src import routes