import re
import itertools

with open("data.txt") as f:
    data = f.read()
    instructions = data.split("\n")[0]
    pat = "([A-Z]+) = \\(([A-Z]+), ([A-Z]+)\\)"
    directions = {x[0]:(x[1],x[2]) for x in re.findall(pat,data)}
    
move = lambda loc, direction:directions[loc][0 if direction=="L" else 1]
steps = 0
location = "AAA"
target = "ZZZ"
for d in itertools.cycle(instructions):
    location = move(location, d)
    steps += 1
    if location == target:
        break

print(steps)