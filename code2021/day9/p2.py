from functools import reduce

with open('data.txt') as file:
    floor = [list(map(int,x[:-1])) for x in file.readlines() if x != "\n"]

#print(floor)

def rollingWindow(matrix, size):
    def get(x,y):
        if x < 0 or y < 0:
            return 10
        try:
            return matrix[y][x]
        except:
            return 10
        
    lowPoints = []
    for y, line in enumerate(matrix):
        for x, cell in enumerate(line):
            neighbors = []
            for xdiff in range(-size,size+1):
                for ydiff in range(-size,size+1):
                    
                    if (ydiff == 0 or xdiff == 0):
                        if ydiff == 0 and xdiff == 0:
                            continue
                        neighbors.append(get(x+xdiff, y+ydiff))
            
            if matrix[y][x] < min(neighbors, default=10) :
                lowPoints.append((y,x))
    return lowPoints

visited = set()
def BFS(y,x):
    if (y,x) in visited:
        return 0    
    
    visited.add((y,x))

    if y < 0 or x < 0 or y >= len(floor) or x >= len(floor[0]):
        return 0
    
    if floor[y][x] == 9:
        return 0
    
    size = 1
    size += BFS(y+1,x)
    size += BFS(y-1,x)
    size += BFS(y,x+1)
    size += BFS(y,x-1)

    return size

lowPoints = rollingWindow(floor,1)

sizes = []
for coord in lowPoints:
    sizes.append(BFS(*coord))

print(reduce(lambda a,b: a*b,sorted(sizes)[-3:]))
