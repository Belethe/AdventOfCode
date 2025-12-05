f = open("input3.txt", "r")
sum = 0
dial = 50
for line in f:
    currentFirstCiffer = 0
    currentSecondCiffer = 0
    bank = int(line)
    for n in str(bank//10):
        battery = int(n)
        if battery > currentFirstCiffer:
            currentFirstCiffer = battery
            currentSecondCiffer = 0
        else:
            currentSecondCiffer = max(currentSecondCiffer,battery)
    currentSecondCiffer = max(currentSecondCiffer,bank % 10)
    sum += currentFirstCiffer*10+currentSecondCiffer
  
f.close()
print(sum)
