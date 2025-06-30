# Write a program that receives a list of numbers and displays only the even numbers.

no_list=[22, 5, 43, 12, 71, 66, 7, 18]
checking=False

for i in no_list:
    if i % 2 ==0:
        print(f"even numbers are {i}")
    checking=True
if not checking:
        print("there is no even numbers")

    
