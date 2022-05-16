from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from src import db
from src.models import Cars
from src.schemas import CarSchema

class CarListApi(Resource):
    car_schema = CarSchema()

    def get(self,CarNum=None):
        if not CarNum:
            cars = db.session.query(Cars).all()
            return self.car_schema.dump(cars,many=True), 200
            #return [f.to_dict() for f in cars], 200
        cars=db.session.query(Cars).filter_by(plate=CarNum).first()
        if not cars:
            return '', 404
        return self.car_schema.dump(cars), 200
        #return cars.to_dict(), 200


    def post(self):
        try:
            car = self.car_schema.load(request.json,session=db.session)
        except ValidationError as e:
            return {'message':str(e)}, 400
        db.session.add(car)
        db.session.commit()
        return self.car_schema.dump(car), 200


    #def post(self):
    #    car_json=request.json
    #    if not car_json:
    #        return {'message':'Wrong data'}, 400
    #    try:
    #        auto = Cars(
    #            auto=car_json['auto'],
    #            plate=car_json['plate'],
    #            color=car_json['color']
    #        )
    #        db.session.add(auto)
    #        db.session.commit()
    #    except(ValueError, KeyError):
    #        return {'message':'Wrong data 1'}, 400
    #    return {'message':'Record created'}, 201

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



    def patch(self,plate):
        cars=db.session.query(Cars).filter_by(plate=plate).first()
        if not cars:
            return '',404
        car_json = request.json
        auto=car_json.get('auto')
        color=car_json.get('color')
        if auto:
            cars.auto = auto
        elif color:
            cars.color = color
        
        db.session.add(cars)
        db.session.commit()
        return {'message':'Record updated'}, 200




    def delete(self):
        pass


