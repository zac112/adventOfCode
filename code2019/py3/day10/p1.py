from math import atan, degrees

space = set()

with open("../../day10.txt","r") as f:
    spaceMap = [list(x[:-1]) for x in f.readlines()]    
    for y in range(len(spaceMap)):
        print (str(y)+" "+"".join(spaceMap[y]))
        for x in range(len(spaceMap[y])):
            if spaceMap[y][x] == "#":
                space.add((x,y))
                #print ((x,y))

print (space)

def calculateAngle(fromAsteroid, toAsteroid):
    dx, dy = toAsteroid[0]-fromAsteroid[0], toAsteroid[1]-fromAsteroid[1]
    if dx == 0:
        return 90 if dy>=0 else 270
    if dy == 0:
        return 180 if dx>=0 else  0
    
    baseAngle = 90
    if dy > 0:
        baseAngle += 180

    angle = degrees(atan(dy/dx))    
    result = angle+baseAngle
    return result
    
def findVisibleAsteroids(asteroid, space):
    angles = {}
    for a in space:
        if a == asteroid:
            continue
        angles.setdefault(calculateAngle(asteroid,a), []).append(a)
    #print (angles)
    #angles.sort(key: lambda x: math.sqrt((x[0]-a[0])**2 + (x[1]-a[1])**2) )
    return len(angles)
    

print(sorted([(findVisibleAsteroids(asteroid,space),asteroid) for asteroid in space], reverse=True, key= lambda a: a[0])[0])
    
