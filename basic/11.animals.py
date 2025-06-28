# You have a list of animals.
# Ask the user to enter the name of an animal (e.g., "tiger").
# Using a for loop, check if that animal exists in the list:
# If it does → Animal found: tiger
# If it doesn't → Animal not found.

predators=["Lion", "Tiger","Wolf", "Panter", "Mountain Lion", "Cheetah", "Lepard"]

add_animal=input("Add an predator\n")
for animal in predators:
    if animal.lower()==add_animal.lower():
        print("Animal found")
        break
else:
    print("Animal not found")
    predators.append(add_animal)
    print(f"the predator {add_animal} was added")

print(f"the new list of predators is {predators}")

