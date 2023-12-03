def thirdA(file):
    f = open(file)
    string = f.read()
    houses = [[0 for x in range(1000)] for x in range(1000)]
    i = 499
    j = 499
    houses[i][j] += 1
    lucky = 1
    for move in string:
        if move == "<":
            i -= 1
        elif move == ">":
            i += 1
        elif move == "^":
            j -= 1
        elif move == "v":
            j += 1
        else:
            print("wtf?")
        houses[i][j] += 1
        if houses[i][j] == 1:
            lucky += 1
    return lucky
            
def thirdB(file):
    f = open(file)
    string = f.read()
    houses = [[0 for x in range(1000)] for x in range(1000)]
    i = 499
    j = 499
    s = 499
    t = 499
    houses[i][j] += 2
    lucky = 1
    santa = True
    for move in string:
        if santa:
            if move == "<":
                i -= 1
            elif move == ">":
                i += 1
            elif move == "^":
                j -= 1
            elif move == "v":
                j += 1
            else:
                print("wtf?")
            houses[i][j] += 1
            if houses[i][j] == 1:
                lucky += 1
            santa = False
        else:
            if move == "<":
                s -= 1
            elif move == ">":
                s += 1
            elif move == "^":
                t -= 1
            elif move == "v":
                t += 1
            else:
                print("wtf?")
            houses[s][t] += 1
            if houses[s][t] == 1:
                lucky += 1
            santa = True
    return lucky
