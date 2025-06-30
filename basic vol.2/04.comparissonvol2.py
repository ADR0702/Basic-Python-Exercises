# Ask the user for a word.
# Iterate over the first half of the word with a for loop.
# For each position i, save in two separate variables the letter from the front (front_char) and the symmetrical letter from the back (back_char).
# For each position, display a message like:

word=input("Enter a word\n")

for i in range(len(word) //2):
    front_char=word[i]
    back_char=word[-1 -i]
    print(f"At position {i}: front letter is {front_char}, back letter is {back_char}")

print(f"Length of the word is: {len(word)}")