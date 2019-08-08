import random

min_val = int(input("Enter the minimum value of the dice "))
max_val = int(input("Enter the maximum value of the dice "))

while True:
    if max_val < min_val:
        print("Please Enter Valid Maximum and Minimum Values ")
        min_val = int(input("Enter the minimum value of the dice "))
        max_val = int(input("Enter the maximum value of the dice "))
    else:
        break

while True:
    roll = input("Do You want to roll ")
    if roll == "Yes" or roll == "yes" or roll == "y":
        print(random.randint(min_val, max_val))
    elif roll == "No" or roll == "no" or roll == "n":
        break
    else:
        break
