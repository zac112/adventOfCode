with open('data.txt') as f:
    data = f.read()
    diagram = data.split("\n")
    splitters = {}
    for y,row in enumerate(diagram):
        items = []
        for x, cell in enumerate(row):
            if cell=="^":
                items.append((x,y))
            if cell=="S":
                start = (x,y)
        splitters[y] = items

hitSplitters = {}
beam = [start]

while beam:
    x, y = beam.pop(0)    
    try:
        while (x,y) not in splitters[y]: y += 1
    except KeyError: continue
    
    hitSplitters.setdefault(y,set()).add(x)
    
    if (x-1,y) not in beam: beam.append((x-1,y))
    if (x+1,y) not in beam: beam.append((x+1,y))
    

print("Part 1:",sum(map(len,hitSplitters.values())))

pascalTriangle = [0]*len(diagram[0])
pascalTriangle[len(pascalTriangle)//2]=1

y=0
while y<=max(hitSplitters):
    y += 1
    if y in hitSplitters:
        for i, val in enumerate(pascalTriangle):
            if val>0 and i in hitSplitters[y]:
                pascalTriangle[i-1]+= pascalTriangle[i]
                pascalTriangle[i+1]+= pascalTriangle[i]
                pascalTriangle[i]   = 0

print("Part 2:",sum(pascalTriangle))
