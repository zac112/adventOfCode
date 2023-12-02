import re
import operator
from functools import reduce

with open('data.txt') as f:
    data = f.readlines()

target = {'red':12,'green': 13,'blue': 14}
both = "(\\d+) ([a-z]+)"
idsum = 0

for day in data:
    dayID, cubes = day.split(":")
    cubes = cubes.split(";")
    
    maxCubes = {}
    for configuration in cubes:            
        for num, color in re.findall(both,configuration):                
            maxCubes[color] = max(maxCubes.get(color,int(num)), int(num))
            
    power = reduce(operator.mul, maxCubes.values(), 1)
    idsum += power

print(idsum)