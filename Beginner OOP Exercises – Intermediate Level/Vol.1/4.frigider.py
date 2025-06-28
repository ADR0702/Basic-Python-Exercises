# Create a class Drink:

# Has an attribute name (e.g., "Cola").

# Has a method serve() that prints: Serving [name].

# Create a class Fridge:

# Has an attribute color (e.g., "LG").

# Contains a Drink object (composition).

# Has a method open_fridge() that:

# Prints: "Fridge [color] is opening..."

# Then calls the serve() method of the drink.

class Drink:
    def __init__(self, name,):
        self.name=name

    def serving(self):
        print(f"She takes {self.name} out and serves it with ice and a bit of lemon")

class Fridge:
    def __init__(self, color, drink):
        self.color=color
        self.drink=drink
    def open(self):
        print(f"Anna opens the {self.color} fridge...")
        self.drink.serving()

drink1=Fridge("red", Drink("Coca Cola"))
drink1.open()
    