from itertools import product
from collections import deque

class Elf:
    def __init__(self,pos):
        self.pos = pos
        self.left  = []
        self.up    = []
        self.down  = []
        self.right = []
        self.dirs = deque([self.up,self.down,self.left,self.right])

    def checkSurroundings(self):
        x,y = self.pos
        self.surroundings = [(x+a,y+b) for a,b in product([-1,0,1],repeat=2) if not(a==b==0)]
        self.left[:]  = self.surroundings[:3]
        self.up[:]    = [self.surroundings[0],self.surroundings[3],self.surroundings[5]]
        self.down[:]  = [self.surroundings[2],self.surroundings[4],self.surroundings[7]]
        self.right[:] = self.surroundings[-3:]
            
    def propose(self,others, proposals):
        proposal = self.pos
        if all(map(lambda a:a not in others,self.surroundings)):
            proposal = self.pos
        else:
            for dirs in self.dirs:
                if all(map(lambda a:a not in others,dirs)):
                    proposal = [(x,y) for x,y in dirs if x==self.pos[0] or y==self.pos[1]][0]
                    break
            
        self.dirs.rotate(-1)
        self.proposal = proposal
        proposals[proposal] = proposals.get(proposal,0)+1

    def move(self,proposals):
        if self.proposal == self.pos:
            return 0
        if proposals[self.proposal] == 1:
            self.pos = self.proposal            
        return 1

    def __eq__(self, other):
        if isinstance(other,Elf): return self.pos==other.pos
        if isinstance(other,tuple): return self.pos==other
        return False

def boundingBox(elves):
    minx = min([e.pos[0] for e in elves])
    miny = min([e.pos[1] for e in elves])
    maxx = max([e.pos[0] for e in elves])
    maxy = max([e.pos[1] for e in elves])
    return minx,miny,maxx,maxy

def printMap(elves):
    minx,miny,maxx,maxy = boundingBox(elves)
    
    for y in range(miny,maxy+1):
        line = []
        for x in range(minx,maxx+1):
            if (x,y) in elves:
                line.append("#")
            else:
                line.append(".")
        print("".join(line))
    print()

def countSquares(elves):
    minx,miny,maxx,maxy = boundingBox(elves)
    area = (maxx-minx+1)*(maxy-miny+1)
    free = area-len(elves)
    return free

elves = []
with open("data.txt") as f:
    for y,line in enumerate(f):
        for x,c in enumerate(line):
            if c=="#":
                elves.append(Elf((x,y)))

#printMap(elves)
r = 0
while True:
    proposals = {}
    moves = 0
    positions = set([e.pos for e in elves])
    for e in elves:
        e.checkSurroundings()
    for e in elves:
        e.propose(positions,proposals)
    for e in elves:
        moves += e.move(proposals)

    
    r += 1
    #printMap(elves)
    if moves == 0:
        print("Finished at round",r)
        break    

#printMap(elves)
print(countSquares(elves))
