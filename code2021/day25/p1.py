from copy import deepcopy
from collections import namedtuple

area = []
with open('data.txt') as f:
    for line in f.readlines():
        area.append(list(line.strip()))
        
def step(area):
    newarea = deepcopy(area)
    changes = 0
    moved = set()
    
    for y,row in enumerate(area):
        for x,cell in enumerate(row):
            if cell == '>':
                if (x,y) in moved: continue
                newx = (x+1)%len(area[y])
                if area[y][newx]=='.':
                    newarea[y][newx] = '>'
                    newarea[y][x] = '.'
                    changes += 1
                    moved.add((newx,y))

    area = deepcopy(newarea)
    newarea = deepcopy(area)
    for y,row in enumerate(area):
        for x,cell in enumerate(row):            
            if cell == 'v':
                if (x,y) in moved: continue
                newy = (y+1)%len(area)
                if area[newy][x]=='.':
                    newarea[newy][x] = 'v'
                    newarea[y][x] = '.'
                    changes += 1
                    moved.add((x,newy))

    return (newarea,changes)

def printarea(area):
    [print("".join(line)) for line in area]
    print()

steps = 0
while True:
    #print(steps)
    #printarea(area)
    steps += 1
    area,changes = step(area)
    if changes == 0: break

printarea(area)
print(steps)
