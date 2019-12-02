from PIL import Image

def advance(positions):
    for p in positions:
        p[0][0] += p[1][0]
        p[0][1] += p[1][1]

def goBack(positions):
    for p in positions:
        p[0][0] -= p[1][0]
        p[0][1] -= p[1][1]
        
#[ [[x,y], [vX, vY]] ]
positions = []
with open("../../data/10.txt", "r") as f:
    for line in f:
        #position=< 9,  1> velocity=< 0,  2>
        split = line[10:].split("> velocity=<")
        split[1] = split[1][:-2]
        
        posX = int(split[0].split(",")[0])
        posY = int(split[0].split(",")[1])

        velX = int(split[1].split(",")[0])
        velY = int(split[1].split(",")[1])
        positions.append([ [posX,posY], [velX,velY]])
        
#print positions

positions.sort(key = lambda a : a[0][0])

minX = positions[0][0][0]
maxX = positions[len(positions)-1][0][0]

positions.sort(key = lambda a : a[0][1])

minY = positions[0][0][1]
maxY= positions[len(positions)-1][0][1]

curArea = (maxX-minX)*(maxY-minY)
prevArea = 0

while curArea > prevArea:
    
#print "area:", (maxX-minX)*(maxY-minY)
    prevArea = curArea
    advance(positions)

    positions.sort(key = lambda a : a[0][0])

    minX = positions[0][0][0]
    maxX = positions[len(positions)-1][0][0]

    positions.sort(key = lambda a : a[0][1])

    minY = positions[0][0][1]
    maxY= positions[len(positions)-1][0][1]
    
    prevArea = (maxX-minX)*(maxY-minY)

goBack(positions)

prevArea = curArea

positions.sort(key = lambda a : a[0][0])

minX = positions[0][0][0]
maxX = positions[len(positions)-1][0][0]

positions.sort(key = lambda a : a[0][1])

minY = positions[0][0][1]
maxY= positions[len(positions)-1][0][1]
    
prevArea = (maxX-minX)*(maxY-minY)

print "prevarea:", prevArea
print minX, minY, maxX, maxY

with open("output.txt", "w") as f:
    for y in range(maxY, minY-1, -1):            
        xPos = [p[0][0] for p in positions if p[0][1]==y]
        xPos.sort()        
        for x in range(minX, maxX+1):        
            if x-minX in xPos:
                f.write("*")
            else:
                f.write(" ")
        f.write("\r\n")
    f.flush()
