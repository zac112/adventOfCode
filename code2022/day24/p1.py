import heapq
from collections import deque

class Blizzard:
    
    def __init__(self,pos,d):
        dirs = {'>':(1,0),
            '<':(-1,0),
            'v':(0,1),
            '^':(0,-1)}
        self.pos = pos
        self.icon = d
        self.d = dirs[d]

    def copy(self):
        return Blizzard(self.pos,self.icon)
    
    def move(self, walls):
        x,y = self.pos
        a,b = self.d
        self.pos = (x+a,y+b)
        
        if self.pos in walls:
            self.pos = walls[self.pos]

    def __eq__(self, other):
        if isinstance(other,Blizzard): return self.pos==other.pos
        if isinstance(other,tuple): return self.pos==other
        return False


def moveBlizzards(blizzards, walls):    
    blizzards = [b.copy() for b in blizzards]
    for b in blizzards:
        b.move(walls)
    return blizzards
    
def printMap(areaSize,blizzards):
    
    screen = [["#"]+['.']*(areaSize[0]-1)+["#"] for i in range(areaSize[1]-1)]
    screen.insert(0,["#"*(areaSize[0]+1)])
    screen.append(["#"*(areaSize[0]+1)])

    for b in blizzards:
        try:
            x,y = b.pos
        except:
            x,y = b
        try:
            screen[y][x] = b.icon
        except:
            print(x,y,len(screen),len(screen[0]))
        
    for line in screen:
        print("".join(line))
    print()

def distance(pos, target):
    x,y = pos
    tx,ty = target
    return abs(x-tx)+abs(y-ty)

def score(pos, steps, target):
    return distance(pos,target)+steps
    
blizzards = []
walls = {}
with open("data.txt") as f:
    for y,line in enumerate(f):
        for x,c in enumerate(line):
            if c in "<>v^":
                blizzards.append(Blizzard((x,y),c))
            areaSize = (x,y)
        target = (len(line)-2,y)

for y in range(areaSize[1]+1):
    walls[(0,y)] = (areaSize[0]-1,y)
    walls[(areaSize[0],y)] = (1,y)

for x in range(areaSize[0]+1):
    walls[(x,0)] = (x,areaSize[1]-1)
    walls[(x,areaSize[1])] = (x,1)

start = (1,0)
del walls[start]
del walls[target]
printMap(areaSize,blizzards)

stack = []
push = lambda pos, step: heapq.heappush(stack,(score(pos,step,target),(pos,step)))
pop = lambda: heapq.heappop(stack)
up = lambda a:(a[0],a[1]-1)
down = lambda a:(a[0],a[1]+1)
left = lambda a:(a[0]-1,a[1])
right = lambda a:(a[0]+1,a[1])

blizzardCache = {}
cycle = (areaSize[0]-1)*(areaSize[1]-1)
print("cycle length:",cycle)
for c in range(cycle+1):
    for b in blizzards:
        b.move(walls)
    blizzardCache[c] = set(b.pos for b in blizzards)

print("Starting simulation")
counter = 0
push((1,0),0)
memoize = set()
while stack:
    priority,(pos, step) = pop()
    if (pos,step) in memoize:
        continue
    memoize.add((pos,step))
    if pos == target:
        print(step+1)
        break
    
    newBlizzards = blizzardCache[(step+1)%cycle]
    positions = [pos, up(pos), down(pos), left(pos), right(pos)]

    for p in positions:
        x,y = p
        if p in walls:
            continue
        elif x<0 or x>areaSize[0] or y < 0 or y > areaSize[1]:
            continue
        elif p not in newBlizzards:
            push(p,step+1)

    if counter%10000==0:
        print(f"{priority},{pos},{step}")
    counter +=1
    
    
print("finished")
