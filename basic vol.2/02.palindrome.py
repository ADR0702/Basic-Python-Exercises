# You ask the user for a word.
# You check if that word is a palindrome.
# You display the appropriate message:
# "It is a palindrome" or
# "It is not a palindrome".

word=input("Please enter a word\n")
check=False
for i in word:
    if i[0]==i[-1]:
        print("it's a palindrome")
        check=True
        
    else:
        print("it's not a palindrome")