
# Create a class Toy:
# Attribute: type (e.g., "plush mouse")
# Method use() → prints: "The cat plays with [type]."
# Create a class Cat:
# Attribute: name
# Attribute: toy → a Toy object
# Method play() that:
# Prints: "[name] jumps on the couch!"
# Calls use() on the toy


class Toy:
    def __init__(self, type):
        self.type=type
    def use(self):
        print(f"The cat plays with {self.type}.")
class Cat:
    def __init__(self, name, toy):
        self.name=name
        self.toy=toy
    def play(self):
        print(f"{self.name} jumps on the couch!")
        self.toy.use()

toy1=Toy("plush mouse")
cat1=Cat("Ingrid", toy1)

cat1.play()

