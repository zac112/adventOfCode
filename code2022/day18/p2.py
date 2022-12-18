from itertools import product
from collections import deque

points = set()
with open("data.txt") as f:
    for line in f:
        points.add(tuple(int(x) for x in line.replace("\n","").split(",")))

#print(points)

#neighbors = list(product([-1,0,1], repeat=3))
neighbors = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
print(neighbors)
def floodfill(pointsLeft, curr, visited):
    visited = set()
    stack = deque()
    stack.append(curr)
    sides = 0
    while stack:
        curr = stack.popleft()        
        x,y,z = curr
        if curr in visited: continue
        #print(curr)
        visited.add(curr)
        for neighbor in ((x+a,y+b,z+c) for a,b,c in neighbors):
            a,b,c = neighbor
            #print("checking ",neighbor)
            if a > maxCoord or b > maxCoord or c > maxCoord:continue
            if a < minCoord or b < minCoord or c < minCoord:continue        
            if neighbor in pointsLeft:
                sides += 1            
            else:
                if neighbor in visited: continue
                
                stack.append(neighbor)
        #print(sides)    
    return sides

##def floodfill(pointsLeft, curr, visited):
##    x,y,z = curr
##    sides = 0
##    #print("c",curr)
##    #print("l",pointsLeft)
##    #print("v",visited)
##    visited.add(curr)
##    for neighbor in ((x+a,y+b,z+c) for a,b,c in neighbors):
##        a,b,c = neighbor
##        #print("checking ",neighbor)
##        if a > maxCoord or b > maxCoord or c > maxCoord:continue
##        if a < minCoord or b < minCoord or c < minCoord:continue        
##        if neighbor in pointsLeft:
##            sides += 1            
##        else:
##            if neighbor in visited: continue
##            sides += floodfill(pointsLeft, neighbor, visited)
##        #print(sides)
##    return sides

minCoord = min([min([x for x,y,z in points])
            ,min([y for x,y,z in points])
            ,min([z for x,y,z in points])])-1

maxCoord = max([max([x for x,y,z in points])
            ,max([y for x,y,z in points])
            ,max([z for x,y,z in points])])+1


print(minCoord, maxCoord)
print("...",points)
sides = floodfill(points, (minCoord,minCoord,minCoord), set())
print(sides)
        
    
