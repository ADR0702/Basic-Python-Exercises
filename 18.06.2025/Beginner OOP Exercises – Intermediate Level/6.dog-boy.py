# Create a class Dog:

# Has an attribute name (e.g., "Rex").

# Has a method bark() that prints: "The dog [name] is barking!"

# Create a class Boy:

# Has an attribute name.

# Has an attribute dogs → a list of Dog objects.

# Has a method walk_dogs() that:

# Prints: "The boy [name] is walking his dogs..."

# Loops through the list and calls bark() on each dog.

class Dog:
    def __init__(self, name):
        self.name=name
    def bark(self):
        print(f"{self.name} barks all the time!!")

class Boy:
    def __init__(self, name, dogs):
        self.name=name
        self.dogs=dog
    def walk_dogs(self):
        print(f"the boy {self.name} is walking his dogs...")
        for dog in self.dogs:
            dog.bark()

dog=[Dog("Spot"), Dog("Max")]
boy=Boy("Steven", dog)
boy.walk_dogs()

        