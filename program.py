


class Car:
    def __init__(self, maker, model, serial):
        self.maker = maker
        self.model = model
        self.serial = serial

class CarFactory:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def makeCar(self, model):
        self.cars.append(Car(self.name, model, len(self.cars)))

    def listCars(self):
        for car in self.cars:
            print(car.maker + " " + car.model + " serial#: " + str(car.serial))

    def findCar(self, serial):
        for car in self.cars:
            if(car.serial == serial):
                return car

toyota = CarFactory('Toyota')
toyota.makeCar('Prius')
toyota.makeCar('Rav 4')
toyota.listCars()
print(toyota.findCar(1).model)