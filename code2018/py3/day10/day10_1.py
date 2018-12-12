from collections import deque

def advance(positions):
    for p in positions:
        p[0][0] += p[1][0]
        p[0][1] += p[1][1]

def goBack(positions):
    for p in positions:
        p[0][0] -= p[1][0]
        p[0][1] -= p[1][1]
        
def countAreas(positions):
    coords = set([ (p[0][0],p[0][1]) for p in positions])    
    areas = 0       

    while len(coords) > 0:
        c = coords.pop()
        coords.add(c)
        areas += 1
        search(coords, c)
        
    return areas

def search(coords, coord):
    try:
        coords.remove(coord)
    except:
        return
    
    search(coords, (coord[0]+1, coord[1]))
    search(coords, (coord[0]-1, coord[1]))
    search(coords, (coord[0], coord[1]+1))
    search(coords, (coord[0], coord[1]-1))

positions = []
with open("../../data/10.txt", "r") as f:
    #position=<15,  0> velocity=<-2,  0>
    for line in f:
        split = line.split("=<")
        split[1] = split[1][:split[1].find(">")]
        split[2] = split[2][:split[1].find(">")-1]

        pos = split[1].split(",")
        vel = split[2].split(",")
        
        positions.append([[int(pos[0].strip()),int(pos[1].strip())],[int(vel[0].strip()), int(vel[1].strip())]])
    


originalArea = countAreas(positions)
smallestAreas = (originalArea,list(positions))
currentArea = originalArea

##wait until we get some action
while countAreas(positions) == originalArea:
    advance(positions)

##Something's happening! Elves never send messages longer than 50 letters... I hear...
while currentArea > 50:
    currentArea = countAreas(positions)
    if currentArea < smallestAreas[0]:
        smallestAreas = (currentArea, list(positions))
    advance(positions)
    
goBack(positions)

print("Final areas: ",countAreas(positions))
print()
positions.sort(key=lambda a: a[0][0])
xMin = positions[0][0][0]
xMax = positions[len(positions)-1][0][0]

positions.sort(key=lambda a: a[0][1])
yMin = positions[0][0][1]
yMax = positions[len(positions)-1][0][1]

message = [[" " for x in range (xMin, xMax+1)] for y in range(yMin, yMax+1)]
coords = set([ (p[0][0],p[0][1]) for p in positions]) 
for y in range(len(message)):
    for x in range(len(message[y])):
        if((x+xMin,y+yMin) in coords):
            message[y][x] = "*"

for x in message:
    print ("".join(x))
