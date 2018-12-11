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
for x in range(len(grid)-3):
    for y in range(len(grid)-3):        
        gridSum = 0
        for x1 in range(3):            
            for y1 in range(3):
                gridSum += grid[x+x1][y+y1]

        if gridSum > maxGridSum:            
            maxGridSum = gridSum
            xCoord = x+1
            yCoord = y+1

print (maxGridSum,"at",xCoord,",",yCoord)
