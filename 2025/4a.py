f = open("input4.txt", "r")

dict = {}
sum = 0

for i, line in enumerate(f):
    for j, char in enumerate(line):
        if char == '@':
            dict[str(i)+" "+str(j)] = 0
f.close()

for d in dict:
    (i,j)=d.split(" ")
    i = int(i)
    j = int(j)
    for x in [i-1, i, i+1]:
        for y in [j-1, j, j+1]:
            if (i != x or j != y) and str(x)+" "+str(y) in dict:
                dict[str(x)+" "+str(y)] = dict[str(x)+" "+str(y)] + 1

for value in dict.values():
    if value < 4:
        sum = sum +1

print(sum)