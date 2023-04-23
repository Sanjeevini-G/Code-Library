import random

def hat_check(n):
    hats = [i for i in range(n)]
    random.shuffle(hats)
    matches = 0

    for i in range(n):
        if hats[i] == i:
            matches += 1

    return matches

n = int(input("Enter the number of hats: "))
matches = hat_check(n)

print("Number of people who got their own hat back:", matches)
print("Probability that a person gets their own hat back:", matches/n)
