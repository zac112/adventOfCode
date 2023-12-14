def printMap(rocks, balls):
    items = rocks|balls
    for y in range(max(items,key=lambda a:a[1])[1]):
        for x in range(max(items,key=lambda a:a[0])[0]):
            if (x,y) in rocks: print("#",end="")
            elif (x,y) in balls: print("O",end="")
            else: print(".",end="")
        print()

def tilt(rocks, balls, tiltDir):
    blocked = set(rocks)
    keyfunc = lambda a:a[(tiltDir+1)%2]
    dir = [(0,-1),(-1,0),(0,1),(1,0)][tiltDir]
    rev = tiltDir in [2,3]
    
    for ballX, ballY in sorted(balls,key=keyfunc, reverse=rev):
        while not (ballX,ballY) in blocked:
            ballX,ballY = ballX+dir[0], ballY+dir[1]
        ballX,ballY = ballX-dir[0], ballY-dir[1]
        blocked.add((ballX,ballY))

    return blocked.difference(rocks)

def cycle(rocks, balls):
    for i in range(4):
        balls = tilt(rocks, balls,i)
    return balls

with open('data.txt') as f:
    data = f.read().splitlines()

balls = set()
rocks = set((x,-1) for x in range(len(data[0])))
rocks.update((x,len(data[0])) for x in range(len(data[0])))
rocks.update((-1,y) for y in range(len(data)))
rocks.update((len(data),y) for y in range(len(data)))

for y, line in enumerate(data):
    for x,c in enumerate(line):
        if c == 'O': balls.add((x,y))
        if c == '#': rocks.add((x,y))

i  = 0
cycles = 0    
cache = set()
cycleLengths = []
while i < 2:
    balls = cycle(rocks,balls)
    if tuple(balls) in cache:
        cycleLengths.append(cycles)
        cycles = 0
        cache = set()
        i += 1

    cache.add(tuple(balls))
    cycles += 1

print(cycleLengths)
remainingCycles = (10**9-cycleLengths[0])%cycleLengths[1] - 1
for i in range(remainingCycles):
    balls = cycle(rocks,balls)

computeLoad = lambda a,b: sum(len(a)-y for x,y in b)
print("Final load:",computeLoad(data,balls))