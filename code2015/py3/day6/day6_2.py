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

lights = {}
for command in commands:
    for x in range(command[1][0],command[2][0]+1):
        for y in range(command[1][1],command[2][1]+1):
            if (x,y) not in lights:
                lights[(x,y)] = 0
                
            if command[0] == 1:
                lights[(x,y)] += 1
            if command[0] == 0:
                lights[(x,y)] = max(lights[(x,y)]-1,0)
            if  command[0] == 2:
                lights[(x,y)] += 2
                
print (sum([lights[x] for x in lights]))
