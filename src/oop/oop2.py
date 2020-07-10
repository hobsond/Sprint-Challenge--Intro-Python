# To the GroundVehicle class, add method drive() that returns "vroooom".
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self,name,type, num_wheels=4):
        self.num_wheels = num_wheels
        self.type = type
        self.name = name
    def drive(self): 
        print('vroom')
    # TODO


# Subclass Motorcycle from GroundVehicle.
class Motorcycle(GroundVehicle):
    def __init__(self,name,type,num_wheels=2,):
        super().__init__(type,num_wheels)  
        
    def drive(self):
        print('brapp')
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

vehicles = [
    
    GroundVehicle('name','type'),
    Motorcycle("name","type"),
    GroundVehicle("name","type"),
    Motorcycle("name","type`    "),
]

for i in vehicles:
   i.drive()

# Go through the vehicles list and print the result of calling drive() on each.

# TODO
