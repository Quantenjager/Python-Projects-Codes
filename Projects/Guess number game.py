#Made by quantenjager
import random

num = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess > num:
            print("lower")
        elif guess < num:
            print("higher")
        else:
            print("Congratulation the number was " + str(num))
            break

    except ValueError:
        print("Please enter a number")

