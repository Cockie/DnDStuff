import random

total = 0
tries = 100000

die = 10
num = 2

flames = False
adept = True

for i in range(0, tries):
    for j in range(0, num):
        roll = random.randint(1, die)
        if flames and roll == 1:
            roll = random.randint(1, die)
        if adept and roll == 1:
            roll = 2
        total += roll

print(total / tries)
print(num * (1. + die) / 2.)
print(total / tries - num * (1. + die) / 2.)