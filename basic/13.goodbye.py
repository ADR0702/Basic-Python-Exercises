# Ask the add_text to enter text.
# If they type “exit”, stop the program and print “Goodbye!”.
# Otherwise, print the entered text and continue asking for input.




while True:
    add_text=input("Enter a text\n")
    if add_text.lower()=="exit":
        print("Goodbye!")
        break
    else:
        print("you printed", add_text)

