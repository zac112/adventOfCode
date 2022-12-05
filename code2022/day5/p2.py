import re
with open("data.txt") as f:
    data = f.read()

stacks = {}
for line in data.split("\n")[:8]:
    for i, x in enumerate(list(line[1::4]), 1):
        stacks.setdefault(i,[]).append(x)

for k,v in stacks.items():
    while " " in v:
        v.remove(" ")

print(stacks)
for line in data.split("\n")[10:]:
    amount,index,target = map(int,re.findall("(\d+)",line))
    
    boxes = stacks[index][:amount]
    for _ in range(amount):
        stacks[index].pop(0)    
    stacks[target][:0] = boxes

for k,v in stacks.items():
    print(v[0],end="")        
print()
