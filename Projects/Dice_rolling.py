#Made by quantenjager
import random

while True:
    question = input("Do you want to roll the dice? (y/n): ").lower()
    if question == "y":
        dice = random.randint(1, 6)
        print(f"{dice}")

    elif question == "n":
        print("Thanks for playing!")
        break

    else:
        print("Please enter y/n")