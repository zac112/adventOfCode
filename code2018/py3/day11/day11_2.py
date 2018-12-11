def fuelCellPower(x, y, serial):
    rack = x+10
    initialPower = y*rack
    added = initialPower+serial
    multiplied = added*rack
    hundredDigit = ((multiplied // 100) %10) -5
    return hundredDigit

puzzleInput = 8979
#puzzleInput = 18

grid = [[fuelCellPower(x,y,puzzleInput) for y in range(1,301)] for x in range(1,301)]

maxGridSum = 0
xCoord = 0
yCoord = 0
maxSize = 0

#{ (x,y, size) -> value }
preCalculated = {}

for x in range(len(grid)-1, -1, -1):
    for y in range(len(grid)-1, -1, -1):
        if (y%100 == 0):
            print (x,y,"   \t", maxSize,":",maxGridSum)
        for size in range( min(len(grid)-x, len(grid)-y) ):
            if(size == 0):
                gridSum = grid[x][y]
            else:
                gridSum = grid[x][y] + preCalculated[(x+1,y+1,size-1)]
            for x1 in range(1,  size+1 ): 
                gridSum += grid[x][y+x1] + grid[x+x1][y]

            preCalculated[(x,y, size)] = gridSum
            
            if gridSum > maxGridSum:
                maxGridSum = gridSum
                xCoord = x+1
                yCoord = y+1
                maxSize = size+1

print (maxGridSum,"at",xCoord,",",yCoord,",",maxSize)
