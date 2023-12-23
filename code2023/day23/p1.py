import sys
sys. setrecursionlimit(10**5) 
with open("data.txt") as f:
    data = f.read().splitlines()

start = (1,0,[])
end = (len(data)-2,len(data)-1)
coords = {(x,y):c for y, line in enumerate(data) for x,c in enumerate(line) if c in ".<>v^"}
blocks = {'<':(-1,0),'>':(1,0),'v':(0,1),'^':(0,-1)}

queue = deque()
queue.append(start)
nodesVisited = []
visited = {}
i = 0
while queue:
    x,y,nodesVisited = queue.popleft()
    if (x,y)in nodesVisited:
        continue
    
    if (x,y)==end:
        print(len(nodesVisited))
        continue
    neighbors = [(x+dx,y+dy) for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)] if (x+dx,y+dy) in coords and (x+dx,y+dy) not in visited]
    for x1,y1 in neighbors:
        dx,dy = x1-x,y1-y
        if coords.get((x1,y1),"") in blocks:
            block = coords.get((x1,y1),"")
            if blocks.get(block) != (dx,dy):
                continue
            
        nv = list(nodesVisited)
        nv.append((x,y))
        queue.append((x1,y1,nv))
    i += 1
    
