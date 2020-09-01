
import random
total = 0
tries = 100000

AC = 16
bonusA = 9
bonusB = 7
damage = 4


attacks = 3


def doRoll(die, lucky = False):
    roll = random.randint(1, die)
    if lucky and roll == 1:
        roll = random.randint(1, die)
    return roll

for i in range(0, tries):
    usedhunter = False
    for j in range(0, attacks):
        first = doRoll(20, True)
        tohit = first + bonusA
        if first == 1:
            pass
        elif first == 20:
            total += 2 * (doRoll(8) + doRoll(6)) + damage
            if not usedhunter:
                total += 2 * (doRoll(8))
                usedhunter = True
        elif tohit >= AC:
            total += doRoll(8) + doRoll(6) + damage
            if not usedhunter:
                total += doRoll(8)
                usedhunter = True
    for j in range(0, attacks):
        first = doRoll(20)
        tohit = first + bonusB
        if first == 1:
            pass
        elif first == 20:
            total += 2 * (doRoll(8) + doRoll(6)) + damage
        elif tohit >= AC:
            total += doRoll(8) + doRoll(6) + damage
        
print(total / tries)