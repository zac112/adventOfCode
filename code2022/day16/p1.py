from collections import deque
from itertools import product,permutations
from functools import cache

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

@cache
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
    
#vertices.sort(key=lambda a:valves[a][0], reverse=True)
vertices.sort()
#vertices.insert(0,"AA")
#trips = zip(vertices,vertices[1:])
print(vertices)
print(valves)
op = None

path = []
#@cache
def paths(remainingValves, currLoc, t):
    #nextLocs = [v for v in valves[currLoc][1] if v in remainingValves]
    #print("aaaaaa",valves[currLoc][1])
    #print("bbbbbb",remainingValves)
    #print(f"r {remainingValves},{t=}")
    path.append((currLoc,30-t))
    if t <= 0:
        def g(x):
            v,t  = x
            return valves[v][0]*(30-t)
        p = map(g,path[:-1])
        p = [p for p in p]
        #print(p, sum(p))
        #print(f"All Valves: {path}, {t}, {sum(p)}")
        return sum(p)
    
        #print(f"Out of time: {path}, {t}")
        #return 0

    if len(remainingValves)==0:
        #print(f"All Valves: {path}, {t}")
        #return sum([f[0] for f in valves.values()])*t
        #return 0
        def g(x):
            v,t  = x
            return valves[v][0]*(30-t)
        p = map(g,path)
        p = [p for p in p]
        #print(p, sum(p))
        print(f"All Valves: {path}, {t}, {sum(p)}")
        return sum(p)
            
        
    s = 0    
    for i,v in enumerate(remainingValves):
        #path.append((v,t-getDist(currLoc,v)-1))
        remaining = tuple(x for x in remainingValves if x != v)        
        #s = max(valves[currLoc][0]*(t-1) + paths(remaining, v, t-getDist(currLoc,v)), s)
        s = max(paths(remaining, v, t-getDist(currLoc,v)), s)
        #path.pop()
        path.pop()
    return s

print(tuple(vertices))
print(paths(tuple(vertices), "AA", 30))
#print(getDist("JJ","HH"))
#print(get_path("AA","HH"))

#print(valves)
time = 29
start = "AA"

#print(getEventualRelease("AA", time))
#open_valves(start,time)

#D2 B5 J9 H17 E21 C24
#print(getDist("EE","CC"))
