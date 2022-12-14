class Sand:
    def __init__(self, id, coord, abyssLimit):
        self.id = id
        self.coord = coord
        self.moving = True        
        self.y_limit = abyssLimit

    def move(self, movechecker_func, inabyss_func, print_func):
        if not self.moving: return        
                
        x,y = self.coord        
        if movechecker_func((x,y+1)):
            self.coord = (x,y+1)
        elif movechecker_func((x-1,y+1)):
            self.coord = (x-1,y+1)
        elif movechecker_func((x+1,y+1)):
            self.coord = (x+1,y+1)
        else:
            self.moving = False
            #print_func()

        if self.coord[1] > self.y_limit:
            inabyss_func(self)
            return
        #print(f"Sand moved to {self.coord}, moving {self.moving}")

    def __repr__(self):
        return str(self.coord)
class Cave:

    def __init__(self, coords):
        self.coords = coords
        self.entry = (500,0)
        self.sands = set()
        self.abyss = max([y for x,y in self.coords])+50
        print("Abyss at",self.abyss)

    def isAvailable(self,coord):
        if coord in [s.coord for s in self.sands]: return False
        if coord in self.coords: return False
        return True

    def addSand(self):
        self.sands.add(Sand(len(self.sands)+1, self.entry, self.abyss))        

    def removeSand(self, sand):
        print("Sand in abyss: current sand",len(self.sands)-1)
        raise Exception("Sand in abyss exception")
        
    def simulate(self):
        newSand = True
        for sand in self.sands:
            sand.move(self.isAvailable, self.removeSand, self.print)
            if sand.moving: newSand = False

        if newSand:
            self.addSand()

    def print(self):
        minx = min([x for x,y in self.coords])
        maxx = max([x for x,y in self.coords])
        maxy = max([y for x,y in self.coords])

        for row in range(maxy+1):
            line = []
            for col in range(minx,maxx+1):
                c = "."
                if (col,row) in self.coords: c = "#"
                if (col,row) in [s.coord for s in self.sands]: c = "o"
                line.append(c)
            print("".join(line))
        print()
            

coords = set()

with open("data.txt") as f:
    for line in f:
        corners = line.split(" -> ")
        for i,(start,end) in enumerate(zip(corners,corners[1:])):
            sx,sy = map(int,start.split(","))
            ex,ey = map(int,end.split(","))
            if sy == ey:
                if ex < sx:
                    s,e = ex,sx
                else:
                    s,e = sx,ex
                for x in range(s,e+1):
                    coords.add((x,sy))                
            elif sx == ex:
                if ey < sy:
                    s,e = ey,sy
                else:
                    s,e = sy,ey
                for y in range(s,e+1):
                    coords.add((sx,y))                
    cave = Cave(coords)

while True:
    try:
        cave.simulate()
    except:
        cave.print()
        break
