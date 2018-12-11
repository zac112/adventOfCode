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

for x in range(len(grid)):
    for y in range(len(grid)):
        if (y%100 == 0):
            print (x,y)
        for size in range(min(len(grid)-x-1, len(grid)-y-1)):
            gridSum = 0
            for x1 in range( size ):            
                for y1 in range( size ):
                    gridSum += grid[x+x1][y+y1]

            if gridSum > maxGridSum:            
                maxGridSum = gridSum
                xCoord = x+1
                yCoord = y+1
                maxSize = size+1

print (maxGridSum,"at",xCoord,",",yCoord,",",maxSize)
