# Create a class Book with:

# attribute title

# method read() → prints: Reading the book [title]

# Create a class Girl with:

# attribute name

# attribute books → a list of Book objects

# method read_all_books() → loops through the list and calls read() on each book

class Book:
    def __init__(self, title):
        self.title=title
    def read(self):
        print(f"I'm reading the book named {self.title}")
class Girl:
    def __init__(self, name, books):
        self.name=name
        self.books=books
        
    def read_all_books(self):
        print(f"{self.name} is reading all the books:")
        for book in self.books:
            book.read()


books = [Book("Alice in Wonderland"), Book("Harry Potter")]
girl = Girl("Emma", books)
girl.read_all_books()

