import re

with open('data.txt') as f:
    data = f.readlines()

target = {'red':12,'green': 13,'blue': 14}
both = "(\\d+) ([a-z]+)"
idsum = 0

for day in data:
    dayID, cubes = day.split(":")
    print(dayID)
    cubes = cubes.split(";")
    dayOK = True

    for configuration in cubes:            
        for num, color in re.findall(both,configuration):                
            if target[color]<int(num):
                dayOK = False
    if dayOK:
        ID = int(dayID.split(" ")[1])
        print(ID)
        idsum += ID

print(idsum)