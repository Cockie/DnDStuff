import random
total = 0
tries = 100000

die = 10
num = 2

emp = 5
method = 1
flames = False

for i in range(0, tries):
    rolls = [0]*num
    for i in range(0, num):
        rolls[i] = random.randint(1, die)
    rolls = sorted(rolls)
    firstnon1 = 0
    for i in range(0, num):
        if rolls[i] != 1:
            firstnon1 = i
            break
    #firstnon1 = 0
    if method == 1:
        left = emp
        for i in range(firstnon1, num):
            if rolls[i] <= die / 2 -1  and left > 0:
                rolls[i] = random.randint(1, die)
                left -= 1
        for i in range(0, firstnon1):
            if rolls[i] <= die / 2 -1 and left > 0:
                rolls[i] = random.randint(1, die)
                left -= 1
    if flames:
        for i in range(0, num):
            if rolls[i] == 1:
                rolls[i] = random.randint(1, die)
    total += sum(rolls)
    

print(total / tries)
print(num*(1.+die)/2.)
print(total / tries - num*(1.+die)/2.)