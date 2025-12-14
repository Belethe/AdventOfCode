# f = open("test5.txt", "r")
f = open("input5.txt", "r")

fresh = 0
ranges = []
ids = []
for line in f:
    if "-" in line:
        ranges.append(line)
    else:
        ids.append(line)
f.close()

def splitRange(range):
    split = range.split("-")
    return (int(split[0]), int(split[1]))

ranges = list(map(splitRange, ranges))

ids = ids[1:] #Remove the empty line
ids = list(map(int, ids))

for id in ids:
    for range in ranges:
        if range[0] <= id and id <= range[1]:
            fresh = fresh + 1
            break

print(fresh)
