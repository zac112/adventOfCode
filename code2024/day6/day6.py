
class Guard:
    def __init__(self, pos):
        self.pos = tuple(pos)
        self.startpos = pos
        self.dirs = [(0,-1),(1,0),(0,1),(-1,0)]
        self.dir = 0

    def reset(self):
        self.pos = self.startpos
        self.dir = 0
        
    def setarea(self, area):
        self.area = area
    
    def move(self, lab):
        #tuplesum = lambda a,b:tuple((x+y) for x,y in zip(a,b))
        tuplesum = lambda a,b:(a[0]+b[0],a[1]+b[1])
        for _ in range(4):
            forward = tuplesum(self.pos, self.dirs[self.dir])
            self.dir = ( self.dir + (1 if (forward in lab) else 0))%4
        
        self.pos = tuplesum(self.pos, self.dirs[self.dir])
        if not (0<=self.pos[0]<=self.area[0]) or not (0<=self.pos[1]<=self.area[1]):
            return False
        return True

with open('data.txt') as f:
    lab = set()
    for y,line in enumerate(f.readlines()):
        for x,char in enumerate(line):
            if char=="#": lab.add((int(x),int(y)))
            if char=="^": guard = Guard((int(x),int(y)))
    guard.setarea((int(x),int(y)))

steps = set()
while True:    
    if not guard.move(lab): break
    steps.add(guard.pos)
    
print("Steps:",len(steps))

#Part2
oldsteps = steps
oldsteps.remove(guard.startpos)
obstacles = set()

for newObstacle in oldsteps:
    guard.reset()    
    lab.add(newObstacle)
    steps = set()
    
    while True:
        steps.add((guard.pos,guard.dir))
        if not guard.move(lab): break
        if (guard.pos,guard.dir) not in steps: continue

        obstacles.add(newObstacle)
        break
    lab.remove(newObstacle)
        
print("Obstacles:",len(obstacles))
