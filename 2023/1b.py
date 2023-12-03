f = open("input1.txt", "r")
finalSum = 0
for line in f:
    numbers = []
    replace = True
    while replace:
        nextReplace = []
        nextReplaceOriginal = []
        nextReplace.append(line.find("one"))
        nextReplace.append(line.find("two"))
        nextReplace.append(line.find("three"))
        nextReplace.append(line.find("four"))
        nextReplace.append(line.find("five"))
        nextReplace.append(line.find("six"))
        nextReplace.append(line.find("seven"))
        nextReplace.append(line.find("eight"))
        nextReplace.append(line.find("nine"))
        
        if max(nextReplace) == -1: #No more written numbers
            replace = False
        else:
            nextReplaceOriginal.extend(nextReplace)
            nextReplace.sort()
            while min(nextReplace) == -1: #Find lowest that isn't -1
                nextReplace.remove(-1)
            
            index = min(nextReplace)
            number = nextReplaceOriginal.index(index)

            if number == 0:
                x = line.partition("one")
                line = x[0]+"1e"+x[-1]
            elif number == 1:
                x = line.partition("two")
                line = x[0]+"2o"+x[-1]
            elif number == 2:
                x = line.partition("three")
                line = x[0]+"3e"+x[-1]
            elif number == 3:
                x = line.partition("four")
                line = x[0]+"4"+x[-1]
            elif number == 4:
                x = line.partition("five")
                line = x[0]+"5e"+x[-1]
            elif number == 5:
                x = line.partition("six")
                line = x[0]+"6"+x[-1]
            elif number == 6:
                x = line.partition("seven")
                line = x[0]+"7n"+x[-1]
            elif number == 7:
                x = line.partition("eight")
                line = x[0]+"8t"+x[-1]
            elif number == 8:
                x = line.partition("nine")
                line = x[0]+"9e"+x[-1]
        

        
    for letter in line:
        if letter.isnumeric():
            numbers.append(int(letter))
    first = numbers[0]
    last = numbers[-1]
    finalSum += 10*first+last
  
f.close()
print(finalSum)
