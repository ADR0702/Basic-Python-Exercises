# Create a class Bottle:
# Has an attribute brand (e.g., "Dorna").
# Has a method drink() that prints:
# "Drinking water from [brand]."
# Create a class Person:
# Has an attribute name.
# Has an attribute bottle → a Bottle object.
# Has a method hydrate() that:
# Prints: "[name] starts drinking water..."
# Then calls the drink() method from the bottle.

class Bottle:
    def __init__(self, brand):
        self.brand=brand
    def drink(self):
        print (f"He is drinking water from {self.brand}.")
class Person:
    def __init__(self, name, bottle):
        self.name=name
        self.bottle=bottle
    def hydrate(self):
        print(f"{self.name} starts drinking water")
        self.bottle.drink()

bottl1=Bottle("Borsec")
pers=Person("Andrei", bottl1)
pers.hydrate()
      
        
        
