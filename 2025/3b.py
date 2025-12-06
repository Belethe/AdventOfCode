def findMax(start, end, string):
    currentMax = 0
    currentMaxIndex = 0
    index = start
    searchString = string[start:end]
    if end == 0: ##if end = 0, include rest of string
        searchString = string[start:]
    for nStr in searchString:
        n = int(nStr)
        if (n > currentMax):
            currentMax = n
            currentMaxIndex = index
        index += 1
    return (currentMax, currentMaxIndex)


f = open("input3.txt", "r")
sum = 0
dial = 50
for line in f:
    bank = int(line)
    bankStr = str(bank) #No end of line char
    joltageArray = []
    currentMax = 0
    currentMaxIndex = 0
    index = 0

    joltageArray.append(findMax(0,-11,bankStr)) #Find first ciffer

    i = -10
    while i <= 0: #Find the rest of the ciffers
        start = joltageArray[-1][1]+1 #Search in bank starting after the last confirmed ciffer
        end = i #End in time
        joltageArray.append(findMax(start,end,bankStr)) #Found ciffer and its index
        i += 1

    joltage = ""
    for jolt in joltageArray:
        joltage += str(jolt[0]) #Get ciffer from tuple
    sum += int(joltage)
  
f.close()
print(sum)
# print(sum==3121910778619) #Test result