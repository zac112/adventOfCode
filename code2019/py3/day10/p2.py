from math import atan, degrees, sqrt

space = set()

with open("../../day10.txt","r") as f:
    spaceMap = [list(x[:-1]) for x in f.readlines()]
    for y in range(len(spaceMap)):
        print (str(y)+" "+"".join(spaceMap[y]))
        for x in range(len(spaceMap[y])):
            if spaceMap[y][x] == "#":
                space.add((x,y))

def calculateAngle(fromAsteroid, toAsteroid):
    dx, dy = toAsteroid[0]-fromAsteroid[0], toAsteroid[1]-fromAsteroid[1]
    if dx == 0:
        return 90 if dy<=0 else 270
    if dy == 0:
        return 180 if dx<=0 else  0
    
    baseAngle = 360
    if dx > 0:
        baseAngle += 180

    angle = degrees(atan(dy/dx))    
    result = (angle+baseAngle)%360
    return result
    
def findVisibleAsteroids(asteroid, space):
    angles = {}
    for a in space:
        if a == asteroid:
            continue
        angles.setdefault(calculateAngle(asteroid,a), []).append(a)
    return angles
    
def getTarget(targets):    
    i = targets.index(90)
    while True:
        yield targets[i%len(targets)]
        i -= 1
        
station = sorted([(len(findVisibleAsteroids(asteroid,space)),asteroid) for asteroid in space], reverse=True, key= lambda a: a[0])[0][1]
print(station)

visibleAsteroids = findVisibleAsteroids(station,space)
for key, val in visibleAsteroids.items():
    val.sort(key= lambda a: sqrt( (station[0]-a[0])**2 + (station[1]-a[1])**2) )

orderOfHits = sorted([x for x in visibleAsteroids.keys()], reverse=True)

destroyedAsteroids = 0
targets = getTarget(orderOfHits)
while destroyedAsteroids < 200:    
    nextAsteroids = visibleAsteroids[next(targets)]
    while len(nextAsteroids) == 0:
        nextAsteroids = visibleAsteroids[next(targets)]
        
    destroyedAsteroids += 1
    print("Destroyed asteroid ",(destroyedAsteroids),":",nextAsteroids.pop(0))
        
