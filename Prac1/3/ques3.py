import random
num = random.randint(0, 99)

#Without boolean flag
guess = int(input("Guess a number: "))
trys = 1
while guess != num:
    if guess < num:
        guess = int(input("Too low. Guess again: "))
    elif guess > num:
        guess = int(input("Too high. Guess again: "))
    trys += 1
print("Correct. It took you {} guesses.".format(trys))



# With boolean flag
guess = int(input("Guess a number: "))
trys = 1

while guess != num:
    if guess < num:
        guess = int(input("Too low. Guess again: "))
    elif guess > num:
        guess = int(input("Too high. Guess again: "))
    trys += 1
print("Correct. It took you {} guesses.".format(trys))