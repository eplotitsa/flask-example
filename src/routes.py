from flask_restful import Resource
#from requests import request
from src import api,db
from flask import render_template,request
from csv import writer
from src.resource.Cars import CarListApi
from src.resource.Smoke import Smoke



from src.models import Cars

class Root(Resource):
    def get(self):
        return '<h1>Test</h1>'
        #return render_template('index.html')






api.add_resource(Smoke, '/smoke',strict_slashes=False)
api.add_resource(CarListApi,'/cars','/cars/<plate>',strict_slashes=False)
#api.add_resource(Root, '/')
