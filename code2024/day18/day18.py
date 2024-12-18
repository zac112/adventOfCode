from collections import namedtuple
with open('data.txt')as file:
    lines = file.readlines()
    coords = set((int(x),int(y)) for x,y in map(lambda a:a.split(","),lines[:1024]))
print(coords)

area=namedtuple("area",['x','y'])
areamax = area(70,70)

def BFS(path):
    stack = [((0,0),None)]
    while stack:
        (x,y), oldCoord = stack.pop(0)
        if not (0<=x<=areamax.x and 0<=y<=areamax.y): continue
        if (x,y) in coords: continue  
        if (x,y) in path: continue
        path[(x,y)] = oldCoord
        
        if (x,y) == areamax: break
        stack.append(((x+1,y), (x,y)))
        stack.append(((x-1,y), (x,y)))
        stack.append(((x,y+1), (x,y)))
        stack.append(((x,y-1), (x,y)))
    return path

path = BFS({})
steps = 0
node = (70,70)
while node:
    node = path[node]
    steps += 1
steps -= 1
print("P1",steps)

#P2
i = 1024
while (70,70) in path:
    newByte = tuple(map(int,lines[i].split(",")))
    coords.add(newByte)
    path = BFS({})
    i += 1

print(newByte)