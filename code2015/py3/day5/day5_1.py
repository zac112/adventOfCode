import re

lines = []
with open("../../data/5.txt", "r") as f:
    for line in f:
        lines.append(line)

niceLines = 0
for line in lines:
    if line.count("ab")+line.count("cd")+line.count("pq")+line.count("xy") > 0:
        continue
    if(line.count("a")+line.count("e")+line.count("i")+line.count("o")+line.count("u") < 3):
        continue

    for x in range(len(line)-1):
        if line[x] == line[x+1]:
            niceLines += 1
            break

print (niceLines)
