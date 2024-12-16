import heapq
heap = []
heappush = lambda score, entry, coord, direction: heapq.heappush(heap,(score,entry,coord, direction))
heappop = lambda : heapq.heappop(heap)

with open("data.txt") as f:
    path = set()
    for y,line in enumerate(f.readlines()):
         for x,c in enumerate(line):
            if c in "SE.": path.add((x,y))
            if c == "S": start = (x,y)
            if c == "E": end = (x,y)
    
dirs = [(1,0),
        (0,1),
        (-1,0),
        (0,-1)]  
tuplesum = lambda a,b: (a[0]+b[0],a[1]+b[1])
tuplesub = lambda a,b: (a[0]-b[0],a[1]-b[1])
getDir = lambda d:dirs[d]

heappush(0, 0, start, 0)
steps = {}
PART1ANS = 0
entry = 0
while heap:
    score, _, coord, direction = heappop()
    if coord not in path:continue
    if coord in steps: continue
    
    steps[coord] = tuplesub(coord,dirs[direction])
    if coord == end:
        print("Found path with score",score)
        PART1ANS = score
        break

    heappush(score+1,    entry+1, tuplesum(coord,dirs[direction]), direction)
    heappush(score+1001, entry+2, tuplesum(coord,dirs[(direction+1)%4]), (direction+1)%4)
    heappush(score+1001, entry+3, tuplesum(coord,dirs[(direction+3)%4]), (direction+3)%4)
    entry += 3
        

#P2
heap.clear()
steps = {}
heappush(0, 0, start, 0)
while heap:
    score, _, coord, direction = heappop()
    if coord not in path:continue
    if coord in steps:
        steps.setdefault(coord,[]).append((tuplesub(coord,dirs[direction]),score))
        continue
    if score > PART1ANS+100: continue 

    steps.setdefault(coord,[]).append((tuplesub(coord,dirs[direction]),score))

    heappush(score+1,    entry+1, tuplesum(coord,dirs[direction]), direction)
    heappush(score+1001, entry+2, tuplesum(coord,dirs[(direction+1)%4]), (direction+1)%4)
    heappush(score+1001, entry+3, tuplesum(coord,dirs[(direction+3)%4]), (direction+3)%4)
    entry += 3
    
commonSteps = set()
def collect(oldNode, oldScore):
    node = steps.get(oldNode,[])
    for c in node:
        node,score = c
        if score <= oldScore:
            commonSteps.add(node)
            collect(node,score)
    
collect(end,min(steps[end],key=lambda a:a[1])[1])
print("Common steps:",len(commonSteps))
