#Running this takes a while; the answer was 219529182
def parseData(data):
    data.append("")
    maps = []
    seeds = list(map(int, data[0].replace("seeds: ","").split(" ")))
    for line in data[2:]:

        if line=="":
            maps.append(lookups)
            lookups = []
            continue
        if 'map' in line:
            lookups = []
            continue
        lookups.append(list(map(int,line.split(" "))))
    
    seedranges = []
    for start, length in zip(seeds[::2],seeds[1::2]):
        seedranges.append([start,start+length])

    def checkIsSeed(val):
        for start,end in seedranges:
            if start<=val<end:
                return True
        return False
    
    return checkIsSeed, maps

maps = {}
with open("data.txt") as f:
    isSeed, mapping = parseData(f.read().split("\n"))

val = 0
startval = 0
while True:
    startval = val
    for M in mapping[::-1]:
        for m in M:
            if m[0] <= val < m[0]+m[2]:
                val += (m[1]-m[0])
                break
    if isSeed(val):
        print("found seed",val, "with startval",startval)
        break
    val = startval+1