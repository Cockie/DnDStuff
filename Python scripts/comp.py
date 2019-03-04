import random

tries = 10000



save = True
advantage = False

def fireball(level, chance):
    die = 6
    num = 8 + level - 3
    total = 0
    for i in range(0, tries):
        rolls = [0 ] *num
        for i in range(0, num):
            rolls[i] = random.randint(1, die)
            if rolls[i] == 1:
                rolls[i] = random.randint(1, die)
        total += sum(rolls)
    damage = total / tries
    print("Fireball:")
    print(str(1 - chance) + " chance of " + str(damage) + ", " + str(chance) + " chance of " + str(damage/2.))
    return damage * (1 - chance) + damage * chance / 2.

def vitriolic(level, chance):
    die = 4
    numinit = 10 + 2 * (level - 4)
    numthen = 5
    init = numinit * (1. + die) / 2.
    then = numthen * (1. + die) / 2.
    print("Vitriolic:")
    print(str(1 - chance) + " chance of " + str(init + then) + ", " + str(chance) + " chance of " + str(init / 2.))
    return (init + then) * (1 - chance) + init * chance / 2.

for dex in range(-5, 6):
    chance = (20. - 15. + 1 + dex) / 20.
    #chance = (20. - 16. + 1 + dex) / 20.

    print("DEX=" + str(dex))
    print("fireball " + str(fireball(4, chance)))
    print("vitriolic sphere " + str(vitriolic(4, chance)))