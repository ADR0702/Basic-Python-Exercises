# "Ask the user to guess a secret number (choose any fixed number in the code, for example 7).
# If the entered number is incorrect, the program says:
# "Wrong number, try again."
# and asks for the number again.
# When the user guesses the correct number, the program says:
# "Congratulations! You guessed the number!"
# and ends."**

user=int(input("Choose any number between 1-20\n"))

while user!= 7:
    print("Wrong number, try again.")
    user=int(input("Choose any number between 1-20\n"))

print("Congratulations! You guessed the number!")