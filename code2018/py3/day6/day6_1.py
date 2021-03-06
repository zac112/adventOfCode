coords = []
with open("../../data/6.txt","r") as f:
    for line in f :
        coord = line.split(",");
        coords.append((int(coord[0]),int(coord[1])))

#coords = [(1, 1),(1, 6),(8, 3),(3, 4),(5, 5),(8, 9)]

def printArea(area):
    for x in range(len(area)):
        print (area[x])
        
def fillArea(pos, area, name):    
    #optimize if I ever have time: make a flood fill
    for x in range(len(area)):
        for y in range(len(area[x])):
            area[x][y].append( (name, abs(x-pos[0])+abs(y-pos[1]) ) )

def sortAndMarkArea(area):
    for x in range(len(area)):
        for y in range(len(area[x])):
            area[x][y].sort(key=lambda a : a[1])
            if(len(area[x][y])>1 and area[x][y][0][1] == area[x][y][1][1]):
                area[x][y][0] = (-1,0)
    print ("sorted!")

def findInfinites(area):
    result = set([])
    for x in range(len(area)):
        result.add(area[x][0][0][0])
        result.add(area[x][len(area[x])-1][0][0])
        for y in range(len(area[x])):
            result.add(area[0][y][0][0])
            result.add(area[len(area)-1][y][0][0])
    print ("infinites:", result)
    return result

def findLargestArea(area, infiniteAreas):
    areas = {}
    for x in range(len(area)):
        for y in range(len(area[x])):
            cell = area[x][y]
            #cell: list of tuples: (name, distance)
            if cell[0][0] in infiniteAreas:
                continue
            if cell[0][0] not in areas:
                areas[cell[0][0]] = 1
            else:
                areas[cell[0][0]] += 1

    #id, distance
    maxArea = (0,0)
    for x in areas:
        if areas[x] > maxArea[1]:
            maxArea = (x, areas[x])
    return maxArea

#reduce the infine coordinates to finite coordinates by calculating bounds
#the coordinate points on the bounds MUST have infinite size
coords.sort(key=lambda a : a[0])
xmin = coords[0][0]
xmax = coords[len(coords)-1][0]
coords.sort(key=lambda a : a[1])
ymin = coords[0][1]
ymax = coords[len(coords)-1][1]
xsize = xmax-xmin+1
ysize = ymax-ymin+1

modCoords = [(x[0]-xmin, x[1]-ymin) for x in coords]

#area is [x:int][y:list of closest points as tuple->name, minDistance]

area = [ [[] for y in range(ysize+1)] for x in range(xsize+1)]

for i in range(len(modCoords)):
    fillArea(modCoords[i], area, i)

print ("filled!")
#printArea(area)
sortAndMarkArea(area)
#printArea(area)
infiniteAreas = findInfinites(area)
largest =(findLargestArea(area, infiniteAreas))
print("Largest area:",largest[1],"for coordinate",coords[largest[0]])
