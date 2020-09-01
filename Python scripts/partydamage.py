import random

rangertotal = 0
roguetotal = 0
sorcerertotal = 0
tries = 10000

AC = 14
bonusA = 9
bonusB = 7
damage = 4

flames = False
attacks = 2
sneak = 3
cantrip = 2
bomb = False

def doRoll(die, lucky=False):
    roll = random.randint(1, die)
    if lucky and roll == 1:
        roll = random.randint(1, die)
    return roll

#ranger
for i in range(0, tries):
    usedhunter = False
    for j in range(0, 2):
        first = doRoll(20, True)
        tohit = first + bonusA
        if first == 1:
            pass
        elif first == 20:
            rangertotal += 2 * (doRoll(8) + doRoll(6)) + damage
            if not usedhunter:
                rangertotal += 2 * (doRoll(8))
                usedhunter = True
        elif tohit >= AC:
            rangertotal += doRoll(8) + doRoll(6) + damage
            if not usedhunter:
                rangertotal += doRoll(8)
                usedhunter = True
#rogue
for i in range(0, tries):
    first = max(doRoll(20, True), doRoll(20, True))
    tohit = first + bonusB
    if first == 1:
        pass
    elif first == 20:
        roguetotal += 2 * (doRoll(8)) + damage
        for j in range(0, sneak):
            roguetotal += 2 * doRoll(6)
    elif tohit >= AC:
        roguetotal += doRoll(8) + damage
        for j in range(0, sneak):
            roguetotal += doRoll(6)
#sorcerer
for i in range(0, tries):
    first = doRoll(20, False)
    tohit = first + bonusB
    bombed = False
    if first == 1:
        pass
    elif first == 20:
        for j in range(0, cantrip):
            roll = doRoll(10, flames)
            sorcerertotal += 2 * roll
            if roll == 10 and not bombed and bomb:
                sorcerertotal += 2 * doRoll(10, flames) 
                bombed = True
    elif tohit >= AC:
        for j in range(0, cantrip):
            roll = doRoll(10, flames)
            sorcerertotal += roll
            if roll == 10 and not bombed and bomb:
                sorcerertotal += doRoll(10, flames) 
                bombed = True
            
print("Ranger: " + str(rangertotal / tries))
print("Rogue: " + str(roguetotal / tries))
print("Sorcerer: " + str(sorcerertotal / tries))