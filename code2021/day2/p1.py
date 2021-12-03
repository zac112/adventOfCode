with open('data.txt') as f:
    data = f.readlines()

directions = {'up':0,
              'down':0,
              'forward':0}

for x in data:
    d, num = x.split(" ")
    directions[d] += int(num)

print(directions['forward']*(directions['down']-directions['up']))