with open("data.txt") as f:
    trees = f.read().splitlines()

trees = [[[int(x),False] for x in line] for line in trees]

def count(trees, transpose=False):
    if transpose:
        trees = list(zip(*trees))

    for tree in trees[0]+trees[-1]:
        tree[1] = True
    
    for y,row in enumerate(trees[1:-1],1):
        tallest,seen = row[0]
        for x,(tree,seen) in enumerate(row[1:-1],1):
            if tree > tallest:
                trees[y][x][1] = True
                tallest = tree

def look(trees,startTree,row,col, direction):
    if row < 0 or col < 0:
        return 0
    try:
        tree = trees[row][col][0]
    except:
        return 0
    if tree >= startTree:
        return 1

    r,c = direction
    return 1 + look(trees,startTree,row+r,col+c, direction)

def scenicScore(trees,row,col):
    score = look(trees, trees[row][col][0],  row, col+1, (0,1) )
    score *= look(trees, trees[row][col][0], row, col-1, (0,-1) )
    score *= look(trees, trees[row][col][0], row+1, col, (1,0) )
    score *= look(trees, trees[row][col][0], row-1, col, (-1,0) )
    return score
    
count(trees)
count([line[::-1] for line in trees])
count(trees, True)
count(trees[::-1], True)

scores = []    
for r,row in enumerate(trees):
    for c,(tree,seen) in enumerate(row):
        if seen:
            scores.append(scenicScore(trees, r,c))

print(max(scores))        

