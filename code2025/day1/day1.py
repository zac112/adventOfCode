with open('data.txt') as f:
    lines = f.read().split("\n")
    data = list(map(lambda a:int(a.replace("R","").replace("L","-")), lines))

points = [50]
for x in data:
    points.append(points[-1]+x)
print("part 1:",list(map(lambda a:a%100, points)).count(0))

pointer = 50
passes = 0
for x in data:
    mult = -1 if x < 0 else 1
    for v in range(abs(x)):
        pointer = (pointer+mult)%100
        if pointer == 0:
            passes += 1
        
print("part 2:", passes)
