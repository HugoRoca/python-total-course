from random import *

name = input("What's is your name? -> ")
print(f"Hi {name}, I just thought of a number between 1 and 100, can you guess it?")
print("You have only 8 attempts...")

endGame = False
number = randint(1, 100)

while not endGame:
    for attempt in range(1, 9):
        numberInput = int(input(f"Attempt {attempt}, Enter a number -> "))
        if 0 < numberInput <= 100:
            if numberInput == number:
                print(f"{name}, you win in {attempt} attempts! The number was {number}")
                break
            elif numberInput < number:
                print("The number is less")
            else:
                print("The number is more")
        else:
            print("The number has to be between 1 and 100")

        if attempt == 8:
            print("You don't have attempts")

    continueGame = input("You play again? (y/n) -> ")

    if continueGame == 'n':
        endGame = True
    else:
        number = randint(1, 100)

print("End game!")