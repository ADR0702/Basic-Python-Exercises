# Write a program that:
# Receives a word from the user (input)
# For each position i in the first half of the word, displays the letter at position i and the corresponding letter at position -1 - i (from the end)
# At the end, also displays the length of the word

word=input("Enter a word\n")

for i in range(len(word) //2):
    front_char=word[i]
    back_char=word[-1 -i]
    print(f"i={i} front={front_char} back={back_char}")

print(f"Length: {len(word)}")
    
    