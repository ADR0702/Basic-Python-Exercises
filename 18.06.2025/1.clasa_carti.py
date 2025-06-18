# Clasa Carte
# Creează o clasă Carte cu atributele titlu și autor. Afișează:
# "Cartea [titlu] a fost scrisă de [autor]".
class Carte:
    def __init__(self, titlu, autor):
        self.titlu=titlu
        self.autor=autor

cartea1=Carte("Amintiri din copilarie", "Ion Creanga")
cartea2=Carte("Calatorie spre centrul pamantului", "Jules Verne")

print(f"Cartea {cartea1.titlu} a fost scrisa de {cartea1.autor}")
print(f"Cartea {cartea2.titlu} a fost scrisa de {cartea2.autor}")        