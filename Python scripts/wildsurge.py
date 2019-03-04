import random
lines = []
with open('surges') as f:
    for line in f:
        lines.append(line.replace('\n', ''))
         
output = [''] * 100
for line in lines:
    if 'potted plant' in line:
        output[41] = line
    else:
        index = random.randint(0,99)
        while index == 41 or output[index] != '':
            index = index = random.randint(0,99)
        output[index] = line
     
i = 1   
for line in output:
    print(str(i) + "\t" + line)
    i+=1
            