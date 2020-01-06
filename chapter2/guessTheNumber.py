import random

numberToGuess = random.randint(1,30)
print numberToGuess

# ask the player to guess 5 times

for guessCount in range(1,5):
    print(' guess a number between 1 and 30')
    # converts guess to int
    guess = int(input())
    if guess < numberToGuess:
        print('number guessed is to low')
    elif guess > numberToGuess:
        print('number guessed is to high')
    else:
        break #number guessed is correct 

if guess == numberToGuess:
    print(' you guessed the number correctly it was ' + str(numberToGuess))
else:
    print(' you guessed incorrectly the number is ' + str(numberToGuess))