from collections import namedtuple
from heapq import heappop, heappush
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PriorityItem:
    risk: int
    item: Any=field(compare=False)


with open('data.txt') as f:
    maze = [[int(x.strip()) for x in line if x.strip() != ""] for line in f.readlines()]

newMaze = []
for x in range(0,5):
    for line in maze:
        newRow = []
        newMaze.append(newRow)
        for y in range(0,5):        
            for cell in line:
                newVal = x+y+cell
                if newVal > 9:
                    newRow.append(newVal%10+1)
                else:
                    newRow.append(newVal)
                    
#[print("".join(map(str,row))) for row in newMaze]
maze = newMaze               

cell = namedtuple('cell',['y','x','previous'])
start = (0,0)
end = (len(maze)-1, len(maze[0])-1)
    
def BFS():
    def getNeighbors(x,y):        
        for xdiff in range(-1,2):
            for ydiff in range(-1,2):
                x1,y1 = x+xdiff, y+ydiff
                if not (xdiff == 0 or ydiff ==0):
                    continue
                if x1<0 or y1 < 0 or x1 >=len(maze) or y1>= len(maze):
                    continue
                
                yield (y1,x1,maze[y1][x1])
    
    queue = [PriorityItem(risk=maze[0][0],item=cell(*start,None))]
    
    visited = set()    
    while queue:
        item = heappop(queue)
        node = item.item        

        coord = (node.x,node.y)
        if coord in visited:
            continue
        visited.add(coord)
        
        for x,y,risk in getNeighbors(node.x,node.y):
            heappush(queue,PriorityItem(risk=item.risk+risk,item=cell(x,y,node)))
        
        if node.x == end[0] and node.y == end[1]:
            return item
        
    
path = BFS()
#print(path.item)
print(path.risk-maze[start[1]][start[0]])
