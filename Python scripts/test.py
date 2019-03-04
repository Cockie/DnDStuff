import random
total = 0

for i in range(0,1000000):
    roll = random.randint(1,10)
    if roll == 1:
        roll = random.randint(1, 10)
    total += roll

print(total / 1000000 * 4)
print(4*(1.+10.)/2.)
print(total / 1000000 * 4 - 4*(1.+10.)/2.)