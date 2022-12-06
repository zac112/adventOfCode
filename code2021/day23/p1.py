from collections import defaultdict, namedtuple, deque
from copy import deepcopy
from math import inf
import sys
sys.setrecursionlimit(5000)

class Creature:
    def __init__(self,symbol):
        self.symbol = symbol
        self.visited = []

    def scoreMulti(self):
         return 10**'ABCD'.index(self.symbol.upper())

    def getSymbol(self):
        return self.symbol.upper()

    def canStopIn(self, node):
        return not node.isDoor()\
               and not node.creature \
               and (not node.roomFor or node.roomFor == self.getSymbol())
    
    def __eq__(self, other):
        return self.symbol == other.symbol

    def __hash__(self):
        return hash(self.symbol)
    
    def __repr__(self):
        return f"{self.symbol}"
    
creatures = {'A':[Creature('A'),Creature('a')],
             'B':[Creature('B'),Creature('b')],
             'C':[Creature('C'),Creature('c')],
             'D':[Creature('D'),Creature('d')]}
class Node:

    def __init__(self,pos, creature, roomFor=None, canStop=False):
        self.pos = pos
        self.neighbors = [] 
        self.roomFor = roomFor
        self.creature = creatures[creature].pop() if creature in 'ABCD' else None
        self.canStop = canStop

    def setCreature(self, c=None):
        self.creature = c
        
    def scoreMultiplier(self):
        if self.creature:
            return self.creature.scoreMulti()
        return 0

    def solved(self):
        if self.creature:
            return self.creature.symbol.upper() == self.roomFor
        return True

    def isDoor(self):
        return self.pos in [point(3,1),point(5,1),point(7,1),point(9,1)]
    def canSkip(self):
        return (self.solved() and self.pos[1]==3)
    
    def __eq__(self,other):
        if other is None:
            return False
        return self.pos==other.pos

    def __hash__(self):
        return hash(self.pos)

    def __repr__(self):
        #return f"{self.pos}->{self.neighbors}: {self.creature} (For {self.roomFor}))"
        return f"{self.pos}: {self.creature} (For {self.roomFor}))"
    
point = namedtuple('Point',['x','y'])
pathnode = namedtuple("PathNode",['current','previous'])
rooms = {(3,2):"A",(3,3):"A",
         (5,2):"B",(5,3):"B",
         (7,2):"C",(7,3):"C",
         (9,2):"D",(9,3):"D"}

coords = []
with open('data_test1.txt') as f:
    for y,line in enumerate(f.readlines()):
        for x, cell in enumerate(line):
            if cell not in 'ABCD.': continue
            n = Node(point(x,y),
                     cell,
                     rooms.get((x,y),None),
                     canStop=(x,y) not in [point(3,1),point(5,1),point(7,1),point(9,1)])
            coords.append(n)

def getNeighbors(node):
    x,y = node.pos.x,node.pos.y
    return [(x+1,y),
            (x-1,y),
            (x,y+1),
            (x,y-1)]

def printNodes(maze):
    lines = []
    for y in range(5):
        line = []
        for x in range(13):
            node = maze.get((x,y),None)
            if not node:
                line.append("#")
                continue
            if node.creature:
                line.append(node.creature.symbol)
            else:
                line.append('.')
        lines.append("".join(line)+"\n")
    return "".join(lines)

def checkMaze():
    return all([n.solved() for n in coords])

def floodfill(startnode):
    available = []
    queue = [pathnode(startnode,None)]
    visited = set()
    mustEndInRoom = startnode.pos.y == 1 #not in rooms
    n = None
    creature = startnode.creature
    #print("startnode;",startnode)
    while queue:
        #print("in queue:",[x.current.pos for x in queue])
        currentNode = queue.pop()
        n,prev = currentNode
        #print("current:",n)
        
        
        if n in visited:
            #print('already visited',n)
            continue
        visited.add(n)
        
        if n != startnode:
            if n.creature is not None: continue
            if n.roomFor and n.roomFor != creature.getSymbol():continue

        #print("Extending:",n.neighbors)
        queue.extend([pathnode(x,n) for x in n.neighbors]) 

        if n == startnode: continue
        available.append(currentNode)

    #print("Available",available)
    return available

def backtrack(availableNodes,start):
    try:
        #print(availableNodes, start)
        prevNode = [x.previous for x in availableNodes if x.current == start][0]
    except Exception as e:
        return []

    result = [start]+backtrack(availableNodes,prevNode)
    return result

    
cache = set()
bestScore = [inf]
i = [0]
def solve(nodes, score):
    #print(printNodes(nodes))
    #printNodes(nodes)
    #print("Score now:",score)
        
    queue = deque()
    queue.append((nodes,0))
    while queue:        
        nodes,score = queue.popleft()
        #state = hash(printNodes(nodes))
        #if state in cache:
        #    continue
        #cache.add(state)
        if len(queue) %100 == 0:
            print(len(queue),score)
            print(printNodes(nodes))
        creatures = [node for pos,node in nodes.items() if node.creature]
        for creatureNode in creatures:
            currCreature = creatureNode.creature        
            if creatureNode.canSkip():
                if creatureNode.creature.symbol not in 'aC':
                    print(printNodes(nodes))
                continue
            
            availableNodes = floodfill(creatureNode)
            #print("availableNodes:",[x.current.pos for x in availableNodes if x.current.pos not in currCreature.visited])
            for available in availableNodes:
                current = available.current
                if current.pos in currCreature.visited:
                    continue
                if current.isDoor(): continue
                if creatureNode.pos.y==1 and current.pos.y==1:
                    continue
                #print("Current node:",available.current.pos)
                path = backtrack(availableNodes, current)
                scoreadd = len(path)+1
                #print([x.pos for x in path])
                newScore = scoreadd*creatureNode.scoreMultiplier()+score

                if newScore >= bestScore[0]:
                    print("score too high")
                    continue
                
                if checkMaze() and newScore < bestScore[0]:
                    bestScore[0] = newScore
                    print("Got score",newScore)
                    continue
                
                newState = deepcopy(nodes)
                newCreature = newState[creatureNode.pos].creature
                newCreature.visited.append(current.pos)
                
                newState[creatureNode.pos].setCreature()
                newState[current.pos].setCreature(newCreature)
                
                #i[0] += 1
                #if i[0]%1 == 1000:
                #    print(printNodes(newState))
                queue.append((newState, score+newScore))

            
nodes = {}
for node in coords:
    neighbors = [x for x in coords if x.pos in getNeighbors(node)]
    nodes.setdefault(node.pos,node).neighbors.extend(neighbors)

print(nodes[(3,2)].neighbors)
print()
print(printNodes(nodes))
print(checkMaze())
solve(nodes,0)
#print("3,2 neighbors",nodes[(3,2)].neighbors)
#print(floodfill(nodes[(3,2)]))
