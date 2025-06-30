def checkage(age):
    if age < 18:
        return "You're a minor!"
    else:
        return "You're a major!"
    
age=int(input("Enter your age\n"))

print(checkage(age))