import random

while True:
    roll = input("Do You want to roll ")
    if roll == "Yes" or roll == "yes" or roll == "y":
        print(random.randint(1, 6))
    elif roll == "No" or roll == "no" or roll == "n":
        break
    else:
        break
