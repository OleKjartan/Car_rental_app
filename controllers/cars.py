from flask import jsonify, make_response, request
from flask_restful import Resource
from werkzeug.exceptions import *

# Class responsible for /cars/
class CarList(Resource):
    def __init__(self, cars):
        self.cars = cars

    def get(self):
        return jsonify(self.cars.get_all())

    def post(self):
        car = self.cars.add(request.json)
        return make_response(jsonify(car), 201)

# Class responsible for /cars/<id>
class Car(Resource):
    def __init__(self, cars):
        self.cars = cars

    def put(self, id):
        car = self.cars.get(id)

        if not car:
            raise NotFound('Invalid ID...')

        json = request.get_json()

        car.car = json['car']
        car.model = json['model']
        car.year = json['year']

        self.cars.update(car)
        return jsonify(car)

    def delete(self, id):
        car = self.cars.get(id)

        if not car:
            raise NotFound('Invalid ID...')

        self.cars.delete(car)
        return jsonify(car)