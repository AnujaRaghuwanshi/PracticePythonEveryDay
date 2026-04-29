# Guess the Number
# Difficulty level selection
#  Hard  attempts = 5 and easy attempts = 10
# computer selects random number between 1- 100
# check it and tell accordinlgy

import art
import random

print (art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

chosen_number = random.randint(1, 100)
level = input("Choose the difficulty level, hard or easy")

if level == "hard":
    attempts = 5
else:
    attempts = 10

for i in range(attempts):
    user_guessed_number = int(input("Take a guess: "))
    if user_guessed_number == chosen_number:
        print(f"You got it! The number was {chosen_number}")
        attempts -= 1
        break
    elif user_guessed_number < chosen_number:
        print("Too low!")
        attempts -= 1
        print(f"You have {attempts} attempts left.")
        print("Guess again")

    elif user_guessed_number > chosen_number:
        print ( "Too high !" )
        attempts -= 1
        print(f"You have {attempts} attempts left.")
        print (" Guess again")

