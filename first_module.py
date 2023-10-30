#!usr/bin/env python3

def hello():
    print("First module ")


class car:

    def __init__(self, name, max_speed, distance, fuel_meter):
        self.name = name
        self.max_speed = max_speed
        self.distance = distance
        self.fuel_meter = fuel_meter

"wee need to ad:d this line to run the module as a script"

# Here we are goin to define a new class 
class car:

    def __init__(self, name, max_speed, distance, fuel_meter):
        self.name = name
        self.max_speed = max_speed
        self.distance = distance
        self.fuel_meter = fuel_meter

    def drive(self):
        print("driving")

    def stop(self):
        print("stopped")

    def park(self):
        print("parking")

    def refuel(self):
        print("refueling")

    def status(self):
        print("name: ", self.name)
        print("max_speed: ", self.max_speed)
        print("distance: ", self.distance)
        print("fuel_meter: ", self.fuel_meter)
