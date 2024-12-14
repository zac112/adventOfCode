import re
from functools import reduce

robots = []
with open("data.txt") as f:
    for line in f.readlines():
        regex = "p=([-+]?\d+),([-+]?\d+) v=([-+]?\d+),([-+]?\d+)"
        robots.append(list(map(int,re.findall(regex,line)[0])))

x_size = 101
y_size = 103
        
quadrants = {True:{True:0,False:0},
             False:{True:0,False:0}}
time = 100
for r in robots:
    r[0] = (r[0]+r[2]*time)%x_size
    r[1] = (r[1]+r[3]*time)%y_size

    if r[0] == x_size//2 or r[1] == y_size//2:continue
    quadrants[r[0]<x_size//2][r[1]<y_size//2] += 1

safety = 1
for v in quadrants.values():
    print(v)
    safety *= reduce(lambda a,b: a*b, (v for v in v.values()),1)
print("Safety:",safety)

#P2
def draw(robots):    
    drawing = [[" " for x in range(x_size)] for y in range(y_size)]            
    for r in robots:
        drawing[r[1]][r[0]] = "x"
    [print("".join(line)) for line in drawing]

#these values came from manual inspection
next_x = 108
next_y = 156
while True:
    for r in robots:
        r[0] = (r[0]+r[2])%x_size
        r[1] = (r[1]+r[3])%y_size        
    time += 1
    
    #check positions manually:
    if time == next_x:
        next_x += x_size
        draw(robots)
        print(time)
        input()
    if time == next_y:
        next_y += y_size
        draw(robots)
        print(time)
        input()
    """
    if time == 8087: #solution
        draw(robots)
        input()
    """
