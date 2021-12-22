import re
from functools import reduce
from collections import defaultdict
from itertools import zip_longest, product
import math

class Space():
    def __init__(self):
        self.cubes = []

    def addCube(self, new):        
        for c in self.cubes:
            c.addOverlap(new)
        if new.mode == 'on':
            self.cubes.append(new)
        
    def countOn(self):
        result = 0
        for c in self.cubes:
            result +=c.count()
        return result

    def __repr__(self):
        return f"{self.cubes}"
        
class Cube():

    def __init__(self, coords, mode):
        self.coords = coords
        self.x, self.y, self.z = coords
        self.start = (self.x[0],self.y[0],self.z[0])
        self.end = (self.x[1],self.y[1],self.z[1])
        self.mode = mode
        self.overlap = []
       
    def count(self):
        res = reduce(lambda a,b: a*(b[1]-b[0]), self.coords,1) 
        for c in self.overlap:
            res -= c.count()
        return res
            
    def getOverlap(self, other):
                
        new = []
        for i in range(3):
            max_start = max(self.coords[i][0], other.coords[i][0])
            min_end = min(self.coords[i][1], other.coords[i][1])
            if max_start <= min_end:
                new_start = max_start
                new_end = min_end
            else:
                new_start = 0
                new_end = 0
            new.append([new_start,new_end])

        new = Cube(new, "off")
        return new
        
    
    def addOverlap(self, other):
        
        overlap = self.getOverlap(other)
        
        if overlap and overlap.count()>0:
            for c in self.overlap:
                if c == overlap: continue
                c.addOverlap(overlap)
        
            
            self.overlap.append(overlap)

    def __repr__(self):
        return f"({self.mode}) x={self.x} y={self.y} z={self.z} overlaps={self.overlap}"

cubes = Space()

with open('data.txt') as f:
    for line in f.readlines():
        print(line)
        mode, coords = line.split(' ')        
        coords = re.sub("[xyz=\n]","",coords)
        separate = lambda a:[int(a.split("..")[0]), int(a.split("..")[1])+1]

        xc,yc,zc = coords.split(',')
        x = separate(xc)
        y = separate(yc)
        z = separate(zc)

        c = Cube([x,y,z],mode)
        cubes.addCube(c)

print(cubes.countOn())

