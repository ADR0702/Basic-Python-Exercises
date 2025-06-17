class Animal:
    def __init__(self, sunet):
        self.sunet=sunet
        sunet="Ham!"

obiect=Animal("caine")

print(obiect)


class Carte:
    def __init__(self, titlu, autor, an_publicare ):
        self.titlu=titlu
        self.autor=autor
        self.an_publicare=an_publicare

cartea1=Carte("Micul Print", "Antoine de Saint-Exupéry", "1943")

print(f"Carte:{cartea1.titlu} Autor: {cartea1.autor} An Publicare:{cartea1.an_publicare}")