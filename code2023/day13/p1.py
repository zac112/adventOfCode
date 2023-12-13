def findReflection(pattern):
    reflections = []
    for colA, lineA in enumerate(pattern[:-1]): 
        if pattern[colA] == pattern[colA+1]:
            reflections.append([colA,colA+1,0])

    for point in reflections:
        isPerfect = False
        colA, colB = point[:2]
        while pattern[colA]==pattern[colB]:
            point[2] += 1
            colA -= 1
            colB += 1
            if colA == -1 or colB == len(pattern): 
                isPerfect = True
                break
        point.append(isPerfect)
        
    return reflections

with open('data.txt') as f:
    data = f.read().split("\n\n")
    for i, pattern in enumerate(data):
        data[i] = pattern.splitlines()
    
points = 0
for pattern in data:
    reflection = findReflection(pattern)
    for r in reflection:
        if r[-1]:
            points += 100*r[1]
    
    reflection = findReflection(list(zip(*pattern)))
    for r in reflection:
        if r[-1]:
            points += r[1]
print(points)