def findReflection(pattern):
    countDefects = lambda a,b:len([x for x,y in zip(a,b) if x!=y])
    reflections = []
    for colA, _ in enumerate(pattern[:-1]):
        line, nextLine = pattern[colA], pattern[colA+1]
        if line == nextLine or countDefects(line,nextLine):
            reflections.append([colA,colA+1,0])

    for point in reflections:
        defects = point[-1]
        colA, colB = point[:2]        
        while colA > -1 and colB < len(pattern):            
            defects += countDefects(pattern[colA],pattern[colB])
            colA -= 1
            colB += 1
        point[-1] = defects
        
    return reflections

with open('data.txt') as f:
    data = f.read().split("\n\n")
    for i, pattern in enumerate(data):
        data[i] = pattern.splitlines()
    
points = 0
for pattern in data:
    reflectionPoints = findReflection(pattern)
    points += sum(100*r[1] for r in reflectionPoints if r[-1]==1)
    
    reflectionPoints = findReflection(list(zip(*pattern)))
    points += sum(r[1] for r in reflectionPoints if r[-1]==1)
    
print(points)