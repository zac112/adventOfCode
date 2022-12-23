import re
from itertools import zip_longest

def moves(text):
    steps = re.findall("\d+",text)
    turns = re.findall("\D+",text)
    for s,t in zip(steps,turns):
        yield int(s),t

def execute(moveFuncs):
    def doMove(pos, d, times):
        for _ in range(times):
            pos = move(moveFuncs, d, pos)
        return pos
                    
    def inner (instruction, pos, direction):
        match instruction:        
            case int(x),"L":
                pos = doMove(pos,direction,x)
                newDir = (direction-1+len(moveFuncs))%len(moveFuncs)                
                return pos,newDir
            
            case int(x),"R":
                pos = doMove(pos,direction,x)
                newDir = (direction+1+len(moveFuncs))%len(moveFuncs)                
                return pos,newDir
            
            case int(x),None:
                pos = doMove(pos,direction,x)
                return pos,direction
    return inner
        
def move(moveFuncs, direction, pos):
    def wraparound(startpos):
        newPos = pos
        oppositeDir = (direction+2)%len(moveFuncs)
        while get(moveFuncs[oppositeDir](newPos)) != " ":
            newPos = moveFuncs[oppositeDir](newPos)
        match get(newPos):
            case "#":
                return startpos
            case ".":
                return newPos
            case _:
                raise Exception
    
    newPos = moveFuncs[direction](pos)
    match get(newPos):
        case ".":
            return newPos
        case " ":            
            return wraparound(pos)
        case "#":
            return pos
        case _:
            raise Exception("Unknown tile")


with open("data.txt") as f:    
    *maze,instructions = f.read().splitlines()
    maxwidth = max([len(l) for l in maze])
    maze = [" "+"".ljust(maxwidth+1)]+[" "+l.ljust(maxwidth+1," ") for l in maze]
    start = len(maze[1])+maze[1].index(".")
    print(start)

itoxy = (lambda maze:lambda i: (i//len(maze[0]),i%len(maze[0])))(maze)
xytoi = (lambda maze:lambda row,col:row*len(maze)+col*len(maze[0]))(maze)
get = (lambda maze:lambda i:maze[itoxy(i)[0]][itoxy(i)[1]])(maze)
right = (lambda maze:lambda i:i+1)(maze)
down = (lambda maze:lambda i:i+len(maze[0]))(maze)
left = (lambda maze:lambda i:i-1)(maze)
up = (lambda maze:lambda i:i-len(maze[0]))(maze)
movements = [right,down,left,up]
execute =  execute(movements)

pos = start
direction = 0
print(pos)
for i in moves(instructions):
    #print(i)
    pos,direction = execute(i, pos, direction)
    #print(itoxy(pos), direction)
    
print(itoxy(pos), direction)
row,col = itoxy(pos)
print("result",row*1000+col*4+direction)
