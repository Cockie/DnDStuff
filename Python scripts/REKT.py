import random
import math


tries = 100000

def roll():
    return random.randint(1,6)

A = 2
B = 2
C = 1
D = 1

diff = math.floor(((A+B) - (C+D))*1./2.)

resA = [0]*10
resB = [0]*10

for i in range(0, tries):
    r = roll()
    resA[r+2]+=1
    
    r1 = roll() + (A + B)/2.
    r2 = roll() + (C + D)/2.
    r = math.floor(r1 - r2)
    resB[r + 2] += 1

for i in range(0, 10):
    resA[i] = resA[i]/tries
    resB[i] = resB[i] / tries
print(resA)
print(resB)