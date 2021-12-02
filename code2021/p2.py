with open('data.txt') as f:
    data = f.readlines()

directions = {'up':0,
              'down':0,
              'forward':0,
              'aim':0,
              'depth':0}

for x in data:
    d, num = x.split(" ")
    directions[d] += int(num)
    if d == 'forward':
        directions['depth'] += (directions['down']-directions['up'])*int(num)
        

print(directions['forward']*directions['depth'])
