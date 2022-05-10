import config
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy







application=Flask(__name__)
application.config.from_object(config.Config)
api=Api(application)
db=SQLAlchemy(application)



from src import routes