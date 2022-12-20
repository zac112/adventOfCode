import re
from functools import lru_cache
import heapq

blueprints = {}
with open("data.txt") as f:
    for line in f:
        print(re.findall("(\d+)", line))
        bp, *ores = map(int,re.findall("(\d+)", line))        
        blueprints[bp] = [
            [ores[0],0,0,0],
            [ores[1],0,0,0],
            [ores[2],ores[3],0,0],
            [ores[4],0,ores[5],0]
            ]

def score(ores, bots, timeleft):
    primes = [1,10,100,1000]
    return sum(a*b for a,b in zip(primes,bots))
               
def canbuild(reqs, ores):
    return all(map(lambda a: a[0]>=a[1], zip(ores,reqs)))

times = {}
def get_geodes(reqs,timeLeft, ores, bots):
    
    ores = [0,0,0,0]
    bots = [1,0,0,0]

    heap = []
    heappush = lambda item:heapq.heappush(heap,item)
    heappop = lambda: heapq.heappop(heap)
    pushstate = lambda a,b,c,d:heapq.heappush(heap,(-score(a,b,c),(a,b,c,d)))
    
    pushstate(ores,bots,timeLeft, [0])
    besthist = [0]*(timeLeft+1)
    geodes = 0
    memoize = set()
    while heap:
        
        state = heappop()        
        ores,bots,time, hist = state[1]
        s = tuple(ores+bots+[time])

        #Some heuristics
        if state[0]-10 > besthist[MAXTIME-time]:
            continue
        if s in memoize:
            continue
        memoize.add(s)
            
        if len(memoize)%1000000 == 0:
            print(f"{len(heap)},{len(memoize)}, {geodes}")
            
        
        if time == 0:            
            oldg = geodes
            geodes = max(geodes, ores[-1])
            if geodes > oldg:
                besthist = hist
                print("new geodes",geodes, hist)
            continue

        newores =[o+b for o,b in zip(ores,bots)]
        pushstate(newores,bots,time-1, hist+[state[0]])
        
        for i, b in enumerate(bots):
            if canbuild(reqs[i], ores):
                newores = [o-r+b for o,r,b in zip(ores,reqs[i],bots)]
                newbots = list(bots)
                newbots[i] += 1
                pushstate(newores,newbots,time-1, hist+[state[0]])
    return geodes

        
MAXTIME = 32
quality = 1
for bp, ores in blueprints.items():
    if bp == 4:break
    print("Blueprint",bp, ores)
    geodes = get_geodes(ores, MAXTIME, (0,0,0,0), (1,0,0,0))
    quality *= geodes
    
print(quality)
