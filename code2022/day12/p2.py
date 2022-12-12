import string
from collections import deque

with open("data.txt") as f:
    maze = [list(line) for line in f.read().splitlines()]

correction = {b:a for a,b in enumerate(string.ascii_lowercase)}
path = [[None for _ in range(len(maze[0]))]for _ in range(len(maze))]

possibleStarts = []
for y,row in enumerate(maze):
    for x,cell in enumerate(row):
        if cell == "S":
            start=(y,x)
            cell = 'a'
        if cell == "E":
            end=(y,x)
            cell = 'z'
        maze[y][x]=string.ascii_lowercase.index(cell)
        if cell == 'a':
            possibleStarts.append((y,x))
            
neighbors = [(1,0),(0,1),(-1,0),(0,-1)]

def BFS(maze,path,openCells):
    while openCells:
        y,x,level,from_y, from_x = openCells.popleft()        
        try: maze[y][x]
        except:continue
        
        if path[y][x] is not None: continue
        if y < 0 or x < 0: continue
        if maze[y][x] >= maze[from_y][from_x]+2: continue
        path[y][x] = (from_y,from_x)
        
        if (y,x) == end:
            print(level)
            return level
        newCells = [(y+a,x+b) for a,b in neighbors]        
        for cell in newCells:
            openCells.append((*cell,level+1,y,x))

lengths = []
for start in possibleStarts:
    path = [[None for _ in range(len(maze[0]))]for _ in range(len(maze))]
    cells = deque()
    cells.append((*start,0,*start))
    length = BFS(maze,path, cells)
    if length:
        lengths.append(length)
print(min(lengths))
