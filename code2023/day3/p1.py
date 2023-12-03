class Number:

    def __init__(self, num):
        self.digits = []
        self.coords = []
        self.id = num

    def getValue(self):
        if len(self.digits)==0: return 0
        return int("".join(self.digits))
    
    def isPartNumber(self, diagram):
        return any([diagram.get((cx+x, cy+y),self).isSymbol()
                    for (cx,cy) in self.coords
                    for x in [-1,0,1]
                    for y in [-1,0,1]
                    ])  

    def addDigit(self, digit): self.digits.append(digit)
    def addCoord(self, coord): self.coords.append(coord)
    def isSymbol(self): return False
    def __hash__(self) -> int: return self.id    
    def __repr__(self): return "".join(self.digits)
        
class Symbol:
    def __init__(self, symbol):
        self.numbers = []
        self.symbol = symbol

    def isSymbol(self): return True    
    def getValue(self): return 0    
    def isPartNumber(self, diagram): return False    
    def __repr__(self): return self.symbol

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
                sym = Symbol(cells.pop(0))
                diagram[(x,y)] = sym
                x += 1
        except:
            pass

partNumsSum = 0
numbers = set([num for num in diagram.values() if num.isPartNumber(diagram)])
for num in numbers:
    partNumsSum += num.getValue()
print(partNumsSum)