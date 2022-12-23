import re
from itertools import zip_longest

def moves(text):
    steps = re.findall("\d+",text)
    turns = re.findall("\D+",text)
    for s,t in zip_longest(steps,turns):
        yield int(s),t

player = {0:'>',
          1:'v',
          2:'<',
          3:'^'}
movenum = 0
def execute(moveFuncs):
    def doMove(pos, d, times):
        for _ in range(times):
            global movenum
            pos,d = move(moveFuncs, d, pos)
            if movenum < 10000:
                x,y = itoxy(pos)
                screen[x][y] = player[d]
            movenum += 1
            #print("Moved to",itoxy(pos), get(pos))
        return pos,d
                    
    def inner (instruction, pos, direction):
        match instruction:        
            case int(x),"L":
                pos, direction = doMove(pos,direction,x)
                newDir = (direction-1+len(moveFuncs))%len(moveFuncs)                
                return pos,newDir
            
            case int(x),"R":
                pos, direction = doMove(pos,direction,x)
                newDir = (direction+1+len(moveFuncs))%len(moveFuncs)                
                return pos,newDir
            
            case int(x),None:
                pos, direction = doMove(pos,direction,x)
                return pos,direction
    return inner
        
def move(moveFuncs, direction, pos):
    def wraparound(startpos,d):
        try:
            newPos,rot = transitions[(startpos,d)]
        except KeyError:
            #print(f"Failed transition from {itoxy(startpos)} {d}")
            exit()
        match get(newPos):
            case "#":
                #print(f"Blocked warp from {itoxy(startpos)} to {itoxy(newPos)} with rotation {d}>{(d+rot)%len(moveFuncs)}")
                return startpos, d
            case ".":
                #print(f"warped from {itoxy(startpos)} to {itoxy(newPos)} with rotation {d}>{(d+rot)%len(moveFuncs)}")
                return newPos, (d+rot+len(moveFuncs))%len(moveFuncs)
            case _:
                raise Exception("Unknown:",get(newPos))
    
    newPos = moveFuncs[direction](pos)
    #print("Trying to move to direction",direction,itoxy(newPos),get(newPos))
    match get(newPos):
        case ".":
            #print(f"Moved from {itoxy(pos)} to {itoxy(newPos)};{direction}")
            return newPos, direction
        case " ":            
            return wraparound(pos,direction)
        case "#":
            return pos, direction
        case _:
            raise Exception("Unknown tile")


test = ('data1.txt',4)
real = ('data.txt',50)
file,sidewidth = real
with open(file) as f:    
    *maze,instructions = f.read().splitlines()
    maxwidth = max([len(l) for l in maze])
    maze = [" "*(maxwidth+2)] + [" "+l.ljust(maxwidth+1," ") for l in maze]
    screen = [list(l) for l in maze]    
    start = len(maze[1])+maze[1].index(".")
    
transpose = lambda maze:[list(l) for l in zip(*maze)]
rotateCCW = lambda maze:transpose([l[::-1] for l in maze])
rotateCW = lambda maze:transpose([l for l in maze[::-1]])

