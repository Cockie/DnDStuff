import random

total = 0
tries = 10000

#AC = 16
bonus = 5

reckless = True


def doRoll(die):
    roll = random.randint(1, die)
    return roll


damageA = [0] * 11
damageB = [0] * 11
for AC in range (10,21):
    for i in range(0, tries):
        roll = 0
        if reckless:
            roll = max(doRoll(20), doRoll(20))
        else:
            roll = doRoll(20)
        if roll == 20:
            damageA[AC-10] += 3
            damageB[AC-10] += 3
            for i in range(0, 5):
                damageA[AC-10] += doRoll(6)
            for i in range(0, 3):
                damageB[AC-10] += doRoll(10)
        elif roll > 1 and roll + bonus >= AC:
            damageA[AC-10] += 3
            damageB[AC-10] += 3
            for i in range(0, 2):
                damageA[AC-10] += doRoll(6)
            damageB[AC-10] += doRoll(10)

    print("AC=" + str(AC))
    print(damageA[AC-10] / (tries))
    print(damageB[AC-10] / (tries))