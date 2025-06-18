#  2. Clasa Film
# Creează o clasă Film cu titlu și durata. Creează 2 filme și afișează durata fiecăruia.

class Film:
    def __init__(self, nume, durata):
        self.nume=nume
        self.durata=durata
        
filmul1=Film("The Godfather", "175 Minutes")     
filmul2=Film("First Man", "141 Minutes")

print(f"Filmul {filmul1.nume} are o durata de {filmul1.durata}, iar filmul {filmul2.nume} are o durata de {filmul2.durata} ")
