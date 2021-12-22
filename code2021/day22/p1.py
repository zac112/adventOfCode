import re
from collections import defaultdict
import math

def cube(coords, minval=-math.inf, maxval=math.inf):
    coords = re.sub("[xyz=\n]","",coords)
    xc,yc,zc = coords.split(',')
    #print("".join(xc).split(".."))
    separate = lambda a:[int(a.split("..")[0]), int(a.split("..")[1])+1]
    #print(separate(xc))
    xrange = separate(xc)
    yrange = separate(yc)
    zrange = separate(zc)
    for r in [xrange,yrange,zrange]:
        if r[1] < minval or r[0] > maxval:
            r[:] = []
            return
        if r[0] < minval and r[1] > minval:
            r[0] = minval
        if r[1] > maxval and r[0] < maxval:
            r[1] = maxval+1

    print(xrange, yrange,zrange)
    for x in range(*xrange):        
        for y in range(*yrange):
            for z in range(*zrange):
                yield (x,y,z)
                
cubes = defaultdict(bool)
with open('data.txt') as f:
    for line in f.readlines():
        print(line)
        mode, coords = line.split(' ')
        for x,y,z in cube(coords,minval=-50,maxval=50):
            if mode=='on':
                cubes[(x,y,z)] = True
            else:
                cubes[(x,y,z)] = False

print(len([cube for cube,mode in cubes.items() if mode]))
