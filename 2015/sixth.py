def A(lights, nwX, nwY, seX, seY, instr):
    for x in range(nwX, seX+1):
        for y in range(nwY, seY+1):
            if instr == 'on':
                lights[x][y] = True
            elif instr == 'off':
                lights[x][y] = False
            else:
                lights[x][y] = not lights[x][y]
    return lights

def B(lights, nwX, nwY, seX, seY, instr):
    for x in range(nwX, seX+1):
        for y in range(nwY, seY+1):
            if instr == 'on':
                lights[x][y] += 1
            elif instr == 'off':
                if lights[x][y] > 0:
                    lights[x][y] -= 1
            else:
                lights[x][y] += 2
    return lights

def sixth(file, rangeOfLights, version):
    lines = str.split(open(file).read(), "\n")
    lights = [[0 for x in range(rangeOfLights)] for x in range(rangeOfLights)]
    for line in lines:
        words = str.split(line, " ")
        if words[0] == 'turn':
            x = 1                
        else:
            x = 0
        instr = words[x]
        nw = str.split(words[x+1], ",")
        se = str.split(words[x+3], ",")
        lights = version(lights, int(nw[0]),int(nw[1]),int(se[0]),int(se[1]),instr)
    on = 0
    for x in range(rangeOfLights):
        for y in range(rangeOfLights):
            if version == 'A':
                if lights[x][y]:
                    on += 1
            else:
                on += lights[x][y]

    #print (lights)
    return on
