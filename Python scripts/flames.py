
import random
total = 0
tries = 100000

die = 6
num = 8

save = True
advantage = False


for i in range(0, tries):
    rolls = [0 ] *num
    for i in range(0, num):
        rolls[i] = random.randint(1, die)
    rolls = sorted(rolls)
    for i in range(0, num):
        if rolls[i] == 1:
            rolls[i] = random.randint(1, die)
    total += sum(rolls)

if save:
    for dex in range(-5,6):
    
        flames = total / tries
        other = num *( 1. +die ) /2
        chanceA = (20. - 15. + 1 + dex) / 20.
        chanceB = (20. - 16. + 1 + dex) / 20.
        
        print("DEX=" + str(dex))
        print("flames " + str(flames*(1.-chanceA) + flames/2.*chanceA))
        print("ASI " + str(other*(1.-chanceB) + other/2.*chanceB))
        print("NOW " + str(other * (1. - chanceA) + other / 3. * chanceA))
else:
    if advantage is False:
        crit = 0.05
    else:
        crit = 0.0975
    for AC in range(10, 18):
        flames = total / tries
        other = num * (1. + die) / 2
        chanceA = (20. - AC + 1 + 7) / 20.
        if advantage:
            chanceA = 1 - (1-chanceA)*(1-chanceA)
        if chanceA > 1:
            chanceA = 1
        if chanceA < crit:
            chanceA = crit
        chanceB = (20. - AC + 1 + 8) / 20.
        if advantage:
            chanceB = 1 - (1-chanceB)*(1-chanceB)
        if chanceB > 1:
            chanceB = 1
        if chanceB < crit:
            chanceB = crit
        
        print("AC=" + str(AC))
        print("flames " + str(flames * (chanceA - crit) + crit*flames*2))
        print("ASI " + str(other *(chanceB- crit) + crit*other*2))
        print("NOW " + str(other * (chanceA - crit) + crit * other * 2))