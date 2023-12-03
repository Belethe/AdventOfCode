def fifthA(file):
    string = open(file).read()
    lines = str.split(string, "\n")
    nice = 0
    for line in lines:
        vowel = 0
        previous = 0
        double = False
        forbidden = False
        for letter in line:
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                vowel += 1
            if letter == previous:
                double = True
            if (previous == 'a' and letter == 'b') or (previous == 'c' and letter == 'd') or (previous == 'p' and letter == 'q') or (previous == 'x' and letter == 'y'):
                forbidden = True
            previous = letter
            #print('vowel: ',vowel)
            #print('previous:',previous)
            #print('double: ',double)
        if vowel >= 3 and double and not forbidden:
            nice += 1
    return nice

def fifthB(file):
    lines = str.split(open(file).read(), "\n")
    nice = 0
    for line in lines:
        pairs = [(0,0)]
        pairRepeat = False
        twoPrev = 0
        prev = 0
        repeat = False
        for l in line:
            if (prev,l) in pairs:
                if l == prev:
                    print(line) #don't count aaaba only aabaa
                pairRepeat = True
            else:
                pairs += [(prev,l)]
            if l == twoPrev:
                repeat = True
            twoPrev = prev
            prev = l
        if pairRepeat and repeat:
            nice += 1
    return nice
