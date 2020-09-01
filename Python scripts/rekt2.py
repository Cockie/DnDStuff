import random
import math
total = 0
tries = 100000

bonus = 1

res = [0] * 10

for i in range(0, tries):
    roll = random.randint(1, 12) + bonus
    roll = math.ceil(roll/2.)
    res[roll] += 1
    
print(res)
    