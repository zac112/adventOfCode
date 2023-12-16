from collections import deque

class Beam:
    def __init__(self,x,y,D, maxX, maxY,energizedTiles) -> None:
        self.x = x
        self.y = y
        self.direction = D
        self.maxX = maxX
        self.maxY = maxY
        self.energized = energizedTiles

    def move(self, tiles):
        newBeam = lambda x,y,D: Beam(x,y,D,width,height,self.energized)
        dx, dy = dirs[self.direction]
        self.x += dx
        self.y += dy

        if not(0 <= self.x < self.maxX) or not(0 <= self.y < self.maxY):
            return []
        
        if (self.x,self.y,self.direction) in self.energized:
            return []
        self.energized.add((self.x,self.y,self.direction))
        
        tile = tiles.get((self.x,self.y),None)
        if not tile: return [self]

        match (self.direction, tile):
            case ((0|2),"-") : return [
                newBeam(self.x, self.y,1),
                newBeam(self.x, self.y,3)
                ]
            case ((1|3),"|"): return [
                newBeam(self.x, self.y,0),
                newBeam(self.x, self.y,2)
                ]
            case (_,('-'|'|')): return [self]
            #case (D,"\\"): return [newBeam(self.x, self.y,(D+3)%4)]
            case (0,"\\"): return [newBeam(self.x, self.y,1)]
            case (1,"\\"): return [newBeam(self.x, self.y,0)]
            case (2,"\\"): return [newBeam(self.x, self.y,3)]
            case (3,"\\"): return [newBeam(self.x, self.y,2)]
            case (0,"/"): return [newBeam(self.x, self.y,3)]
            case (1,"/"): return [newBeam(self.x, self.y,2)]
            case (2,"/"): return [newBeam(self.x, self.y,1)]
            case (3,"/"): return [newBeam(self.x, self.y,0)]
            case _: return []

def printBeams(energized):
    for y in range(height+2):
        for x in range(width+2):
            if (x,y) in ((x,y) for x,y,d in energized):print("#",end="")
            elif (x,y) in coords: print(coords[(x,y)],end="")
            else:print(" ",end="")
        print()
    print(len(energized))

with open('data.txt') as f:
    data = f.read().splitlines()
    height, width = len(data), len(data[0])
    coords = {(x,y):c
              for y, line in enumerate(data)
              for x,c in enumerate(line) if c !="."}
   
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
maxEnergized = 0
def sendBeam(start):
    energized = set()
    newBeam = lambda x,y,D: Beam(x,y,D,width,height,energized)
    beams = deque([newBeam(*start)])

    while beams:
        beam = beams.pop()
        beams.extend(beam.move(coords))

    return len(set((x,y) for x,y,d in energized))


start = (-1,0,1)
print("Part 1 energized:",sendBeam(start))

for y in range(len(data)):
    start = (len(data[0]),y,3)
    maxEnergized = max(maxEnergized, sendBeam(start))
    start = (-1,y,3)
    maxEnergized = max(maxEnergized, sendBeam(start))

for x in range(len(data[0])):    
    start = (x,-1,0)
    maxEnergized = max(maxEnergized, sendBeam(start))
    start = (x,len(data),2)
    maxEnergized = max(maxEnergized, sendBeam(start))
    
print("Part 2 energized:",maxEnergized)

