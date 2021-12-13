dots = set()
folds = []
with open('data.txt') as file:
    for line in file.readlines():
        line = line.strip()
        if not line:
            continue
        if ',' in line:
            dots.add(line)
        else:
            folds.append(line.split(" ")[-1])

print(folds, dots)

dots = set([(int(x),int(y)) for x,y in map(lambda a:a.split(','),dots)])
maxX = max(dots, key=lambda a:a[0])[0]
maxY = max(dots, key=lambda a:a[1])[1]

print(maxX,maxY)

for fold in folds:
    axis, pos = fold.split('=')
    pos = int(pos)

    print('folding',axis,pos)
    newdots = set()
    for dot in dots:
        if axis =='x':
            if dot[0]>pos:
                newpos = pos-(dot[0]-pos)
                newdots.add((newpos,dot[1]))
            else:
                newdots.add(dot)
        if axis == 'y':
            if dot[1]>pos:
                newpos = pos-(dot[1]-pos)
                newdots.add((dot[0],newpos))
            else:
                newdots.add(dot)
    dots = newdots

maxX = max(dots, key=lambda a:a[0])[0]
maxY = max(dots, key=lambda a:a[1])[1]

for x in range(maxY+1):
    for y in range(maxX+1):
        if (y,x) in dots:
            print("x",end='')
        else:
            print(".",end='')
    print()
