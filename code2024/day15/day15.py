from itertools import repeat

with open("data.txt") as f:
    data = f.readlines()
    i = data.index('\n')
    areamap, movement = data[:i],data[i+1:]
    movement = "".join(movement).replace("\n","")

    walls = set()
    boxes = set()
    for y, line in enumerate(areamap):
        for x, c in enumerate(line):
            if c == "#": walls.add((x,y))
            if c == "@": start = (x,y)
            if c == "O": boxes.add((x,y))

def getDirection(movement, times=None):
    directions = {'<':(-1,0),
                  'v':(0,1),
                  '>':(1,0),
                  '^':(0,-1)}
    
    for movements in repeat(movement, times):
        for d in movements:
            yield directions[d]

def pushBox(pos, dir):
    original = pos
    while pos in boxes:
        pos = tuplesum(pos,dir)
        if pos in walls: return False

    boxes.remove(original)
    boxes.add(pos)
    return True

tuplesum = lambda a,b:(a[0]+b[0],a[1]+b[1])

def draw():
    lengths = (max(map(lambda a:a[1],walls)), max(map(lambda a:a[0],walls)))
    area = [[" " for x in range(lengths[0]+1)] for y in range(lengths[1]+1)]
    for y,x in boxes:
        area[x][y] = "O"
    for y,x in walls:
        area[x][y] = "#"
    area[pos[1]][pos[0]] = "@"

    [print("".join(line)) for line in area]
pos = start
for d in getDirection(movement,1):
    #draw()
    #input()    
    newPos = tuplesum(pos,d)
    if newPos in walls: continue
    elif newPos in boxes: 
        if pushBox(newPos,d):
            pos = newPos
    else: pos = newPos

GPSscore = sum(map(lambda a:a[0]+100*a[1],boxes))
print("Part1:",GPSscore)
#P2
class Box():

    def __init__(self,pos):
        self.posLeft = pos[0]
        self.posRight = pos[1]

    def canPush(self,dir):
        success = True
        try:
            newPos = tuplesum(self.posLeft,dir)
            if newPos in walls: return False
            pushedBoxL = [b for b in [a for a in boxes if a != self] if newPos==b.posLeft or newPos==b.posRight][0]
            success &= pushedBoxL.canPush(dir)
        except:
            pass
        
        try:
            newPos = tuplesum(self.posRight,dir)
            if newPos in walls: return False
            pushedBoxR = [b for b in [a for a in boxes if a != self] if newPos==b.posLeft or newPos==b.posRight][0]
            success &= pushedBoxR.canPush(dir)
        except:
            pass
        
        return success
    
    def pushBox(self, dir):
        
        success = True
        pushedBoxL = None
        pushedBoxR = None
        try:
            newPos = tuplesum(self.posLeft,dir)
            if newPos in walls: return False
            pushedBoxL = [b for b in [a for a in boxes if a != self] if newPos==b.posLeft or newPos==b.posRight][0]
            success &= pushedBoxL.canPush(dir)
        except:
            pass
        
        try:
            newPos = tuplesum(self.posRight,dir)
            if newPos in walls: return False
            pushedBoxR = [b for b in [a for a in boxes if a != self] if newPos==b.posLeft or newPos==b.posRight][0]
            success &= pushedBoxR.canPush(dir)
        except:
            pass
        

        if success:
            self.posLeft = tuplesum(self.posLeft,dir)
            self.posRight = tuplesum(self.posRight,dir)
            if pushedBoxL == pushedBoxR and pushedBoxL is not None:
                pushedBoxL.pushBox(dir)
            else:
                if pushedBoxL: pushedBoxL.pushBox(dir)
                if pushedBoxR: pushedBoxR.pushBox(dir)
        return success

with open("data.txt") as f:
    data = f.readlines()
    i = data.index('\n')
    areamap, movement = data[:i],data[i+1:]
    movement = "".join(movement).replace("\n","")

    walls = set()
    boxes = set()
    for y, line in enumerate(areamap):
        s = []
        for p in zip(line,line):
            
            s.extend(p)
        line = "".join(s)
        
        for x, c in enumerate(zip(line,line[1:])):
            if c == ("#","#"): walls.update([(x,y),(x+1,y)])
            if c == ("@","@"): start = (x,y)
            if c == ("O","O"): 
                for b in boxes:
                    if b.posLeft == (x,y) or b.posRight == (x,y):break
                else:
                    boxes.add(Box(((x,y),(x+1,y))))

def getBox(newPos, boxes):
    b = [b for b in boxes if newPos==b.posLeft or newPos==b.posRight]
    if len(b) == 0: return None
    return b[0]
 
def draw():
    lengths = (max(map(lambda a:a[0],walls)), max(map(lambda a:a[1],walls)))
    area = [[" " for x in range(lengths[0]+1)] for y in range(lengths[1]+1)]
    for b in boxes:
        left, right = b.posLeft,b.posRight
        x,y = left
        area[y][x] = "["
        x,y = right
        area[y][x] = "]"
    for y,x in walls:
        area[x][y] = "#"
    area[pos[1]][pos[0]] = "@"

    [print("".join(line)) for line in area]

pos = start
for d in getDirection(movement,1):
    #draw()
    #input()    
    newPos = tuplesum(pos,d)
    if newPos in walls: continue
    elif (box := getBox(newPos, boxes)): 
        if box.pushBox(d):
            pos = newPos
    else: pos = newPos

draw()
GPSscore = sum(map(lambda a:a.posLeft[0]+100*a.posLeft[1],boxes))
print("Part2",GPSscore)