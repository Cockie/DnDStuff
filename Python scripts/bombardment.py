import random
total = 0

die = 6
times = 9
flames = True
test = 2
attempts = 100000

def doRoll():
    roll = random.randint(1, die)
    if flames and roll == 1:
        roll = random.randint(1, die)
    return roll

if test == 1:
    max = 0
    for i in range(0, attempts):
        bomb = False
        dmg = 0
        for j in range(0, times):
            roll = doRoll()
            dmg += roll
            while roll == die:
                roll = doRoll()
                dmg += roll
        total += dmg
        if dmg > max:
            max = dmg
    print("Max="+str(max))
elif test == 2:
    max = 0
    bombed = 0
    for i in range(0,attempts):
        bomb = False
        dmg = 0
        for j in range(0, times):
            roll = doRoll()
            if roll == die:
                bomb = True
            dmg += roll
        if bomb:
            bombed += 1
            roll = doRoll()
            dmg += roll
        total += dmg
        if dmg > max:
            max = dmg
    print("Max=" + str(max))
    print("Bombed " + str(bombed / attempts * 100.))
elif test == 3:
    for i in range(0, attempts):
        rolls = [0] * times
        for j in range(0, times):
            rolls[j] = doRoll()
        rolls = sorted(rolls)
        rolls[times - 1] = 2 * rolls[times - 1]
        total += sum(rolls)
    

print(total / attempts)
print(times * (1. + die)/2.)
print(total / attempts - times * (1. + die)/2.)
