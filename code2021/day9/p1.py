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
            #print(neighbors, matrix[y][x])
            if matrix[y][x] < min(neighbors, default=10) :
                lowPoints.append(matrix[y][x])
    return lowPoints

print(sum(map(lambda a:a+1,rollingWindow(floor,1))))
