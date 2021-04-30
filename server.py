from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from controllers.cars import Car, CarList
from services.cars import CarService


def main():
    #Create the Flask app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.sqlite'

    #Create the Flask-RESTful API
    api = Api(app)

    # Connect to the database with Flask-SQLalchemy
    db = SQLAlchemy(app)

    # Create the cars service. The database is dependency injected to the constructor
    # Controllers can then use db.session to get access to a scoped session.
    cars = CarService(db)

    # Register the route for each resource
    api.add_resource(CarList, '/cars/',
                     resource_class_args=[cars])

    api.add_resource(Car, '/cars/<id>',
                     resource_class_args=[cars])

    app.run(debug=True)

if __name__ == '__main__':
    main()
