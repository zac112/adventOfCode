with open('data.txt') as file:
    dumbos = [[int(x) for x in line[:-1]] for line in file.readlines()]

print(dumbos)

def neighborIndices(matrix, y,x,size):
    for i in range(-size,size+1):
        for j in range(-size,size+1):
            x1, y1 = x+j, y+i
            if i == 0 and j == 0:
                continue
            if x1 < 0 or y1 < 0 or x1 >=len(matrix[0]) or y1 >=len(matrix):
                continue
            yield (y1,x1)

def findCoords(m, comp):
    return [(x,y) for x in range(len(dumbos)) for y in range(len(dumbos[0])) if comp(dumbos[x][y])]

def step():
    flashed = set()
    newDumbos = [[dumbos[i][j]+1 for j in range(len(dumbos[0]))] for i in range(len(dumbos))]
    
    def flash(i,j):
        #print('flashing',i,j)
        for i,j in neighborIndices(dumbos,i,j,size=1):            
            newDumbos[i][j] += 1
            dumbos[i][j] += 1
    
    while flashable := findCoords(dumbos, lambda a:a>=9):
        for i,j in flashable:
            if dumbos[i][j] >= 9:                         
                flash(i,j)
                flashed.add((i,j))

        for i,j in flashed:
            dumbos[i][j] = 0
            newDumbos[i][j] = 0
                
    return newDumbos

steps = 100
numFlashed = 0
for _ in range(steps):
    dumbos = step()
    flashed = findCoords(dumbos, lambda a:a==0)
    numFlashed += len(flashed)
    #[print (x) for x in dumbos]
print(numFlashed)
