ranges = {}
with open("data.txt") as file:
    for a,b in [x.split(' -> ') for x in file.readlines()]:
        ranges.setdefault(tuple(map(int,a.split(','))),[]).append(tuple(map(int,b.split(','))))

print(ranges)

vents = {}
for start,ends in ranges.items():
    for end in ends:        
        #print(start,end)
        xDir = 1 if start[0]<end[0] else -1
        xDir = xDir if start[0]!=end[0] else 0
        
        yDir = 1 if start[1]<end[1] else -1
        yDir = yDir if start[1]!=end[1] else 0

        #print(xDir,yDir)
        x,y = start[0], start[1]

        length = max(abs(end[0]-start[0]), abs(end[1]-start[1]))
        for diff in range(1+length):
            #print(x,y)
            vents[(x,y)] = vents.get((x,y),0)+1
            x += xDir
            y += yDir
        
print(len([x for x in vents.values() if x >= 2]))


