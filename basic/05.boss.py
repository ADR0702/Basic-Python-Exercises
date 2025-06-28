# "Ask the user to enter a name using input().
# If the entered name is 'Adrian', print: Hello, boss!
# If it's any other name, print: Hello, [entered name]!"

user=input("Enter a name\n")

if user=="Adrian":
    print("Hello Boss!")
else:
    print("Hello", user)