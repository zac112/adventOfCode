from itertools import product

with open('data.txt') as f:
    antennas = {}
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line):
            if c in ".\n": continue
            antennas.setdefault(c,[]).append((x,y))
    areamax = (x,y)
    
direction = lambda a,b:(b[0]-a[0],b[1]-a[1])
tuplesum = lambda a,b:(a[0]+b[0],a[1]+b[1])
antinodes = set()
for k,v in antennas.items():
    for a,b in product(v,repeat=2):
        if a==b:continue
        s = direction(a,b)
        antinode = tuplesum(b,s)
        if 0<=antinode[0]<=areamax[0] and 0<=antinode[1]<=areamax[1]:
            antinodes.add(antinode)

print("Part 1:",len(antinodes))

#P2
antinodes = set().union(*antennas.values())
for k,v in antennas.items():
    for a,b in product(v,repeat=2):        
        if a==b:continue
        s = direction(a,b)        
        antinode = tuplesum(b,s)
        while 0<=antinode[0]<=areamax[0] and 0<=antinode[1]<=areamax[1]:
            antinodes.add(antinode)
            antinode = tuplesum(antinode,s)

print("Part 2 (with harmonics):",len(antinodes))
