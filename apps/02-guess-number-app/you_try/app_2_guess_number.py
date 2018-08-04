"""
Jump Start Python App 2 Number App
"""
__author__ = "Jason Belk"
import random

header_space = "-" * 37
app_name = "GUESS THE NUMBER APP"
print(header_space)
buffer = " " * 10
print(buffer+app_name+buffer)
print(header_space)

target = random.randint(0,100)
attempts = True

while attempts:
    guess = int(input("\n Guess a number between 0 and 100: "))
    if guess < target:
        print("Sorry but " + str(guess) + " is LOWER than the number")
    elif guess > target:
        print("Sorry but " + str(guess) + " is HIGHER than the number")
    else:
        print("YES! You've got it. The number was " + str(target))
        attempts = False
