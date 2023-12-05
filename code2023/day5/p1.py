def parseData(data):
    data.append("")
    maps = []
    seeds = list(map(int, data[0].replace("seeds: ","").split(" ")))
    print(seeds)
    for line in data[2:]:

        if line=="":
            def mapping(lookups):
                def y(val):
                    for dest,source,dist in lookups:
                        if 0<=val-source<dist:
                            return dest+(val-source)
                    return val
                return y

            maps.append(mapping(lookups))
            lookups = []
            continue
        if 'map' in line:
            lookups = []
            name = line.split(" ")[0]
            continue
        print(line)
        lookups.append(list(map(int,line.split(" "))))

    return seeds, maps

def mapFromTo(val, fromToMap):
    return fromToMap(val,fromToMap)

maps = {}
with open("data.txt") as f:
    seeds, mapping = parseData(f.read().split("\n"))

maptypes = ["seed-to-soil",
"soil-to-fertilizer",
"fertilizer-to-water",
"water-to-light",
"light-to-temperature",
"temperature-to-humidity",
"humidity-to-location"]

print(seeds,"seed")
for type,m in zip(maptypes,mapping):
    seeds = list(map(m,seeds))
    print(seeds,type)

print(min(seeds))