f = open("input1.txt", "r")
finalSum = 0
for line in f:
    numbers = []
    for letter in line:
        if letter.isnumeric():
            numbers.append(int(letter))
    first = numbers[0]
    last = numbers[-1]
    finalSum += 10*first+last
  
f.close()
print(finalSum)
