

def functie_goala(text):
    if text == "":
        return True
    else:
        return False

text=input("introduceti un text")
if functie_goala(text):
    print("Textul e gol")
else:
    print("textul nu este gol")