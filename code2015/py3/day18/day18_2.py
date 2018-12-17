areaSize = 100

def printArea(area):
    grid = [["." for y in range(areaSize)] for x in range(areaSize)]
    for c in area:
        grid[c[0]][c[1]] = "#"

    for line in grid:
        print ("".join(line))
    print("")

area = set([(0,0), (0,areaSize-1), (areaSize-1, 0), (areaSize-1, areaSize-1)])
with open("../../data/18.txt", "r") as f:
    x = 0
    for line in f:        
        y = 0
        for c in line:
            #grid[x][y] = c
            if(c == "#"):
                area.add((x,y))
            y += 1
        x += 1

#printArea(area)

for turn in range(100):
    newGen = set([(0,0), (0,areaSize-1), (areaSize-1, 0), (areaSize-1, areaSize-1)])
    candidates = {}
    for c in area:
        neighbors = 0        
        for x in range(3):
            for y in range(3):
                newX = c[0]+x-1
                newY = c[1]+y-1
                newC = (newX,newY)
                if newX < 0 or newY < 0 or newX >= areaSize or newY >= areaSize: continue
                if x == y == 1: continue
                
                if newC in area:
                    neighbors += 1
                else:
                    candidates[newC] = candidates.get(newC, 0)+1
                
        if neighbors > 1 and neighbors < 4:
            newGen.add(c)

    for can in candidates.items():
        if can[1] == 3:
            newGen.add(can[0])
    area = newGen
    #printArea(area)

print (len(area))
