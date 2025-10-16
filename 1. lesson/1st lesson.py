import random
random_number=random.randint(1,9) #random number between 1 and 9
guess=int(input("Please guess a number between 1 and 9:"))
if guess==random_number:
    print("You guessed right!")
else :
    print("Wrong guess, try again!")

#while instead of if with !=
#line 3 in the while loop