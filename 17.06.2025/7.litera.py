utilizator=input("introduceti un cuvant\n")

for i in utilizator:
    if i == "a":
        print("felicitari! litera cu care incepe cuvantul este", i)
        break
else:
    print("litera este alta decat a", i)