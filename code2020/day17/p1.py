data="""###...#.
.##.####
.####.##
###.###.
.##.####
#.##..#.
##.####.
.####.#."""

##data = """.#.
##..#
#####"""
import itertools
state = {}
for x, line in enumerate(data.splitlines()):
    for y, cell in enumerate(line):
        if cell == "#":
            state[(x,y,0)]=1


neighbors = set(itertools.combinations_with_replacement([-1,1,0],3))

for x in list(neighbors):
    [neighbors.add(y) for y in itertools.permutations(x)]

print(neighbors)
def printBoard(state):
    minvals = (min(state, key=lambda a:a[0]),
               min(state, key=lambda a:a[1]),
               min(state, key=lambda a:a[2]))
    maxvals = (max(state, key=lambda a:a[0]),
               max(state, key=lambda a:a[1]),
               max(state, key=lambda a:a[2]))

    for z in range(minvals[2][2],maxvals[2][2]+1):
        print("z=",z)
        for x in range(minvals[0][0],maxvals[0][0]+1):
            for y in range(minvals[1][1],maxvals[1][1]+1):
                if (x,y,z) in state:
                    print("#",end="")
                else:
                    print(".",end="")
            print()
               
printBoard(state)
def countNeighbors(state,x,y,z):
    count = 0
    for n in neighbors:
        if n == (0,0,0):
            continue
        a,b,c = n        
        count += state.get((x+a,y+b,z+c), 0)
    return count

def setState(newState):
    pass

def generateState(state):
    newState = {}
    for x in state:
        for n in neighbors:
            a,b,c = n
            n1 = (x[0]+a,x[1]+b,x[2]+c)
            nb = countNeighbors(state,*n1)
            if nb == 3:
                newState[n1] = 1
            elif n1 in state and nb == 2:
                newState[n1] = 1
            
    return newState

turns = 6
for i in range(turns):
    state = generateState(state)
    #printBoard(state)
print(len(state))
