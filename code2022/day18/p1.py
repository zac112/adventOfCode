from itertools import product
import sys
sys.setrecursionlimit(100000)
points = set()
with open("data.txt") as f:
    for line in f:
        points.add(tuple(int(x) for x in line.replace("\n","").split(",")))

#print(points)

#neighbors = list(product([-1,0,1], repeat=3))
neighbors = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
print(neighbors)
def floodfill(pointsLeft, curr, visited):
    x,y,z = curr
    sides = 0
    #print("c",curr)
    #print("l",pointsLeft)
    #print("v",visited)
    visited.add(curr)
    for neighbor in ((x+a,y+b,z+c) for a,b,c in neighbors):
        #print("checking ",neighbor)
        if neighbor in pointsLeft:
            pointsLeft.remove(neighbor)
            #visited.add(neighbor)
            sides += floodfill(pointsLeft, neighbor, visited)
        else:
            sides += 0 if neighbor in visited else 1
        #print(sides)
    return sides

print("...",points)
sides = 0
while points:
    start = list(points)[0]
    points.remove(start)
    sides += floodfill(points, start, set())
print(sides)
        
    
