class Movie:
    def __init__(self, name , launch_date):
        self.name=name
        self.launch_date=launch_date
    def description(self):
        print(f"The movie {self.name} was launched on {self.launch_date}")

movie1=Movie("First Man", "2018")
movie1.description()