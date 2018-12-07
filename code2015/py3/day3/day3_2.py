instructions = ""
with open("../../data/3.txt", "r") as f:
    instructions = f.readline()

instructions = "^>v<"
#0 santa
#1 robo
positions = [(0,0), (0,0)]
visitedLocations = set([(0,0)])

turn = 0
for c in instructions:
    if c == "<":
        positions[turn] = (positions[turn][0] - 1, positions[turn][1])
    if c == "^":
        positions[turn] = (positions[turn][0], positions[turn][1] + 1)
    if c == "v":
        positions[turn] = (positions[turn][0], positions[turn][1] - 1)
    if c == ">":
        positions[turn] = (positions[turn][0] + 1, positions[turn][1])
    visitedLocations.add(positions[turn])
    turn = (turn+1)%2

print (len(visitedLocations))
