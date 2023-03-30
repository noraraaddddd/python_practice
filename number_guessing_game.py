#Number guessing game
#Goal: Grtting introduced to the random module

import random

low = 1
high = 100
guesses = 0

number = random.randint(low, high)
while True:
 guess = int(input(f"Enter a number between {low} and {high}: "))
 guesses += 1
 if guess > number:
    print("Guess is too high!")
 elif guess < number:
    print("Guess is too low!")
 else:
   print("CORRECT!")
   break
print(f"This round took you {guesses} guesses")