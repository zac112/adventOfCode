from collections import deque

def drawTrench(trench):
    for y in range(20):
        for x in range(10):
            if (x,y) in trench: print("#",end="")
            else: print(".",end="")
        print()

with open('data.txt') as f:
    data = f.read().splitlines()
    data = [line.split(" ") for line in data]

trench = set()
pos = (0,0)
dirs = {'D':(0,1),'U':(0,-1),'L':(-1,0),'R':(1,0)}
for D, L, colr in data:
    for _ in range(int(L)):
        x,y = pos
        pos = (x+dirs[D][0], y+dirs[D][1])
        trench.add(pos)

queue = deque([(1,1)])
while queue:
    pos = queue.popleft()
    if pos in trench: continue
    trench.add(pos)
    for d, v in dirs.items():
        queue.append((pos[0]+v[0],pos[1]+v[1]))
drawTrench(trench)
print(len(trench))
