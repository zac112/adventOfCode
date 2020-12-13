from collections import deque

def printPath(area, path):
    areaCopy = [list(row) for row in area]
    i = 46
    for p in path:
        areaCopy[p[0]][p[1]] = chr(i)
        i +=1

    for row in areaCopy:
        print ("".join(row))

def distanceTo(start, end):
    return abs(start[0]-end[0])+abs(start[1]-end[1])

##start and end tuples
##return None if no path found or a list of coordinates ot the path
def findPath(area, start, end, path, visited, unvisited):
    
    unvisited.append( ( (start[0], start[1]-1), distanceTo((start[0], start[1]-1), end) ) ) #up
    unvisited.append( ( (start[0]-1, start[1]), distanceTo((start[0]-1, start[1]), end) ) ) #left
    unvisited.append( ( (start[0]+1, start[1]), distanceTo((start[0]+1, start[1]), end) ) ) #right
    unvisited.append( ( (start[0], start[1]+1), distanceTo((start[0], start[1]+1), end) ) ) #down

    unvisited = list(set(unvisited))
    unvisited.sort(key=lambda a:a[1])
    
    for pos in unvisited:
        current = pos[0]
        if current in visited:
            continue
        
        if current[0] < 0 or current[1] < 0:
            continue
        if current[0] >= len(area) or current[1] >= len(area[current[0]]):
            continue
        
        if area[current[0]][current[1]] == "#":
            continue
        
        if current == end:
            raise Exception()
        
        visited.add(current)
        path.append(current)
        findPath(area, current, end, path, visited, unvisited)

class Pos:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x)+","+str(self.y)

    def getPos(self):
        return (self.x, self.y)
    
cave = []
elves = []
goblins = []
with open("../../data/15t.txt", "r") as f:
    x = 0
    for line in f:
        line = line.replace("\n","")
        row = []
        cave.append(row)
        y = 0
        for c in line:
            if c == "E":
                elves.append(Pos(x,y))
                row.append(".")
            elif c == "G":
                goblins.append(Pos(x,y))
                row.append(".")
            else:
                row.append(c)
            y += 1
        x += 1

path = []
try:    
    print (elves[0], goblins[0])
    findPath(cave,goblins[2].getPos(), elves[0].getPos(),path, set(), [])
except Exception as e:
    print (e,path)
    printPath(cave, path)
