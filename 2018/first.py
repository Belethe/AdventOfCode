def Freq(file):
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

        freq = 0

        for line in lines:
            freq += int(line)

        return freq

def Freq2(file):
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

        freq = 0
        freqList= [0]
        i = 0
        
        while True:
            for line in lines:

                freq += int(line)

                if freq in freqList:
                    return freq
                else:
                    freqList.append(freq)
            i+=1
            print(i)

        
