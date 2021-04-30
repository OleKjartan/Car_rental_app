from dataclasses import dataclass
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



Base = declarative_base()

@dataclass()
class Car(Base):
    __tablename__ = 'cars'

    id : int
    car : str
    model : str
    year : int

    id = Column(Integer, primary_key=True)
    car = Column(String)
    model = (String)
    year = (Integer)

    def addcar():
        # Engine describes the database and connection URL
        engine = create_engine('sqlite:///cars.sqlite')

        # Create a session maker (factory pattern)
        Session = sessionmaker(bind=engine)

        session = Session()

        car_info = car.get()
        model_info = model.get()
        year_info = year.get()

        new_car = Car(car=car_info, model=model_info, year=year_info)

        # Create a session using the session maker
        session.add(new_car)

        session.commit()



class Customer(Base):
    __tablename__ = 'customers'

    id: int
    first_name : str
    first_name : str
    year: int

    id = Column(Integer, primary_key=True)
    car = Column(String)
    model = (String)
    year = (Integer)

    #Legg til relationship for at det skal være mulig å legge til en bil til en kunde