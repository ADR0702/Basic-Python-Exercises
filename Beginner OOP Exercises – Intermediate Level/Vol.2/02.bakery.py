# Create a class Dessert:
# Has an attribute name (e.g., "Tiramisu").
# Has a method serve() that prints: "Serving the dessert [name]."
# Create a class PastryChef:
# Has an attribute name.
# Has an attribute dessert → a Dessert object.
# Has a method serve_customer() that:
# Prints: "[name] is bringing the dessert to the table..."
# Then calls the dessert’s serve() method.

class Dessert:
    def __init__(self, name):
        self.name=name
    def serve(self):
        print(f"Serving the dessert {self.name}")
class PastryChef:
    def __init__(self, name, cake):
        self.name=name
        self.cake=cake
    def serve_customer(self):
        print(f"{self.name} is bringing the dessert to the table")
        self.cake.serve()
cake=Dessert ("Carrot Cake")
chef=PastryChef ("Enric Lanlard", cake )
chef.serve_customer()
        