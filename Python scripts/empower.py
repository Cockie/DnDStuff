import random
total = 0
tries = 1000000

die = 8
num = 6

emp = 5
method = 1
flames = True
bombardment = False
timebomb = 0

base = [0] * (die * num)
basenum = [0] * (die * num)
for i in range(0, tries):
    rolls = [0]*num
    for i in range(0, num):
        rolls[i] = random.randint(1, die)
    startdamage = sum(rolls)
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
        if bombardment:
            bomb = False
            for i in range(0, num):
                if rolls[i] == die:
                    bomb = True
            if bomb:
                timebomb+=1
                roll = random.randint(1, die)
                if roll <= die / 2 -1 and left > 0:
                    roll = random.randint(1, die)
                if flames and roll == 1:
                    roll = random.randint(1, die)
                total += roll
        base[startdamage - 1] += sum(rolls)
        basenum[startdamage - 1] += 1
        total += sum(rolls)
    

print(total / tries)
print(num*(1.+die)/2.)
print(total / tries - num*(1.+die)/2.)
for i in range(0, len(base)):
    if (basenum[i] > 0):
        print(str(i + 1) + " -> " + str(base[i]/basenum[i]) + " (" + str(basenum[i]) + " tries)")
if bombardment:
    print(timebomb / tries * 100)