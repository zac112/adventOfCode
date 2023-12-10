from collections import deque

def determineStart(start, coords):    
    x,y = start
    left, up, right, down  = [coords.get((x+dx,y+dy),'.') 
                              for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]]
    
    if left in '-FL' and right in '-7J': return '-'
    if left in '-FL' and up in '|7J'   : return 'J'
    if left in '-FL' and down in '|LJ' : return '7'

    if up in '|7F' and down in '|JL'   : return '|'
    if up in '|7F' and left in '-FL'   : return 'J'
    if up in '|7F' and right in '-7J'  : return 'L'

    if right in '-7J' and down in '|JL': return 'F'
    raise Exception("Part not found")

with open('data.txt') as f:
    data = f.read()
    start = data.replace("\n","").index("S")
    data = data.splitlines()
    start = (start%len(data[0]), start//len(data[0]))

coords = {(x,y):c for y, line in enumerate(data) for x,c in enumerate(line)}
coords[start] = determineStart(start, coords)

visited = set()
queue = deque([(*start,0)])
while queue:
    coordx, coordy, dist = queue.popleft()
    makeCoord = lambda dx,dy:(coordx+dx,coordy+dy,dist+1)

    if (coordx, coordy) in visited: continue
    match coords.get((coordx,coordy),0):
        case "L": queue.extend([makeCoord(0,-1), makeCoord(+1,0)])
        case "J": queue.extend([makeCoord(0,-1), makeCoord(-1,0)])
        case "7": queue.extend([makeCoord(0,+1), makeCoord(-1,0)])
        case "F": queue.extend([makeCoord(0,+1), makeCoord(+1,0)])
        case "|": queue.extend([makeCoord(0,-1), makeCoord(0,+1)])
        case "-": queue.extend([makeCoord(-1,0), makeCoord(+1,0)])
        case _: continue
    visited.add((coordx,coordy))

print("Part 1:",dist-1)

def raycast(coord, dist, cuts):
    x,y = coord
    if x < 0 or y < 0: return cuts
    if coord in visited:
        cuts +=1
        if coords[coord] in "L7": cuts +=1
    return raycast( (x-1,y-1), dist+1, cuts)

inside = 0
for y,line in enumerate(data):
    for x, cell in enumerate(line):
        if (x,y) in visited: continue
        if raycast((x,y),0,0)%2==1: inside += 1                

print("Part 2:",inside)

