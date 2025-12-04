with open('data.txt') as f:
    data = f.read().split("\n")

diagram = {}
for y, row in enumerate(data):
    for x, cell in enumerate(row):
        if cell == "@":
            diagram[(x,y)] = [(x+dx,y+dy)
                              for dx in range(-1,2)
                              for dy in range(-1,2)
                              if not dx==dy==0]

def findWithLessNeighbors(diagram, num):
    free = []
    for k, v in diagram.items():        
        neighbors = list(filter(lambda a: a in diagram, v))
        if len(neighbors) < num:
            free.append(k)
    return free


print("Part 1:",len(findWithLessNeighbors(diagram,4)))

removed = 0
while (neighbors := findWithLessNeighbors(diagram,4)):
    for n in neighbors:
        diagram.pop(n)
        removed += 1
        
print("Part 2:",removed)

