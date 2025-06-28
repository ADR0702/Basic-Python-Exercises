# Create a class Bottle:
# Attribute: brand (e.g., "Dorna")
# Method: drink() → prints "Drinking water from [brand]."
# Create a class Person:
# Attribute: name
# Attribute: bottles → a list of Bottle objects
# Method: hydrate() that:
# Prints: "[name] starts drinking from all the bottles..."
# Loops through the list and calls drink() on each bottle

class Bottle:
    def __init__(self, brand):
        self.brand=brand
    def drink(self):
        print (f"He is drinking water from {self.brand}.")
class Person:
    def __init__(self, name, bottle):
        self.name=name
        self.bottle=bottle
        bottle=[]
    def hydrate(self):
        for i in self.bottle:
            if i in self.bottle:
                print(f"{self.name} starts drinking from all the bottles...")
            else:
                pass

bottle1=Bottle("Borsec")
pers=Person("Andrei", bottle1)
pers.hydrate()