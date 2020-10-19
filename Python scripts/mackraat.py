import random

total = 0
tries = 10000

#AC = 16
bonus = 4
prof = 3


AC = 15

reckless = True

att = 2
sneak = 3

rage = 2
divine = 2

SS = True
GWM = True
Scatter = True

tries = 100000

def doRoll(die, advantage = False, lucky = False):
    if lucky:
        roll = doRoll(die, advantage)
        if roll == 1:
            roll = doRoll(die)
        return roll
    if advantage:
        return max(random.randint(1, die), random.randint(1, die))
    else:
        return random.randint(1, die)



#kraat
krdam = 0
for i in range(0, tries):
    rage = i % 2 == 0
    rAC = AC
    if GWM:
        rAC += 5
    if rage:
        useddivine = False
        num = att
        # GWM, one in 2 times?
        if doRoll(3) == 1:
            num += 1
        for j in range(0, num):
            roll = doRoll(20, True)
            if roll == 1:
                pass
            elif roll == 20 or roll == 19:
                krdam += doRoll(10) + doRoll(10) + doRoll(10) + bonus + rage
                if GWM:
                    krdam += 10
                if not useddivine:
                    krdam += doRoll(6) + doRoll(6) + divine
                    useddivine = True
            elif roll + prof + bonus >= rAC:
                krdam += doRoll(10) + bonus + rage
                if GWM:
                    krdam += 10
                if not useddivine:
                    krdam += doRoll(6) + divine
                    useddivine = True
    else:
        num = att
        # GWM, one in 3 times?
        if doRoll(3) == 1:
            num += 1
        for j in range(0, num):
            roll = doRoll(20)
            if roll == 1:
                pass
            elif roll == 20 or roll == 19:
                krdam += doRoll(10) + doRoll(10) + doRoll(10) + bonus
            elif roll + prof + bonus >= AC:
                krdam += doRoll(10) + bonus
                
print("KRaat: " + str(krdam/tries) + " per turn")
macdam = 0
for i in range(0, tries):
    num = 1
    if Scatter and i % 3 == 0:
        num = 2
    rAC = AC
    if SS:
        rAC += 5
    usedSneak = False
    for j in range(0, num):
        roll = doRoll(20, True, True)
        if roll == 1:
            pass
        elif roll == 20 or roll == 19:
            macdam += doRoll(8) + doRoll(8) + bonus
            if SS: 
                macdam += 10
            if num == 2:
                macdam += doRoll(10) + doRoll(10)
            if not usedSneak:
                usedSneak = True
                for r in range(0, 2*sneak):
                    macdam += doRoll(6)
        elif roll + prof + bonus + 2 >= rAC:
            macdam += doRoll(8) + bonus
            if SS: 
                macdam += 10
            '''if num == 2:
                macdam += doRoll(10)'''
            if not usedSneak:
                usedSneak = True
                for r in range(0, sneak):
                    macdam += doRoll(6)
print("Mac normal: " + str(macdam/tries) + " per turn")


cl2dam = 0
for i in range(0, tries):
    if i % 12 == 0:
        cl2dam += 105
    else:
        num = 1
        for j in range(0, num):
            roll = doRoll(20)
            if roll == 1:
                pass
            elif roll == 20:
                cl2dam += doRoll(10) + doRoll(10) + doRoll(10) + doRoll(10) +3
            elif roll + prof + 3 >= AC:
                cl2dam += doRoll(10) + doRoll(10) +3
print("Clink FB: " + str(cl2dam/tries) + " per turn")

cldam = 0
for i in range(0, tries):
    if i % 12 == 0:
        cldam += 105
    else:
        num = 1
        if i%2 == 0:
            for j in range(0, num):
                roll = doRoll(20)
                if roll == 1:
                    pass
                elif roll == 20:
                    cldam += doRoll(8) + doRoll(8) + doRoll(8) + doRoll(8) + bonus + 3
                    if i % 3 == 0:
                        cldam += doRoll(8) + doRoll(8)
                elif roll + prof + bonus >= AC:
                    cldam += doRoll(8) + doRoll(8) + bonus + 3
                    if i % 3 == 0:
                        cldam += doRoll(8) + doRoll(8)
        else:
            for j in range(0, num):
                roll = doRoll(20, True)
                if roll == 1:
                    pass
                elif roll == 20:
                    cldam += doRoll(6) + doRoll(6) + doRoll(6) + doRoll(6)+ doRoll(8) + doRoll(8) + bonus + 3
                    if i % 3 == 0:
                        cldam += doRoll(8) + doRoll(8)
                elif roll + prof + bonus >= AC:
                    cldam += doRoll(6) + doRoll(6) + doRoll(8) + bonus + 3
                    if i % 3 == 0:
                        cldam += doRoll(8) + doRoll(8)
print("Clink BB: " + str(cldam/tries) + " per turn")
        
krdam = 0
for i in range(0, tries):
    if i % 2 == 0:
        roll = doRoll(20)
        if roll == 1:
            pass
        elif roll == 20:
            krdam += doRoll(8) + doRoll(8) + 3
        elif roll + prof + 3 >= AC:
            krdam += doRoll(8) + 3
    if i % 3 == 0:
        krdam += 40
    elif i % 8 == 7:
        krdam += (doRoll(12) + doRoll(12) + doRoll(12)) * 1.5
    else:
        roll = doRoll(20)
        if roll == 1:
            pass
        elif roll == 20:
            krdam += doRoll(6) + doRoll(6) + bonus + doRoll(8) + doRoll(8) +2
            if i % 3 == 0:
                krdam += doRoll(8) + doRoll(8)
        elif roll + prof + bonus >= AC:
            krdam += doRoll(6) + bonus + doRoll(8) +2
            if i % 3 == 0:
                krdam += doRoll(8) + doRoll(8)
print("Krivkash: " + str(krdam/tries) + " per turn")
            