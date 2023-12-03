from functools import reduce 

class Number:

    def __init__(self, num):
        self.digits = []
        self.coords = []
        self.id = num

    def addDigit(self, digit):
        self.digits.append(digit)

    def addCoord(self, coord):
        self.coords.append(coord)

    def getValue(self):
        if len(self.digits)==0: return 0
        return int("".join(self.digits))
    
    def isPartNumber(self, diagram):
        return any([diagram.get((cx+x, cy+y),self).isSymbol()
                    for (cx,cy) in self.coords
                    for x in [-1,0,1]
                    for y in [-1,0,1]
                    ])        

    def isSymbol(self):
        return False
    
    def isGear(self, diagram):
        return False

    def __hash__(self) -> int:
        return self.id
    
    def __repr__(self):
        return "".join(self.digits)
        
class Symbol:
    def __init__(self, symbol, coord):
        self.numbers = []
        self.symbol = symbol
        self.coord = coord

    def isSymbol(self):
        return True
    
    def getValue(self):
        return 0
    
    def isPartNumber(self, diagram):
        return False
    
    def isGear(self, diagram):
        return len(self.getNeighbors(diagram))==2
    
    def getNeighbors(self, diagram):
        cx,cy = self.coord
        return set(diagram.get((cx+x, cy+y)) 
                        for x in [-1,0,1] 
                        for y in [-1,0,1] 
                        if diagram.get((cx+x, cy+y),self).isPartNumber(diagram)
                    )
    
    def findRatio(self, diagram):
        return reduce(lambda a,b:a.getValue()*b.getValue(), self.getNeighbors(diagram))

    def __repr__(self):
        return self.symbol

with open("data.txt") as f:
    data = f.readlines()

numID = 0
diagram = {}

for y, line in enumerate(data):
    cells = list(line.replace("\n",""))    
    x = 0
    while cells:
        try: 
            while cells[0]==".":
                cells.pop(0)
                x += 1

            if cells[0] in "1234567890":
                num = Number(numID)
                numID += 1
                while cells[0] in "1234567890":
                    num.addDigit(cells.pop(0))
                    num.addCoord((x,y))
                    diagram[(x,y)] = num
                    x += 1

            if cells[0] not in ".1234567890":
                sym = Symbol(cells.pop(0), (x,y))
                diagram[(x,y)] = sym
                x += 1
        except:
            pass

gearRatios = 0
gears = set([symbol for symbol in diagram.values() if symbol.isGear(diagram)])
for gear in gears:
    gearRatios += gear.findRatio(diagram)
print(gearRatios)
