with open("data.txt") as f:
    trees = f.read().splitlines()

trees = [[[int(x),False] for x in line] for line in trees]
seen = set()

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

count(trees)
count([line[::-1] for line in trees])
count(trees, True)
count(trees[::-1], True)

print(str(trees).count("True"))
        
