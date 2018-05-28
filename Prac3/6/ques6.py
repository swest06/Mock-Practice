import random

# Random 4 digit int to individual string characters in list
num = list(str((random.randint(1000, 10000))))
print(num)
fin = False
while not fin:
    cows = 0
    bulls = 0
    guess = list(str(int(input("Enter a number: "))))
    for i, e in enumerate(guess):
        # Comparison
        if guess[i] == num[i]:
            cows +=1
        elif guess[i] in set(num):
            bulls += 1
    print("{} cows, {} bulls".format(cows, bulls))
    if cows == 4:
        fin = True

print("You won")