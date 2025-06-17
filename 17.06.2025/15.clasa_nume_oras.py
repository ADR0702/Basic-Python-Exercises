

class Masina:
    def __init__(self, nume, oras):
        self.nume=nume
        self.oras=oras

masina1=Masina("Mercedes", "Stuttgard")

print(f"masina se numeste {masina1.nume} si este din {masina1.oras}")


class Telefon:
    def __init__(self, name, model, color):
        self.name=name
        self.model=model
        self.color=color

telefon1=Telefon("Iphone", "15 PRO MAX", "White Titanium")

print(f"Telefonul pe care ti-l vand este un {telefon1.name} {telefon1.model} de culoarea {telefon1.color}")