f = open("input1.txt", "r")
finalSum = 0
dial = 50
for line in f:
    direction = line[0] #The first letter
    count = int(line[1:]) #Everything but the first letter
    revolutions = (count//100) #Floor division
    finalSum += revolutions
    count %= 100
    if direction == 'L':
        if dial == 0: #If dial is already 0, don't doublecount it
            dial = 100
        dial -= count
        if dial == 0: #If we reach 0, count it.
            finalSum += 1
        if dial < 0:
            finalSum += 1
            dial += 100
    if direction == 'R':
        dial += count
        if dial > 99:
            finalSum += 1
            dial -= 100
  
f.close()
print(finalSum)
