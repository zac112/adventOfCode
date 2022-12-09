from collections import deque
from math import sqrt

def distance(p1_x,p1_y, p2_x,p2_y):
    return sqrt((p2_x-p1_x)**2+(p2_y-p1_y)**2)
    
dirs = {'U':(-1,0),
        'D':(1,0),
        'L':(0,-1),
        'R':(0,1)}
with open("data.txt") as f:
    movements = [x.split(" ") for x in f.read().splitlines()]
    movements = [(dirs[d], int(a)) for d,a in movements]

buffer = deque(maxlen=2)
buffer.append((0,0))
buffer.append((0,0))

visited = set()
visited.add((0,0))

for d,amount in movements:
    for x in range(amount):
        h = buffer[-1]
        newHead = (h[0]+d[0], h[1]+d[1])
        dist = distance(*buffer[0],*newHead)
        if dist > 1.5:
            buffer.append(newHead)
        else:
            buffer[-1] = newHead
        visited.add(buffer[0])

print(len(visited))
