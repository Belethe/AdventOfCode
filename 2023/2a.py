import re
f = open("input2.txt", "r")
idsum = 0
maxred = 12
maxgreen = 13
maxblue = 14

for line in f:
    gameid = int(re.findall(r'\d+',line)[0])

    line = line.partition(": ")[2].rstrip("\n")

    draws = line.split(";")
    red = 0
    blue = 0
    green = 0
    
    for draw in draws:
        colours = draw.split(", ")
        for colour in colours:
            x = colour.split()
            if x[1] == "red":
                red = max(red,int(x[0]))
            elif x[1] == "green":
                green = max(green,int(x[0]))
            elif x[1] == "blue":
                blue = max(blue,int(x[0]))

    if red <= maxred and blue <= maxblue and green <= maxgreen:
        idsum += gameid

print(idsum)
