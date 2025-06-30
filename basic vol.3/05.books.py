class Book:
    def __init__(self, title, autor):
        self.title=title
        self.autor=autor

    def titlename(self):
        print(f"The title name is {self.title}")
    
    def autor_name(self):
            print(f"the name of the writter is {self.autor}")


book1=Book("The Godfather", "Mario Puzzo")
book1.titlename()
book1.autor_name()

        