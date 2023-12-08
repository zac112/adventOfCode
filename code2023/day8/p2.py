import re
import itertools
from math import lcm

with open("data.txt") as f:
    data = f.read()
    instructions = data.split("\n")[0]
    pat = "([A-Z]+) = \\(([A-Z]+), ([A-Z]+)\\)"
    directions = {x[0]:(x[1],x[2]) for x in re.findall(pat,data)}


move = lambda loc, direction:directions[loc][0 if direction=="L" else 1]
steps = 0
locations = [key for key in directions if key[-1]=='A']
cycles = list(map(lambda a:(a,0),locations))

for d in itertools.cycle(instructions):
    if all(map(lambda a:a[1]>0,cycles)):
        break

    for i,(loc,(target,step)) in enumerate(zip(locations,cycles)):
        if loc[-1]=='Z'and target[-1]!='Z' and step==0:
            cycles[i] = (loc,steps)

    locations = list(map(lambda loc:move(loc,d), locations))    
    steps += 1

print()
print(lcm(*map(lambda a:a[1],cycles)))