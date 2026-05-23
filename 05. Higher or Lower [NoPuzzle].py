import random

totalGuesses = 0
number = random.randint(0, 100)
print("Try to find my number between 0 and 100!\n")

while True:

    totalGuesses += 1
    triesText = "Try" if totalGuesses == 1 else "Tries"

    guess = int(input("Your guess: "))

    if guess == number:
        print(f"You got it, it was {number}! ({totalGuesses} {triesText})\n")
        totalGuesses = 0
        number = random.randint(0, 100)

    elif guess > number:
        print("Lower\n")

    elif guess < number:
        print("Higher\n")

