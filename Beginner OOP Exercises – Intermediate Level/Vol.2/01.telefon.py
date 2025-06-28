# Create a class Phone:
# Attribute: model (e.g., "iPhone")
# Method call() → prints: "Calling from [model]..."
# Create a class Person:
# Attribute: name
# Attribute: phone → a Phone object
# Method make_call() that:
# Prints: "[name] is dialing a number..."
# Calls the phone's call() method


class Phone:
    def __init__(self, brand):
        self.brand=brand
    def call(self):
        print(f"Calling from {self.brand}")

class Person:
    def __init__(self, name, phone):
        self.name=name
        self.phone=phone
    def make_call(self):
        print(f"{self.name} is dialing a number")
        self.phone.call()   

person = Person("Alex", Phone("Samsung Galaxy"))
person.make_call()
