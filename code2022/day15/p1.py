import re
from collections import deque

def distance(x1,y1,x2,y2):
    return abs(abs(x2-x1)+abs(y2-y1))

def countRow(row, sensor,dist):
    positions = set()
    for x in range(sensor[0]-dist,sensor[0]+dist+1):
        if distance(*(x,row),*sensor) <= dist:
            positions.add((x,row))
    return positions

locations = {}
with open("data.txt") as f:
    for line in f:
        x1,y1,sx,sy = map(int,re.findall("(\d+)", line))
        locations[(x1,y1)] = (sx,sy)

row = 2000000
coveredArea = set()
for sensor, beacon in locations.items():
    print(sensor,beacon)
    coveredArea = coveredArea.union(countRow(row,sensor, distance(*sensor,*beacon)))

coveredArea = coveredArea.difference(locations.values())
print(len(coveredArea))
