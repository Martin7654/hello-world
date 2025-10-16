import math
import random   
random_number = random.randint(1, 10)
guess = int(input("Enter a number between 1 and 10: "))
while guess != random_number:
    guess = (int(input("You guessed wrong, try again: ")))
else:
    print("You guessed right!")