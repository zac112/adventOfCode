with open('data.txt') as f:
    ranges, ids = f.read().split("\n\n")
    ranges = list(map(lambda a:a.split("-"),ranges.split("\n")))
    ranges = [[int(a),int(b)] for a,b in ranges]
    ranges.sort(key=lambda a:a[0])
    ids = map(int,ids.split("\n"))


fresh = 0
for i in ids:
    for a,b in ranges:
        if a <= i <= b:
            fresh += 1
            break
        
print("Part 1:",fresh)

combinedRanges = [ranges.pop(0)]
while ranges:
    currRange = ranges.pop(0)
    head = combinedRanges[-1]
    if head[0] <= currRange[0] <= head[1]:
        head[1] = max(currRange[1], head[1])
    else:
        combinedRanges.append(currRange)

allIDs = 0
for a,b in combinedRanges:
    allIDs += (b-a)+1
print("Part 2",allIDs)
