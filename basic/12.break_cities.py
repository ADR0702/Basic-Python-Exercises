# cities = ["Paris", "London", "Tokyo", "New York", "Berlin"]

# Ask the user to enter a city.
# If the city exists in the list, print “City found!” and stop searching.
# If not, continue searching. If the city is not found at all, print “City not found.”

cities = ["Paris", "London", "Tokyo", "New York", "Berlin"]

traveller=input("Enter a city\n")

for city in cities:
    if traveller==city:
        print("City found in the list!")
        break
    else:
        print("City not found!")
        