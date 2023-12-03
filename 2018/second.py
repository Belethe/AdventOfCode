def checkSum(file):
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

        doubles = 0
        triples = 0

        for line in lines:
            d = 0
            t = 0
            for letter in line:
                c = line.count(letter)
                if d == 0 and c == 2:
                    d = 1
                elif t == 0 and c == 3:
                    t = 1
            doubles += d
            triples += t

        return doubles * triples

def compareId(file):
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

        for line in lines:
            line = lines[0]
            lines.pop(0)
            
            for comp in lines:
                dif = 0
                index = 0
                i = 0
                while i < len(line) and dif < 2:
                    if line[i] != comp[i]:
                        dif += 1
                        index = i
                    i += 1
                if dif < 2:
                    result = list(line)
                    result.pop(index)
                    return ''.join(result)
                
        return 'oops'
