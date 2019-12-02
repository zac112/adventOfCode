
depth = 5616
target = (10,785)
#depth = 510
#target = (10,10)

def type(cave, x, y):
    return erosion(cave,x,y)%3

def erosion(cave, x, y):
    return (cave_g[x][y]+depth)%20183

def printCave(cave_g):
    cave = ""
    for x in range(target[1]+1):
        line = ""
        for y in range(target[0]+1):
            if(x == 0 and y == 0):
                line += "S"
                continue
            if(y == 10 and x == 785):
                line += "T"
                continue
            risk = erosion(cave_g,y,x)%3
            if risk == 0:
                line += "."
            if risk == 1:
                line += "="
            if risk == 2:
                line += "|"
        cave += line+"\n"
    print (cave)
cave_g = [[ 0 for y in range(target[1]+1)] for x in range(target[0]+1)]

print ( cave_g)

for x in range(target[0]+1):
    for y in range(target[1]+1):
        if(x == 0 and y == 0):
            cave_g[x][y] = 0
            continue
        if(x == target[0] and y == target[1]):
            cave_g[x][y] = 0
            continue
        if(y == 0):
            cave_g[x][y] = x*16807
            continue
        if(x == 0):
            cave_g[x][y] = y*48271
            continue
        
        cave_g[x][y] = erosion(cave_g,x-1,y)*erosion(cave_g,x,y-1)

print (cave_g[target[0]][target[1]])

risk = 0
for x in cave_g:
    risk += sum([(c+depth)%20183%3 for c in x])

printCave( cave_g)
print (cave_g[0][0])
print (cave_g[target[0]][target[1]])
print (risk)            

#8606 low, 8781 high
