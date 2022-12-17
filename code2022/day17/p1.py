pieceTypes = {
    0: [(0,0), (1,0), (2,0), (3,0)],
    1: [(1,0), (0,1), (1,1), (2,1), (1,2)],
    2: [(0,0), (1,0), (2,0), (2,1), (2,2)],
    3: [(0,0), (0,1), (0,2), (0,3)],
    4: [(1,0), (0,1), (1,1), (0,0)]}
class Piece:    
    def __init__(self, type, id, coord):
        self.num = id
        self.type = type
        self.coord = coord
        self.moving = True

    def getCoords(self):
        x,y = self.coord
        return [(x+a, y+b) for a,b in pieceTypes[self.type]]

    def getMovedCoords(self, pos):
        x,y = pos
        return [(x+a, y+b) for a,b in pieceTypes[self.type]]
    
    def isMoving(self):
        return self.moving
    
    def stop(self):
        self.moving = False
        
    def tryMove(self, direction):
        x,y = self.coord
        a,b = direction
        return (x+a, y+b)
        
    def move(self,direction):
        x,y = self.coord
        a,b = direction
        self.coord = (x+a, y+b)
        self.moving = True

    def __eq__(self, other):
        if isinstance(other, Piece): return self.coord == other.coord
        if isinstance(other, tuple): return self.coord == other
        return False

    def __hash__(self):
        return hash(self.num)
def printTetris(positions):
    y = max((y for x,y in stoppedPieces))
    screen = [['.' for col in range(8)] for row in range(y+1)]
    for col,row in positions:
        screen[row][col] = '#'
    
    for line in screen[::-1]:
        print("".join(line))
        
jets = {'<':(-1,0),
        '>':(1,0)}
stoppedPieces = set()
with open("data.txt") as f:
    pattern = f.read()

pieces = 2022
piecetype = 0
width = 7
pattern_index = 0
for p in range(pieces):    
    start = (2,max((y for x,y in stoppedPieces))+4) if len(stoppedPieces)>0 else (2,3)
    p = Piece(piecetype,p, start)
    piecetype = (piecetype+1)%len(pieceTypes)
    isMoving = True
    while isMoving:
        direction = jets[pattern[pattern_index]]
        pattern_index = (pattern_index+1)%len(pattern)

        
        for x,y in p.getMovedCoords(p.tryMove(direction)):
            if (x,y) in stoppedPieces:
                break
            if x < 0 or x >= width:
                break
        else:
            p.move(direction)
        
        direction = (0,-1)
        for x,y in p.getMovedCoords(p.tryMove(direction)): 
            if (x,y) in stoppedPieces:
                for pos in p.getCoords():
                    stoppedPieces.add(pos)
                isMoving = False
                break
            if y < 0:
                for pos in p.getCoords():
                    stoppedPieces.add(pos)
                isMoving = False
                break
        else:
            p.move(direction)
     
#printTetris(stoppedPieces)
print(max((y for x,y in stoppedPieces))+1)
