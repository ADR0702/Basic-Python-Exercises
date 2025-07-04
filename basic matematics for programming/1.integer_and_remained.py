# Exercise 1: Integer Division and Remainder
# Write a Python program that:
# Asks the user to input two numbers: a and b;
# Displays:
# the result of the integer division a // b;
# the remainder of the division a % b.
while True: 
    a=int(input("Please add a number\n"))
    b=int(input("Please add a number\n"))
    if a > 0 and  b > 0:
        integer_division=a // b
        remainder_division=a % b

        print(f"the result of a // b is {integer_division} ")
        print(f"the result of a % b is {remainder_division}")
        break

    else:
        print("both numbers should be bigger than 0!! Try again!")
    