itoxy = (lambda maze:lambda i: (i//len(maze[0]),i%len(maze[0])))(maze)
xytoi = (lambda maze:lambda row,col:row*len(maze[0])+col)(maze)
get = (lambda maze:lambda i:maze[itoxy(i)[0]][itoxy(i)[1]])(maze)
right= (lambda maze:lambda i:i+1)(maze)
down = (lambda maze:lambda i:i+len(maze[0]))(maze)
left = (lambda maze:lambda i:i-1)(maze)
up =   (lambda maze:lambda i:i-len(maze[0]))(maze)
movements = [right,down,left,up]
execute =  execute(movements)

def connectEdges(transitions,e1,r1,d1,e2,r2,d2):
    for a,b in zip(e1,e2):
        if a in transitions:
            raise Exception(a)
        if b in transitions:
            raise Exception(b)
        transitions[(a,d1)] = (b,r1)
        transitions[(b,d2)] = (a,r2)
        
def getEdge(i,movement):
    res = []
    for x in range(sidewidth):        
        res.append(i)
        i = movement(i)
    return res
    
corners = []
for y in range(4):    
    for x in range(4):
        piece = []
        corners.append(piece)
        piece.append((y*sidewidth+1,x*sidewidth+1))
        piece.append((y*sidewidth+sidewidth,x*sidewidth+1))        
        piece.append((y*sidewidth+1,x*sidewidth+sidewidth))
        piece.append((y*sidewidth+sidewidth,x*sidewidth+sidewidth))      
transitions={}
if file=="data.txt":
    p=1
    topleft_1 = corners[p][0]
    bottomleft_1 = corners[p][1]
    topright_1 = corners[p][2]
    bottomright_1 = corners[p][3]
    p=2
    topleft_2 = corners[p][0]
    bottomleft_2 = corners[p][1]
    topright_2 = corners[p][2]
    bottomright_2 = corners[p][3]
    p=5
    topleft_3 = corners[p][0]
    bottomleft_3 = corners[p][1]
    topright_3 = corners[p][2]
    bottomright_3 = corners[p][3]
    p=8
    topleft_4 = corners[p][0]
    bottomleft_4 = corners[p][1]
    topright_4 = corners[p][2]
    bottomright_4 = corners[p][3]
    p=9
    topleft_5 = corners[p][0]
    bottomleft_5 = corners[p][1]
    topright_5 = corners[p][2]
    bottomright_5 = corners[p][3]
    p=12
    topleft_6 = corners[p][0]
    bottomleft_6 = corners[p][1]
    topright_6 = corners[p][2]
    bottomright_6 = corners[p][3]

    #real data
    #1-4 
    connectEdges(transitions,getEdge(xytoi(*bottomleft_1),up),-2,2, getEdge(xytoi(*topleft_4),down),-2,2)
    #1-6 
    connectEdges(transitions,getEdge(xytoi(*topleft_1),right),1,3, getEdge(xytoi(*topleft_6),down),-1,2)
    #2-6 
    connectEdges(transitions,getEdge(xytoi(*topleft_2),right),0,3, getEdge(xytoi(*bottomleft_6),right),0,1)
    #3-4
    connectEdges(transitions,getEdge(xytoi(*bottomleft_3),up),-1,2, getEdge(xytoi(*topright_4),left),1,3)    
    #2-5 
    connectEdges(transitions,getEdge(xytoi(*topright_2),down),-2,0, getEdge(xytoi(*bottomright_5),up),-2,0)
    #2-3 
    connectEdges(transitions,getEdge(xytoi(*bottomleft_2),right),1,1, getEdge(xytoi(*topright_3),down),-1,0)
    #5-6 
    connectEdges(transitions,getEdge(xytoi(*bottomleft_5),right),1,1, getEdge(xytoi(*topright_6),down),-1,0)

else:
    #test data
    topleft_1 = corners[2][0]
    bottomleft_1 = corners[2][1]
    topright_1 = corners[2][2]
    bottomright_1 = corners[2][3]
    p=4
    topleft_2 = corners[p][0]
    bottomleft_2 = corners[p][1]
    topright_2 = corners[p][2]
    bottomright_2 = corners[p][3]
    p=5
    topleft_3 = corners[p][0]
    bottomleft_3 = corners[p][1]
    topright_3 = corners[p][2]
    bottomright_3 = corners[p][3]
    p=6
    topleft_4 = corners[p][0]
    bottomleft_4 = corners[p][1]
    topright_4 = corners[p][2]
    bottomright_4 = corners[p][3]
    p=10
    topleft_5 = corners[p][0]
    bottomleft_5 = corners[p][1]
    topright_5 = corners[p][2]
    bottomright_5 = corners[p][3]
    p=11
    topleft_6 = corners[p][0]
    bottomleft_6 = corners[p][1]
    topright_6 = corners[p][2]
    bottomright_6 = corners[p][3]

    #[right,down,left,up]
    #1-2
    connectEdges(transitions,getEdge(xytoi(*topleft_1),right),-2, getEdge(xytoi(*topright_2),left),2)
    #1-3
    connectEdges(transitions,getEdge(xytoi(*topleft_1),down),-1, getEdge(xytoi(*topleft_3),right),1)
    #1-6
    connectEdges(transitions,getEdge(xytoi(*topright_1),down),-2, getEdge(xytoi(*bottomright_6),up),2)
    #2-5
    connectEdges(transitions,getEdge(xytoi(*bottomleft_2),right),2, getEdge(xytoi(*bottomright_5),left),2)
    #2-6
    connectEdges(transitions,getEdge(xytoi(*topleft_2),down),1, getEdge(xytoi(*bottomright_6),left),-1)
    #3-5
    connectEdges(transitions,getEdge(xytoi(*bottomright_3),left),-1, getEdge(xytoi(*topleft_5),down),1)
    #4-6
    connectEdges(transitions,getEdge(xytoi(*topright_4),down),1, getEdge(xytoi(*topright_6),left),-1)


pos = xytoi(*topleft_1)
direction = 0
for i in moves(instructions):
    #print(i)
    pos,direction = execute(i, pos, direction)    
    #print(pos,itoxy(pos), direction, get(pos))

print("Final:",itoxy(pos), direction)
row,col = itoxy(pos)
print("result",row*1000 + col*4 + direction)
