# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
class Vehicle():
    def __init__(self,name,wheels,doors):
        self.name = name
        self.wheels = wheels;
        self.doors = doors;
        
    def __str__(self):
         return (f"Wheels:{self.wheels}, Doors : {self.doors}")


class GroundVehicle(Vehicle):
    def __init__(self,type,name,wheels,doors):
        self.type = type
        super().__init__(name,wheels,doors)
        
class Car(GroundVehicle):
    def __init__(self,style,type,name,wheels,doors):
        self.style = style
        super().__init__(type,name,wheels,doors)

class Motorcycle(GroundVehicle):
    def __init__(self,speed,style,type,name,wheels,doors):
        self.speed = speed
        super().__init__(style,type,name,wheels,doors)
        
class FlightVehicle():
    def __init__(self,name,wings,propeller):
        self.name = name
        self.wings = wings
        self.propeller = propeller
class AirPlane():
    def __init__(self,type,name,wings,propeller):
        self.type = type
        super().__init__(name,wings,propeller) 
class Starship():
    def __init__(self,name,type,hyperspeed=True):
        self.name= name
        self.type= type
        self.hyperspeed= hyperspeed
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
droptop = Vehicle("bugatti",4,2)

print(droptop)