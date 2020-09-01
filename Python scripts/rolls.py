import random

total = 0
tries = 100000

AC = 16
bonus = 5
die = 10
attacks = 4


def doRoll(die, lucky=False):
    roll = random.randint(1, die)
    if lucky and roll == 1:
        roll = random.randint(1, die)
    return roll

damageA = 0
damageB = 0
for i in range(0, tries):
    roll = doRoll(20, False)
    if roll == 20:
        for i in range(0, attacks):
            damageA += 2 * doRoll(8, False)
    elif roll > 1:
        for i in range(0, attacks):
            damageA += doRoll(8, False)

    for i in range(0, attacks):
        roll = doRoll(20, False)
        if roll == 20:
            damageB += 2 * doRoll(8, False)
        elif roll > 1:
            damageB += doRoll(8, False)
    

print(damageA / tries)
print(damageB / tries)