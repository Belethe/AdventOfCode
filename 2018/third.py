def thirdA(file):
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]
        coords = []
        sqinch = 0

        for line in lines:
            elem = line.split(' ')
            
            start = elem[2].split(',')
            start[0] = int(start[0])
            start[1] = int(start[1][:-1])
            
            size = elem[3].split('x')
            size[0] = int(size[0])
            size[1] = int(size[1])
            
            i = 0
            while i < size[0]:
                
                j = 0
                while j < size[1]:
                    coords.append(str(start[0]+i)+','+str(start[1]+j))
                    j += 1
                    
                i += 1


        for coord in coords:
            if coords.count(coord) > 1:
                sqinch += 1
                for x in coords:
                    if x == coord:
                        coords.remove(x)
                #coords = [elem for elem in coords if elem != coord]
                if sqinch %1000 == 0:
                    print(sqinch)
        print(len(coords))  
        return(sqinch)
