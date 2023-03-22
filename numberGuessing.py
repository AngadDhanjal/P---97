print("Number Guessing Game")
import random 
number = random.randrange(1,9)
guess = int(input("Guess the number between 1 and 9 : "))

while guess != number:
    if guess < number:
        print ("You need to guess higher")
        print("Try again")
        guess = int(input("Guess the number between 1 and 9 : "))
    else:
        print ("You need to guess lower")
        print("Try again")
        guess = int(input("Guess the number between 1 and 9 : "))

print ("You have guessed the number correctly!")
