# Exercise: "A Girl has a Game"
# Create two classes:

# Game

# Has an attribute name (the name of the game).

# Has a method play() that prints:
# "Playing [game name]!"

# Girl

# Has a name (e.g., "Emma")

# Has a Game object as an attribute (composition).

# Has a method start_game() that:

# Prints: "Emma is starting the game..."

# Then calls the play() method of the Game.


class Game: #creez clasa game
    def __init__(self, name): # o definesc
        self.name=name
    def play(self):  #ii creez si un "verb" face ceva
        print(f"playing {self.name}!") # ii cream un string care sa spuna exact ce face functia play

class Girl: #creez substantivul, omul care ia actiunea de mai sus
    def __init__(self, name, game): #definesc numele si jocul
        self.name=name
        self.game=game #nu am inteles de ce mai definesc aici jocul daca am o clasa mai sus cu numele jocului.e doar pentru play?

    def start_game(self): #initializez jocul dinou se pare
        print(f"{self.name} is starting the game!") # ii dau un string 
        self.game.play()

girl=Girl("Ema", Game("Counter-Strike"))
girl.start_game()
   