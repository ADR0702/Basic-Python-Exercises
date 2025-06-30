word=input("Enter a word\n")

for i in range(len(word) //2):
    primele_litere=word[i]
    ultimele_litere=word[-1 -i]
    print(f"din {word} primele litere sunt {primele_litere} si ultimele litere sunt {ultimele_litere}")

print(f"numarul total de litere este {len(word)}")