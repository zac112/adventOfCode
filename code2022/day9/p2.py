from collections import deque
from math import sqrt

def distance(p1_x,p1_y, p2_x,p2_y):
    return sqrt((p2_x-p1_x)**2+(p2_y-p1_y)**2)

def getDir(p1_x,p1_y, p2_x,p2_y):
    dx = p2_x-p1_x
    dy = p2_y-p1_y
    try:
        x = dx//abs(dx)
    except:
        x = 0
    try:
        y = dy//abs(dy)
    except:
        y = 0
    return (x, y)

dirs = {'U':(-1,0),
        'D':(1,0),
        'L':(0,-1),
        'R':(0,1)}
with open("data.txt") as f:
    movements = [x.split(" ") for x in f.read().splitlines()]
    movements = [(dirs[d], int(a)) for d,a in movements]

oldRope = []
for i in range(10):
    oldRope.append((0,0))

visited = set()
visited.add((0,0))

for d,amount in movements:    
    for x in range(amount):
        newRope = []
        h = oldRope[0]
        newHead = (h[0]+d[0], h[1]+d[1])
        newRope.append(newHead)
        
        for i,part in enumerate(oldRope[1:],1):
            dist = distance(*newRope[-1],*oldRope[i])
            if dist > 1.5:
                dx,dy = getDir(*part, *newRope[-1])
                newPiece = (part[0]+dx, part[1]+dy)
                newRope.append(newPiece)
            else:
                newRope.append(part)
                
        oldRope = newRope
        visited.add(newRope[-1])

print(len(visited))
