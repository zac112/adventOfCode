from collections import deque
from functools import lru_cache

maxpressure = [0]
def getPath(start, target):
    visited = {}
    stack = deque()
    stack.append((start,None))
    while stack:
        loc,prev = stack.popleft()        
        visited[loc] = prev
        if loc == target:
            break
        nextLocs = [(v,loc) for v in valves[loc][1] if v not in visited]
        stack.extend(nextLocs)

    path = [target]
    while path[-1] is not None:
        path.append(visited[path[-1]])
    return path[-2::-1]

@lru_cache(maxsize=10000000)
def getDist(source,target):
    return len(getPath(source, target))
    
valves = {}
vertices = []
with open("data.txt") as f:
    for line in f.read().splitlines():
        line = line.split(" ")
        valve, flow_rate, others = line[1], int(line[4].split("=")[1][:-1]), "".join(line[9:])
        others = others.split(",")
        valves[valve] = [int(flow_rate),others]
        if flow_rate > 0:
            vertices.append(valve)

vertices.sort(key=lambda a:valves[a][0], reverse=True)
MAXTIME = 26

@lru_cache(maxsize=20_000_000)
def paths(remainingValves, currLoc_h, t_h, currLoc_e, t_e):    
    if max(t_h,t_e) > MAXTIME or len(remainingValves)==0:
        return 0
    
    s = 0    
    for i,v in enumerate(remainingValves):
        humanTurn = t_h < t_e
        remaining = tuple(x for x in remainingValves if x != v)   

        if humanTurn:
            nt = t_h+getDist(currLoc_h,v)
            s = max(valves[v][0]*max(MAXTIME-nt,0) +
                    paths(remaining,
                          v, nt,
                          currLoc_e, t_e), s)            
        else:
            nt = t_e+getDist(currLoc_e,v)
            s = max(valves[v][0]*max(MAXTIME-nt,0) +
                    paths(remaining,
                          currLoc_h, t_h,
                          v, nt), s)
    return s

print(paths(tuple(vertices), "AA", 0, "AA", 0))
