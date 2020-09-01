


import random
total = 0
tries = 1000000

succesA = 0
succesB = 0

mod = 5
modDC = -5

for i in range(0, tries):
    roll = random.randint(1, 20) + mod
    if roll >= 10 + modDC:
        succesA+=1
    
    DC = random.randint(1, 20) + modDC
    roll = random.randint(1, 20) + mod
    if roll >= DC:
        succesB+=1

print(succesA/tries)
print(succesB/tries)
    