class Sand:
    def __init__(self, id, coord, abyssLimit):
        self.id = id
        self.start = coord
        self.coord = coord
        self.moving = True        
        self.y_limit = abyssLimit

    def simulate(self, movechecker_func, inabyss_func, print_func, stopped_func):
        while self.moving: 
                
            x,y = self.coord        
            if movechecker_func((x,y+1)):
                self.coord = (x,y+1)
            elif movechecker_func((x-1,y+1)):
                self.coord = (x-1,y+1)
            elif movechecker_func((x+1,y+1)):
                self.coord = (x+1,y+1)
            else:
                self.moving = False
                stopped_func()
                #print_func()

            if self.coord[1]+1 == self.y_limit:
                self.moving = False
                stopped_func()
                break

            if not self.moving and self.coord == self.start:
                inabyss_func(self)
                break
            #print(f"Sand moved to {self.coord}, moving {self.moving}")

    def __repr__(self):
        return str(self.coord)

    def __hash__(self):
        return hash(self.coord)
    
    def __eq__(self,other):
        if isinstance(other,Sand): return other.coord == self.coord
        if isinstance(other,tuple): return other == self.coord
        return False
class Cave:

    def __init__(self, coords):
        self.coords = coords
        self.entry = (500,0)
        self.sands = set()
        self.floor = max([y for x,y in self.coords])+2
        print("Floor at",self.floor)

    def isAvailable(self,coord):
        if coord in self.sands: return False
        if coord in self.coords: return False
        return True

    def removeSand(self, sand):
        print("Sand in start: current sand",len(self.sands)+1)
        raise Exception("Sand in abyss exception")

    def sandStopped(self):
        #print(len(self.sands))
        pass
        
    def simulate(self):
        sand = Sand(len(self.sands)+1, self.entry, self.floor)
        sand.simulate(self.isAvailable, self.removeSand, self.print,self.sandStopped)
        self.sands.add(sand)

    def print(self):
        minx = min([x for x,y in self.coords])
        maxx = max([x for x,y in self.coords])
        maxy = max([y for x,y in self.coords])

        for row in range(maxy+2):
            line = []
            for col in range(minx,maxx+1):
                c = "."
                if (col,row) in self.coords: c = "#"
                if (col,row) in self.sands: c = "o"
                line.append(c)
            print("".join(line))
        
        print("".join(["#"]*(maxx-minx)))
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
    except Exception as e:
        print(e)
        cave.print()
        print(len(cave.sands)+1)
        break
