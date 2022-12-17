import re
from collections import deque

def distance(x1,y1,x2,y2):
    return abs(abs(x2-x1)+abs(y2-y1))

def walkPerimeter(sensor, dist):
    pos = list(sensor)
    while distance(*pos,*sensor)<dist:
        pos[1] += 1

    while abs(pos[1]-sensor[1])>0:
        yield pos
        pos[0] -= 1
        pos[1] -= 1

    while abs(pos[0]-sensor[0])>0:
        yield pos
        pos[0] += 1
        pos[1] -= 1

    while abs(pos[1]-sensor[1])>0:
        yield pos
        pos[0] += 1
        pos[1] += 1

    while abs(pos[0]-sensor[0])>0:
        yield pos
        pos[0] -= 1
        pos[1] += 1
        
locations = {}
with open("data.txt") as f:
    for line in f:
        x1,y1,sx,sy = map(int,re.findall("(\d+)", line))
        locations[(x1,y1)] = (sx,sy)

rangemax = 4000000
for sensor, beacon in locations.items():
    print(sensor,beacon)
    """
This monstrosity could possibly be further optimized by only considering
the intersections of the perimeters instead of the whole perimeter.
    """
    for x,y in walkPerimeter(sensor,distance(*sensor,*beacon)):
        neighbors = [(-1,0),(0,1),(1,0),(0,-1)]
        for a,b in [(x+a,y+b) for a,b in neighbors]:
            if a <0 or b < 0:continue
            if a > rangemax or b > rangemax:continue
            in_area = 0
            for sensor, beacon in locations.items():
                sensorDist = distance(*sensor,*beacon)
                d = distance(*sensor,*(a,b))
                if d < sensorDist:
                    inarea += 1
                    break
            if in_area == 0:
                print((a,b))
