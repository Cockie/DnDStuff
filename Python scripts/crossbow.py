import random
total = 0
tries = 10000

AC = 12
bonus = 6



def doRoll(die, lucky = False):
    roll = random.randint(1, die)
    if lucky and roll == 1:
        roll = random.randint(1, die)
    return roll

dam = 0
damhand = 0
for i in range(0, tries):
    roll = max(doRoll(20, True), doRoll(20, True))
    if roll == 20:
        dam += doRoll(8) + doRoll(8) + doRoll(6) + doRoll(6)+ doRoll(6) + doRoll(6) + 4
    elif roll > 1:
        roll += bonus
        if roll >= AC:
            dam += doRoll(8) + doRoll(6) + doRoll(6) + 4
    
    sneak = False
    for i in range(0, 2):
        roll = doRoll(20, True)
        if roll == 20:
            
            damhand += doRoll(6) + doRoll(6) + 4
            if not sneak:
                damhand += + doRoll(6) + doRoll(6) + doRoll(6) + doRoll(6)
                sneak = True
        elif roll > 1:
            roll += bonus
            if roll >= AC:
                damhand += doRoll(6) + 4
                if not sneak:
                    damhand += doRoll(6) + doRoll(6)
                    sneak = True
                    
print("Normal CB: " + str(1.*dam / tries))
print("HCB: " + str(1.*damhand / tries))