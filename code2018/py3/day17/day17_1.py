def inClay(clay, coord):
    return coord in clay
def inWaterOrClay(water, clay, coord):
    #print ("checking",coord)
    if coord in water:
        return True
    if coord in clay:
        return True
    return False

##returns True if possible to continue
##false if no paths are found and water stagnates
def DFS(clay, water, current, yBound, xMin, xMax, branch = False):
    
    nextFlow = current
    
    if inWaterOrClay(water, clay, nextFlow):
        return
        
    print (current)
    water.append(nextFlow)

    if nextFlow[1] > yBound or nextFlow[0] <=xMin or nextFlow[0] >= xMax:
        return

    drop = []
    while True:
        nextFlow = (nextFlow[0],nextFlow[1]+1)
        if inWaterOrClay(water, clay, nextFlow):
            break
        drop.append(nextFlow)
        water.append(nextFlow)
    current = (nextFlow[0],nextFlow[1]-1)
    #DFS(clay, water, (nextFlow[0], nextFlow[1]+1), yBound, xMin, xMax)

    while len(drop) > 0:
        cur = drop.pop()
        if inWaterOrClay(water, clay, (cur[0]-1,cur[1]+1)):
            print ("left")
            DFS(clay, water, (cur[0]-1,cur[1]), yBound, xMin, xMax)
        elif not inWaterOrClay(water, clay, (cur[0]-1,cur[1])):
            DFS(clay, water, (cur[0]-1,cur[1]), yBound, xMin, xMax)
        if inWaterOrClay(water, clay, (cur[0]+1,cur[1]+1)):
            print ("right")
            DFS(clay, water, (cur[0]+1,cur[1]), yBound, xMin, xMax)
        elif not inWaterOrClay(water, clay, (cur[0]+1,cur[1])):            
            DFS(clay, water, (cur[0]+1,cur[1]), yBound, xMin, xMax)

    return True

clay = set()
with open("../../data/17.txt","r") as f:
    f = ["x=495, y=2..7",
"y=7, x=495..501",
"x=501, y=3..7",
"x=498, y=2..4",
"x=506, y=1..2",
"x=498, y=10..13",
"x=504, y=10..13",
"y=13, x=498..504"]
    #y=55, x=464..466
    for line in f:
        line=line.replace("\n","2")
        split = line.split(" ")
        f = line[0]
        fVal = int(split[0][split[0].find("=")+1:-1])

        sVal = split[1].split("..")
        sVal[0] = sVal[0][2:]
        vals = (fVal,  (int(sVal[0]) , int(sVal[1])))
        
        if f == "x":
            for y in range(vals[1][0], vals[1][1]+1):
                coord = (int(vals[0]), y)
                clay.add( coord )
        else:
            for x in range(vals[1][0], vals[1][1]+1):
                coord = (x, int(vals[0]))
                clay.add( coord )


spring = (500,0)
yMin = min(clay, key=lambda a:a[1])[1]
yMax = max(clay, key=lambda a:a[1])[1]
xMin = min(clay, key=lambda a:a[0])[0]
xMax = max(clay, key=lambda a:a[0])[0]
print ("starting DFS")
path = []

DFS(clay, path, spring, yMax, xMin, xMax)

print(len(path), yMin, yMax)
