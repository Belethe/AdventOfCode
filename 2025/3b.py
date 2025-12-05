f = open("test3.txt", "r")
sum = 0
dial = 50
for line in f:
    joltage = [0,0,0,0,0,0,0,0,0,0,0,0]
    bank = int(line)
    i = len(line)
    for n in str(bank):
        battery = int(n)
        if   i > 12 & battery > joltage[0]:
            joltage = [battery,     0,          0,          0,          0,          0,          0,          0,          0,          0,          0,          0]
        elif i > 11 & battery > joltage[1]:
            joltage = [joltage[0],  battery,    0,          0,          0,          0,          0,          0,          0,          0,          0,          0]
        elif i > 10 & battery > joltage[2]:
            joltage = [joltage[0],  joltage[1], battery,    0,          0,          0,          0,          0,          0,          0,          0,          0]
        elif i >  9 & battery > joltage[3]:
            joltage = [joltage[0],  joltage[1], joltage[2], battery,    0,          0,          0,          0,          0,          0,          0,          0]
        elif i >  8 & battery > joltage[4]:
            joltage = [joltage[0],  joltage[1], joltage[2], joltage[3], battery,    0,          0,          0,          0,          0,          0,          0]
        elif i >  7 & battery > joltage[5]:
            joltage = [joltage[0],  joltage[1], joltage[2], joltage[3], joltage[4], battery,    0,          0,          0,          0,          0,          0]
        elif i >  6 & battery > joltage[6]:
            joltage = [joltage[0],  joltage[1], joltage[2], joltage[3], joltage[4], joltage[5], battery,    0,          0,          0,          0,          0]
        elif i >  5 & battery > joltage[7]:
            joltage = [joltage[0],  joltage[1], joltage[2], joltage[3], joltage[4], joltage[5], joltage[6], battery,    0,          0,          0,          0]
        elif i >  4 & battery > joltage[8]:
            joltage = [joltage[0],  joltage[1], joltage[2], joltage[3], joltage[4], joltage[5], joltage[6], joltage[7], battery,    0,          0,          0]
        elif i >  3 & battery > joltage[9]:
            joltage = [joltage[0],  joltage[1], joltage[2], joltage[3], joltage[4], joltage[5], joltage[6], joltage[7], joltage[8], battery,    0,          0]
        elif i >  2 & battery > joltage[10]:
            joltage = [joltage[0],  joltage[1], joltage[2], joltage[3], joltage[4], joltage[5], joltage[6], joltage[7], joltage[8], joltage[9], battery,    0]
        elif battery > joltage[11]:
            joltage[11] = battery
        # print(bank, n, i, joltage)
        i -= 1
    joltagestring = str(joltage[0])+str(joltage[1])+str(joltage[2])+str(joltage[3])+str(joltage[4])+str(joltage[5])+str(joltage[6])+str(joltage[7])+str(joltage[8])+str(joltage[9])+str(joltage[10])+str(joltage[11])
    sum += int(joltagestring)
    print(joltage)
  
f.close()
print(sum)
print(sum==3121910778619) #Test result
