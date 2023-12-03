def secondA(file):
    f = open(file)
    string = f.read()
    total = 0
    for line in string.split("\n"):
        dimension = line.split("x")
        l = int(dimension[0])
        w = int(dimension[1])
        h = int(dimension[2])
        total += 2*l*w + 2*l*h + 2*w*h
        if l < w:
            if w < h:
                total += l*w
            else:
                total += l*h
        elif l < h:
            total += l*w
        else:
            total += w*h
    return total

def secondB(file):
    f = open(file)
    string = f.read()
    total = 0
    for line in string.split("\n"):
        dimension = line.split("x")
        l = int(dimension[0])
        w = int(dimension[1])
        h = int(dimension[2])
        total += l*w*h
        if l < w:
            if w < h:
                total += 2*l+2*w
            else:
                total += 2*l+2*h
        elif l < h:
            total += l*2+2*w
        else:
            total += w*2+2*h
    return total
