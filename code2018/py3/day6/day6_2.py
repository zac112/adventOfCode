from collections import deque

coords = []
with open("../../data/6.txt","r") as f:
    for line in f :
        coord = line.split(",");
        coords.append((int(coord[0]),int(coord[1])))

#test data
#coords = [(1, 1),(1, 6),(8, 3),(3, 4),(5, 5),(8, 9)]

#reduce the infine coordinates to finite coordinates by calculating bounds
#the coordinate points on the bounds MUST have infinite size
coords.sort(key=lambda a : a[0])
xmin = coords[0][0]
xmax = coords[len(coords)-1][0]
coords.sort(key=lambda a : a[1])
ymin = coords[0][1]
ymax = coords[len(coords)-1][1]
xsize = xmax-xmin
ysize = ymax-ymin

#since safe area is a circle with radius 10000, the center point of our finite bounds must overlap with all circles
coordsToCheck = deque([(xsize/2, ysize/2)])
coordsChecked = set([])
#if center point is not safe, safe area size is 0
safeAreaSize = 1
safeDistance = 10000

while len(coordsToCheck) > 0:    
    c = coordsToCheck.popleft()
    coordsChecked.add(c)

    for x in range(-1,2):
        for y in range(-1,2):
            newX = c[0]+x
            newY = c[1]+y
            if (newX, newY) not in coordsChecked:
                distance = 0
                for otherC in coords:
                    distance += abs(newX-otherC[0])+abs(newY-otherC[1])                
                if distance < safeDistance:
                    if (newX,newY) not in coordsToCheck:
                        coordsToCheck.append((newX,newY))
                        safeAreaSize += 1
                else:
                    coordsChecked.add((newX,newY))

    
print ("Answer:",safeAreaSize)
