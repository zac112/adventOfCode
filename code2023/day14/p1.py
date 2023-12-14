with open('data.txt') as f:
    data = f.read().splitlines()
    pass

rocks = set((x,-1) for x in range(len(data[0])))
balls = set()
for y, line in enumerate(data):
    for x,c in enumerate(line):
        if c == 'O': balls.add((x,y))
        if c == '#': rocks.add((x,y))

movedBalls = set(rocks)
totalDistance = 0
for ballX, ballY in sorted(balls,key=lambda a:a[1]):
    newY = max(y for x,y in movedBalls if y < ballY and x==ballX)+1
    movedBalls.add((ballX,newY))
    distance = len(data)-newY
    totalDistance += distance
    
print(totalDistance)
