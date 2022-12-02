class Tile:

    def __init__(self, tile,lines):
        self.id = int(tile)
        self.lines=lines

    def print(self):
        for line in self.lines:
            print(line)

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

    def canCombine(self, other):
        if self.matches(other.getTop()):
            return True
        if self.matches(other.getBottom()):
            return True
        if self.matches(other.getLeft()):
            return True
        if self.matches(other.getRight()):
            return True
        if self.matches(other.getTop(True)):
            return True
        if self.matches(other.getBottom(True)):
            return True
        if self.matches(other.getLeft(True)):
            return True
        if self.matches(other.getRight(True)):
            return True
        return False
        
    def matches(self,side):
        #print(side)
        if side == self.getTop():
            return True
        if side == self.getTop(True):
            return True
        if side == self.getBottom():
            return True
        if side == self.getBottom(True):
            return True
        if side == self.getLeft():
            return True
        if side == self.getLeft(True):
            return True
        if side == self.getRight():
            return True
        if side == self.getRight(True):
            return True
        return False

tiles = []
with open('data.txt') as f:
    while True:
        line = f.readline()
        if not line: break        
        tileid = line[:-2].split(" ")[1:][0]
        lines = [f.readline()[:-1] for _ in range(10)]
        tiles.append(Tile(tileid, lines))
        f.readline()

matches = {}
for i,t in enumerate(tiles):
    matches.setdefault(t.id,0)
    for j,t1 in enumerate(tiles[i:],i):
        matches.setdefault(t1.id,0)
        if t == t1:continue
        if t.canCombine(t1):
            #print(t,t1)
            matches[t.id] += 1
            matches[t1.id] += 1
    
print(len(tiles))
print([(a,b) for a,b in matches.items() if b==2])

