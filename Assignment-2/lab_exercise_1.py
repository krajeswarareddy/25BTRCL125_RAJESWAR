# Lab Exercise 1: Number Guessing Game

import random

secret_number = random.randint(1, 100)

print("===== NUMBER GUESSING GAME =====")
print("I have selected a number between 1 and 100.")

guess = int(input("Enter your guess: "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    guess = int(input("Try again: "))

print("Congratulations! You guessed the correct number.")