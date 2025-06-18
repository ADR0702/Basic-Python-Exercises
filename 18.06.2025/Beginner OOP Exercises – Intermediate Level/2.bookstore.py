# Exercise: BookStore Class
# Create a class called BookStore with the following:

# Attributes:

# store_name (the name of the bookstore)

# books (number of books in stock)

# Methods:

# display_stock() – displays how many books are currently in stock

# add_books(number) – adds a number of books to the stock

# sell_books(number) – subtracts a number of books from the stock if there are enough; otherwise, print a warning

# Create an object of the class, simulate some sales and additions, and print the stock after each step.


class BookStore:
    def __init__(self,name, stock_number):
        self.name=name
        self.stock_number=stock_number
    
    def display_stock(self):
        print(f"The store named {self.name} has {self.stock_number} books in stock")

    def add_books(self, number):
        self.stock_number += number
    
    def sell_books(self, number):
        if number > self.stock_number:
            print("Not enough books in the store")
        else:
            self.stock_number -= number


stock=BookStore("Humanitas", int(input("Please add current shop stock\n")))
stock.display_stock()
stock.add_books(300)
stock.display_stock()
stock.sell_books(450)
stock.display_stock()


        