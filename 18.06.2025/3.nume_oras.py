# create Class Person
# Class has name and city. Creeate a method that says:
# "[name] leaves in [city]".

class Person:
    def __init__(self, name, city):
        self.name=name
        self.city=city


person1=Person("Oppenhemier", "Los Alamos")

print(f"{person1.name} used to live in {person1.city} ")