# Create a program that asks the user for a password.
# If the entered password is not 'python123', the program keeps asking for the password.
# When the user enters the correct password, the program displays: Access granted

program=input("Please enter the password\n")

while program!="python123":
    print("try again")
    program=input("Please enter the password\n")  
      
print("Acces Granted")
    
    