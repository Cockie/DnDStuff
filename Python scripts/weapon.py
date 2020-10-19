import random

tries = 10000
totalA = 0
totalB = 0
# AC = 14
bonus = 8
damage = 5
flamedie = 6
magic = 1


def doRoll(die, lucky=False):
    if die == 0:
        return 0
    roll = random.randint(1, die)
    if lucky and roll == 1:
        roll = random.randint(1, die)
    return roll


# ranger
for AC in range(10, 22):
    totalA = totalB = 0
    for i in range(0, tries):
        first = doRoll(20)
        tohit = first + bonus + magic
        if first == 20:
            totalA += doRoll(8) + doRoll(8)+ doRoll(4)+ doRoll(4) + damage
        elif first != 1:
            if tohit >= AC:
                totalA += doRoll(8)+ doRoll(4) + damage
        if True or i % 5 != 0:
            first = doRoll(20)
            tohit = first + bonus
            if first == 20:
                totalB += doRoll(8) + doRoll(8) + doRoll(flamedie)+ doRoll(flamedie) + damage
            elif first != 1:
                if tohit >= AC:
                    totalB += doRoll(8)+ doRoll(flamedie) + damage
    print(AC)
    print(totalA / tries)
    print(totalB / tries)
