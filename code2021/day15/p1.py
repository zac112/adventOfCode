from functools import reduce
from collections import namedtuple

with open('data_test1.txt') as f:
    maze = [[int(x.strip()) for x in line if x.strip() != ""] for line in f.readlines()]

cell = namedtuple('cell',['y','x','level','risk','previous'])
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
    
    queue = [cell(*start,0,maze[0][0],None)]
    
    visited = []
    while queue:
        node = queue.pop(0)
        if (node.x,node.y) in map(lambda a:(a.x,a.y),visited):
            continue
        
        level = node.level+1
        visited.append(node)
        
        allRisk = node.risk
        neighbors = getNeighbors(node.x,node.y)
        neighbors = [cell(x,y,level,allRisk+risk,node) for x,y,risk in neighbors]
        queue.extend(neighbors)
        queue.sort(key=lambda a: a.risk)
        if visited[-1].x == end[0] and visited[-1].y == end[1]:
            #print('found path',visited[-1])
            return visited[-1]
        
    
path = BFS()
print(path.risk-maze[start[1]][start[0]])
