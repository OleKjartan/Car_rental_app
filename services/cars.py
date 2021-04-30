from models.car_customer import Car

class CarService:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.session.query(Car).all()

    def add_car(self, json):
        car = Car(id=json['id'],car=json['car'], model=json['model'], year=json['year'])
        self.db.session.add(car)
        self.db.session.commit()

    def update(self, car):
        self.db.session.delete(car)
        self.db.session.commit()

    def delete(self, car):
        self.db.session.delete(car)
        self.db.session.commit()