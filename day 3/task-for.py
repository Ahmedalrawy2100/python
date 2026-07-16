# Task: Print all elements in a list using a for loop

name="ahmed alrawy"

for char in name :
    print(f"[{char.upper()}]")





#task: Print all even numbers in a list using a for loop

my_list = [1, 2, 3, 4, 5,6,4, 7, 8, 9, 10]

for num in my_list:
    if num%2 ==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
else:
    print("All numbers have been checked.")
