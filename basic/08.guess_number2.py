# "Choose a secret number in the code (e.g., secret_number = 11).

# Let the user try to guess it a maximum of 3 times.

# If they guess it, display:
# "Well done, you guessed the number!" and exit the loop.

# If they don’t manage to guess it after 3 attempts, display:
# "Access denied. You’ve exceeded the number of attempts."**

secret_number=11
tries=0
maximum_try=3

while tries < maximum_try:
    user_try=int(input("introduceti un numar de la 1-20\n"))
    if user_try==secret_number:
        print("Well done, you guessed the number!")
        break
    else:
        tries+=1
        print(f"Wrong number! Attempt no {tries} ! Try again")
if tries==maximum_try:
    print("Access denied. You've exceeded the number of attempts.")

        

   
