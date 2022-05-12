from flask_restful import Resource
#from requests import request
from src import api,db
from flask import render_template,request
from csv import writer

import csv

from src.models import Cars

class Root(Resource):
    def get(self):
        return '<h1>Test</h1>'
        #return render_template('index.html')

def Csv_data_read():
    # Функция вычитывает все машины из файла и возвращает их в переменной data в виде list
    # аналог get_all_films
    data=[]
    with open('auto.csv',mode="r", encoding="utf-8") as File:  
        reader = csv.DictReader(File)
        for row in reader:
            data.append(row)
    return data

def Csv_data_add(car:list):
    with open('auto.csv',mode="a", encoding="utf-8") as File:
        writer_object = writer(File)
        writer_object.writerow(car)
        File.close()


def get_car_by_number(CarNum) ->dict:
    cars=Csv_data_read()
    car=list(filter(lambda f:f['Plate']==CarNum,cars))
    return car[0] if car else {}

class CarListApi(Resource):
    def get(self,CarNum=None):
        if not CarNum:
            cars = db.session.query(Cars).all()
            return [f.to_dict() for f in cars], 200
        cars=db.session.query(Cars).filter_by(plate=CarNum).first()
        if not cars:
            return '', 404
        return cars.to_dict(), 200


    def post(self):
        car_json=request.json
        if not car_json:
            return {'message':'Wrong data'}, 400
        try:
            auto = Cars(
                auto=car_json['auto'],
                plate=car_json['plate'],
                color=car_json['color']
            )
            db.session.add(auto)
            db.session.commit()
        except(ValueError, KeyError):
            return {'message':'Wrong data 1'}, 400
        return {'message':'Record created'}, 201

    def put(self, plate):
        car_json=request.json
        if not car_json:
            return {'message':'Wrong data'}, 400
        try:
            db.session.query(Cars).filter_by(plate=plate).update(
                dict(
                    auto=car_json['auto'],
                    plate=car_json['plate'],
                    color=car_json['color']
                )
            )
            db.session.commit()
        except(ValueError, KeyError):
            return {'message':'Wrong data 1'}, 400
        return {'message':'Record updated'}, 200



    def patch(self):
        pass
    def delete(self):
        pass


class Smoke(Resource):
    def get(self):
        return {'message':'OK'},200

api.add_resource(Smoke, '/smoke',strict_slashes=False)
api.add_resource(CarListApi,'/cars','/cars/<CarNum>',strict_slashes=False)
api.add_resource(Root, '/')
