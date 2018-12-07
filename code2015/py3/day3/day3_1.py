instructions = ""
with open("../../data/3.txt", "r") as f:
    instructions = f.readline()

xPos = 0
yPos = 0
visitedLocations = set([(0,0)])

for c in instructions:
    if c == "<":
        xPos -= 1
    if c == "^":
        yPos += 1
    if c == "v":
        yPos -= 1
    if c == ">":
        xPos += 1
    visitedLocations.add((xPos,yPos))
print (len(visitedLocations))
