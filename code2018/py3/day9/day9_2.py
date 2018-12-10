
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = self
        self.prevval = self

class LinkedList:
    
    def __init__(self):
        self.headval = Node(0)
        self.currNode = self.headval

# Function to add node
    def add(self,newdata):

        NewNode = Node(newdata)
        node = self.currNode.prevval
        
        node.nextval.prevval = NewNode
        NewNode.nextval = node.nextval
        NewNode.prevval = node
        node.nextval = NewNode
        
        self.currNode = NewNode
        
    def forward(self, steps):
        for x in range(steps):
            self.currNode = self.currNode.nextval

    def backward(self, steps):
        for x in range(steps):
            self.currNode = self.currNode.prevval

    def removeCurrent(self):
        value = self.currNode.dataval

        self.currNode.prevval.nextval = self.currNode.nextval
        self.currNode.nextval.prevval = self.currNode.prevval
        self.currNode = self.currNode.nextval
        
        return value
        
# Print the linked list
    def listprint(self):
        val = str(self.headval.dataval)+", "
        start = self.headval
        printval = self.headval.nextval
        first = True
        while printval is not start:
            val += str(printval.dataval)+", "
            printval = printval.nextval
        return val
            
#puzzle input: 430 players; last marble is worth 71588 points
demoInput = False

if demoInput:
    players = 13
    marbles = 7999
else:
    players = 430
    marbles = 7158800

currentMarble = 0
board = LinkedList()
newMarblePos = 2
scoringMarble = 23

scores = {}

for marble in range(1, marbles+1):
    player = ((marble-1)%players)+1

    if marble % 100000 == 0:
        print ("Current marble:",marble)
    if marble > 1 and marble % scoringMarble == 0:
        turnScore = marble + scores.setdefault(player, 0)
        board.backward(7)
        removedMarble = board.removeCurrent()
        scores[player] = turnScore + removedMarble
        #print ("*[",player,"]",board.listprint(), "; scored",scores[player])
        continue

    board.forward(2)
    board.add(marble)
    #print ("[",player,"]",board.listprint())

tally = sorted([x for x in scores.items()], key=lambda a : a[1], reverse=True)
print(tally[0])
