a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"Because {b} * {a // b} = {b * (a // b)} and the remainder is {a % b}")