from itertools import product
from math import cos, sin, radians
from collections import defaultdict

class Scanner():
    def __init__(self,num):
        self.coords = {}
        self.rotation = None
        self.position = None
        self.neighbors = []
        self.num = num
        
        self.rot = lambda x,y,z:[
            [cos(z)*cos(y),cos(z)*sin(y)*sin(x)-sin(z)*cos(x),cos(z)*sin(y)*cos(x)+sin(z)*sin(x)],
            [sin(z)*cos(y),sin(z)*sin(y)*sin(x)+cos(z)*cos(x),sin(z)*sin(y)*cos(x)-cos(z)*sin(x)],
            [-sin(y),cos(y)*sin(x),cos(y)*cos(x)]
             ]
        
    def translate(self, coord, rotation):
        rot = self.rot(*(radians(x) for x in rotation))
        
        x = round(rot[0][0]*coord[0]+rot[0][1]*coord[1]+rot[0][2]*coord[2])
        y = round(rot[1][0]*coord[0]+rot[1][1]*coord[1]+rot[1][2]*coord[2])
        z = round(rot[2][0]*coord[0]+rot[2][1]*coord[1]+rot[2][2]*coord[2])
        
        return (x,y,z)
        
    def addCoordinate(self, coord):
        coord = [int(x) for x in coord]
        for x,y,z in product([0,90,180,270],repeat=3):
            rot = (x,y,z)
            self.coords.setdefault(rot,set()).add(self.translate(coord, rot))

    def getCoordinates(self, rotation):
        return set(self.coords[rotation])


    def tupleAdd(self, t1, t2):
        return tuple(map(lambda a:a[0]+a[1], zip(t1,t2)))

    def tupleSubtract(self, t1, t2):
        return tuple(map(lambda a:a[0]-a[1], zip(t1,t2)))
                     
    def getAbsoluteCoordinates(self):        
        return set(self.tupleAdd(self.position,x) for x in self.coords[self.rotation])
    
    def getOverlaps(self, otherScanner):
        subtract = self.tupleSubtract
        add = self.tupleAdd

        ownBeaconAbsPositions = [add(self.position,x) for x in self.coords[self.rotation]]
        for rot in product([0,90,180,270],repeat=3):
            overlaps = defaultdict(int)
            for beaconAbsPos, coord in product(ownBeaconAbsPositions, otherScanner.getCoordinates(rot)):
                #Move from known beacon pos to the sat
                otherSatPos = subtract(beaconAbsPos, coord)
                overlaps[otherSatPos] += 1
            
            if len([x for x in overlaps.values() if x >= 12]) >=1:
                o = [(k,v) for k,v in overlaps.items() if v >= 12]
                print("Detected overlap",o)
                otherScanner.position = o[0][0]
                otherScanner.rotation = rot
                print(self)
                print(otherScanner)
                
                return    
        
        

    def __repr__(self):
        return f"Scanner{self.num}:{self.position=},{self.rotation=}"
                        
                        
scanners = []
with open('data.txt') as f:    
    s = Scanner(0)
    s.position = (0,0,0)
    s.rotation = (0,0,0)
    scanners.append(s)
    f.readline()
    i=1
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        if "scanner" in line:
            s = Scanner(i)
            scanners.append(s)
            i+=1
            continue
        
        s.addCoordinate(line.split(","))

print(scanners)
while not all([x.position for x in scanners]):
    for s1 in scanners:
        for s2 in scanners:
            if s1==s2: continue
            if s1.position is None:
                continue
            if s2.position is not None:
                continue
            #print(s1,"woitjn ",s2)
            s1.getOverlaps(s2)

beacons = set()
for s in scanners:
    beacons |= s.getAbsoluteCoordinates()
print(len(beacons))
