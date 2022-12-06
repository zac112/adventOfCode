class Tile:

    def __init__(self, tile,lines):
        self.id = int(tile)
        self.lines=lines
        self.connections = {'T':None,
                            'B':None,
                            'R':None,
                            'L':None}

    def print(self):
        for line in self.lines:
            print(line)

    def flipHorizontally(self):
        for i,line in enumerate(self.lines):
            self.lines[i] = self.lines[i][::-1]

    def flipVertically(self):
        for i in range(len(self.lines)//2):
            self.lines[i],self.lines[len(self.lines)-i-1] = self.lines[len(self.lines)-i-1],self.lines[i]

    def rotateCounterCW(self,times):
        times = times%4        
        for x in range(times):
            newlines = []
            for i,line in enumerate(self.lines):
                newlines.append("".join([l[::-1][i] for l in self.lines]))
            self.lines = newlines
            
    def getTop(self, reverse=False):
        res = self.lines[0]
        if reverse:
            return "".join(reversed(res))
        return res
    
    def getBottom(self, reverse=False):
        res = self.lines[-1]
        if reverse:
            return "".join(reversed(res))
        return res
    
    def getLeft(self, reverse=False):
        res = "".join([l[0] for l in self.lines])
        if reverse:
            return "".join(reversed(res))
        return res
    
    def getRight(self, reverse=False):
        res = "".join([l[-1] for l in self.lines])
        if reverse:
            return "".join(reversed(res))
        return res
            
    def combine(self, other):        
        connection = []
        if not self.canCombine(other,connection): return False
        
        connection = "".join(connection)
        valid = ['TB', 'BT', 'LR', 'RL']
        rots = {'B':'R',
                'R':'T',
                'T':'L',
                'L':'B'}
        while connection not in valid:
            other.rotateCounterCW(1)
            connection = connection[0]+rots[connection[1]]

        self.connections[connection[0]] = other        
        return True

    def getCharacters(self, borders=True):
        if borders: return ["".join(l) for l in self.lines]
        
        result = self.lines[1:-1]
        result = [l[1:-1] for l in result]
        return result

    def getSides(self):
        return [self.getTop(), self.getRight(), self.getBottom(), self.getLeft(),
                self.getTop(True), self.getRight(True) ,self.getBottom(True), self.getLeft(True)]
            
    def canCombine(self, other, connection):
        if self.matches(other.getTop(),connection):
            connection.append("T")
            return True

        if self.matches(other.getBottom(),connection):
            connection.append("B")
            return True

        if self.matches(other.getLeft(),connection):
            connection.append("L")
            return True

        if self.matches(other.getRight(),connection):
            connection.append("R")
            return True

        if self.matches(other.getTop(True),connection):
            connection.append("T")
            other.flipHorizontally()            
            return True
        
        if self.matches(other.getBottom(True),connection):
            connection.append("B")
            #other.flipHorizontally()
            return True

        if self.matches(other.getLeft(True),connection):
            connection.append("L")
            other.flipVertically()
            return True

        if self.matches(other.getRight(True),connection):
            connection.append("R")
            other.flipVertically()
            return True
        connection.clear()
        return False
        
    def matches(self,side,connection):
        #print(side)
        if side == self.getTop():
            connection.append("T")
            return True
        if side == self.getBottom():
            connection.append("B")
            return True
        if side == self.getLeft():
            connection.append("L")
            return True
        if side == self.getRight():
            connection.append("R")
            return True
        return False

    def topMatches(self, side):
        if side == self.getTop():
            return True
    def rightMatches(self, side):
        if side == self.getRight():
            return True
    def bottomMatches(self, side):
        if side == self.getBottom():
            return True
    def leftMatches(self,side):
        if side == self.getLeft():
            return True
        
    def __str__(self):
        return str(self.id)
    def __repr__(self):
        return str(self.id)
    def __eq__(self, other):
        if not isinstance(other,Tile): return False
        return other.id == self.id
    def __hash__(self):
        return hash(self.id)

tiles = []
with open('data.txt') as f:
    while True:
        line = f.readline()
        if not line: break        
        tileid = line[:-2].split(" ")[1:][0]
        lines = [f.readline()[:-1] for _ in range(10)]
        tiles.append(Tile(tileid, lines))
        f.readline()

matched = {}
for i,t in enumerate(tiles):
    for j,t1 in enumerate(tiles[i:],i):
        if t == t1: continue
        if t.canCombine(t1,[]):
            matched.setdefault(t,[]).append(t1)
            matched.setdefault(t1,[]).append(t)

#corner piece from p1        
tile = [t for t in tiles if t.id==2621][0]
        
picture = [[' ' for i in range(12)] for i in range(12)]

for t in matched[tile]:    
    tile.combine(t)

picture[0][0] = tile
picture[0][1] = tile.connections['R']
picture[1][0] = tile.connections['B']

def getFreeNeighbors(picture, pos):
    f,s = pos
    if f < 0 or s < 0: return tiles
    
    neighbors = matched[picture[pos[0]][pos[1]]]
    if pos[0]-1 >= 0 and picture[pos[0]-1][pos[1]] in neighbors:
        neighbors.remove(picture[pos[0]-1][pos[1]])
    if pos[1]-1 >= 0 and picture[pos[0]][pos[1]-1] in neighbors:
        neighbors.remove(picture[pos[0]][pos[1]-1])
    if pos[1]+1 < len(picture[pos[0]]) and picture[pos[0]][pos[1]+1] in neighbors:
        neighbors.remove(picture[pos[0]][pos[1]+1])
    if pos[0]+1 < len(picture) and picture[pos[0]+1][pos[1]] in neighbors:
        neighbors.remove(picture[pos[0]+1][pos[1]])
    return neighbors

nextTiles = [(1,1),(0,2),(2,0)]
while nextTiles:
    t = nextTiles.pop(0)
    f,s = t
    if f >= len(picture) or s >= len(picture[f]):continue
    if picture[t[0]][t[1]] != " ": continue
    
    nextTiles.append((t[0]+1,t[1]))
    nextTiles.append((t[0],t[1]+1))
    nextTiles.append((t[0]+1,t[1]+1))
    n = getFreeNeighbors(picture,(f-1,s))
    n1 = getFreeNeighbors(picture,(f,s-1))
    a = list(set(n).intersection(n1))
    picture[t[0]][t[1]] = a[0]

print("Tile ids:")
for l in picture:
    print(f"{','.join(map(str,l))}")

#Rotate pieces correctly, first row
left = picture[0][0]
for tile in picture[0][1:]:
    turns = 0
    while tile.getLeft()!=left.getRight():
        tile.rotateCounterCW(1)
        turns += 1
        if turns == 4:
            tile.flipHorizontally()
        if turns == 8:
            print("no match")
            break
    left = tile

#Rotate pieces correctly, first column
top = picture[0][0]
for tile in picture[1:]:
    tile = tile[0]
    turns = 0
    while tile.getTop()!=top.getBottom():
        tile.rotateCounterCW(1)
        turns += 1
        if turns == 4:
            tile.flipHorizontally()
        if turns == 8:
            print("no match")
            break
    top = tile

#Rotate pieces correctly, the rest
for i, row in enumerate(picture[1:],1):
    for j, tile in enumerate(row[1:],1):
        top = picture[i-1][j]
        left = picture[i][j-1]
        turns = 0
        while not (tile.getTop()==top.getBottom() and tile.getLeft()==left.getRight()):
            tile.rotateCounterCW(1)            
            if turns == 7:
                tile.flipHorizontally()
            if turns == 14:
                tile.flipVertically()
            if turns == 19:
                print("no match")
                break
            turns += 1

#expand tiles from cells to a 2-d matrix
largePicture = [["" for _ in range(12*8)] for _ in range(12*8)]
for i, row in enumerate(picture):
    for j, cell in enumerate(row):
        pic = cell.getCharacters(borders=False)
        for ii,rrow in enumerate(pic):
            for jj, char in enumerate(rrow):
                largePicture[i*8+ii][j*8+jj] = char

#offset coords for monster pieces (y,x)
seaMonster =[(1, 0), (2, 1), (2, 4), (1, 5), (1, 6), (2, 7), (2, 10), (1, 11), (1, 12), (2, 13), (2, 16), (1, 17), (0, 18), (1, 18), (1, 19)]

monsters = 0
largePicture = Tile(0,largePicture)
#manually tested number of rotations
largePicture.rotateCounterCW(2)
largePicture = largePicture.getCharacters(borders=True)

for i, row in enumerate(largePicture):
    for j, cell in enumerate(row):
        try:
            cells = [largePicture[i+y][j+x] for y,x in seaMonster]
        except:
            continue
        if all(map(lambda a: a=="#",cells)):
            for y,x in seaMonster:
                largePicture[i+y] = largePicture[i+y][:j+x]+'o'+largePicture[i+y][j+x+1:]
            monsters += 1
        
for row in largePicture:
    print("".join(row))

roughness = 0
for i, row in enumerate(largePicture):
    for j, cell in enumerate(row):
        if cell == "#":
            roughness += 1
print(f"Sea {roughness=} with {monsters} monsters")
