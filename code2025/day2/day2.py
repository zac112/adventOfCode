from itertools import starmap, chain
from math import ceil

with open('data.txt') as f:
    data = f.read().split(",")
    data = map(lambda a:a.split('-'),data)
    data = starmap(lambda a,b: (a,b), data)
    data = list(data)

def invalidIdsInRange(start,end):
    startid = start.rjust(len(end),'0') if len(start)%2==1 and len(end)%2==0 else start
    startid = 0 if len(startid)<=1 else int(startid[:len(startid)//2])
    
    endid = int(end[:ceil(len(end)/2)])
    result = []
    for x in range(startid,endid+1):
        if int(start) <= int(str(x)*2) <= int(end):
            result.append(int(str(x)*2))
    return result
    
invalids = starmap(invalidIdsInRange, data)
invalids = chain.from_iterable(invalids)
print("Part 1:",sum(invalids))

def invalidIdsInRange(start,end):
    result = set()
    for x in range(int(start), int(end)+1):
        x = str(x)
        for i in range(1,len(x)//2+1):            
            curId = x[:i]
            if not any(x.split(curId)):
                result.add(int(x))
    return result

invalids = starmap(invalidIdsInRange, data)
invalids = chain.from_iterable(invalids)
print("Part 2:",sum(invalids))
