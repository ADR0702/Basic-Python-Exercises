# "Choose a secret number in the code (e.g., secret_number = 22).

# Let the user try to guess it a maximum of 3 times.

# If they guess it, display:
# "Well done, you guessed the number!" and exit the loop.

# If they don’t manage to guess it after 3 attempts, display:
# "Access denied. You’ve exceeded the number of attempts."**
# The attempts should be counted from 3 to 0

secret_number=22
tries=3
maximum_try=3

while tries>0:
    user_try=int(input("introduceti un numar de la 1-25\n"))

    if user_try==secret_number:
        print("Well done, you guessed the number!")
        break
    tries-=1
    if tries > 0:
        print(f"Wrong number! You have {tries} more attempts ! Try again")

if tries==0:
    print("Access denied. You've exceeded the number of attempts.")