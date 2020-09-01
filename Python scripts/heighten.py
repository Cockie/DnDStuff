import random
damage = 28
for dex in range(-5, 6):
    chance = (20. - 15. + dex) / 20.
    normdamage = damage / 2. * chance + damage * (1 - chance)
    normdamage = normdamage * 3
    heightendamage = damage / 2. * chance * chance + damage * (1 - chance * chance)
    heightendamage = heightendamage * 2
    print("Dex = "+str(dex))
    print("Chance to save = " + str(100*chance))
    print("Chance to save w disadvantave = " + str(100 * chance * chance))
    print("3 normal fireball = " + str(normdamage))
    print("2 heighten fireball = " + str(heightendamage))