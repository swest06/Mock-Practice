correct = str(input("Correct answers: ")).split(" ")
d = dict()

# Take in answer and split it into list
x = str(input("answer: ")).split(" ")

# Takes scores until 999 is inputed. Splits id from score and adds to dict
while int(x[0]) != 999:
    key = x[0]
    x.remove(x[0])
    d[key] = x
    x = str(input("answer: ")).split(" ")


for key in d:
    score = 0
    for i in range(0, len(d[key])):
        if d[key][i] == correct[i]:
            score +=1
        elif d[key][i] == "x":
            continue
        else:
            score -=1
    d[key] = score
    print(key, str(score) + " marks")


# # T F T F T F T F T F T F T F T F T F T F T F T F T F T F T F
# 100 T F T T F F T F T F T F T F T T T F F F x F T x T F T F x F
# 101 T T T T T T T F T F x x x x x x T F T F T F T F T F F F F T
# 110 T F T F T F T F T F T F T F T F T F T F T F T F T F T F T F
# 999