from collections import deque
data =\
"""...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()

with open('data.txt') as f:
    #data = f.read().splitlines()
    pass

coords = set()
for y,line in enumerate(data):
    for x,c in enumerate(line):
        if c=="S": 
            start = (x,y,0)            
            coords.add((x,y))
        if c==".": coords.add((x,y))

stepped = set()
visited = set()
visited.add(start)
steppedCache = set()

#for step in range(26501365):
for step in range(5001):
    newVisited = set()
    if step%100==0:
        print(step)
        print(len(stepped))
    #while visited:
    mindist = 10**10
    maxdist = 0
    for x,y,d in visited:        
        dist = abs(start[0]-x)+abs(start[1]-y)
        if dist < step-2:continue
        #mindist = min(mindist, dist)
        #maxdist = max(maxdist, dist)
        stepped.add((x,y, step%2, dist))
        neighbors = [(x+dx,y+dy, dist) 
                     for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]
                     if ((x+dx)%len(data[0]),(y+dy)%len(data)) in coords
                     and(x+dx,y+dy, (step+1)%2) not in stepped]
        newVisited.update(neighbors)
    #print(mindist, maxdist)
    visited = newVisited

    #print(visited)

#print(stepped)
print(len([x for x,y,s,d in stepped if s==(step)%2]))