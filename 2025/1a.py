f = open("input1.txt", "r")
finalSum = 0
dial = 50
for line in f:
    if line[0] == 'L':
        dial -= int(line[1:])
        while dial < 0:
            dial += 100
    if line[0] == 'R':
        dial += int(line[1:])
        while dial > 99:
            dial -= 100
    if dial == 0:
        finalSum += 1
  
f.close()
print(finalSum)
