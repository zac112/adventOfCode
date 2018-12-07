import re

#commands a list of int-tuples (command, [startX, startY], [endX, endY])
#commands are
#0 turn off
#1 turn on
#2 toggle
commands = []
with open("../../data/6.txt", "r") as f:
    for line in f:
        split = line.split(" ")
        if line.startswith("turn on"):
            commands.append((1, [int(x) for x in split[2].split(",")], [int(x) for x in split[4].split(",")]))
        if line.startswith("turn off"):
            commands.append((0, [int(x) for x in split[2].split(",")], [int(x) for x in split[4].split(",")]))
        if line.startswith("toggle"):
            commands.append((2, [int(x) for x in split[1].split(",")], [int(x) for x in split[3].split(",")]))

lights = set([])

for command in commands:
    for x in range(command[1][0],command[2][0]+1):
        for y in range(command[1][1],command[2][1]+1):
            if command[0] == 1:
                lights.add((x,y))
            if command[0] == 0:
                lights.discard((x,y))
            if  command[0] == 2:
                if (x,y) in lights:
                    lights.discard((x,y))
                else:
                    lights.add((x,y))
print (len(lights))
