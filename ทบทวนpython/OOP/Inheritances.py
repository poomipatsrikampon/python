
class Vehicle:
    def turnOnAirConditioner(self):
        print("Turn on : Air")

class Car(Vehicle):
    def openTheDoor(self):
        print("Open the Door")

car1 = Car()
car1.turnOnAirConditioner()
