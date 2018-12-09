import sys
from collections import deque

#need moar recursions
sys.setrecursionlimit(6000)

data = []
with open("../../data/8.txt", "r") as f:    
    for line in f:
        #line = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        data[len(data):] = [int(x) for x in line.split(" ")]

tree = deque(data)
#nodes: list of triples: [([header], [metadata])]
nodes = []
##parses the value of the tree
##tree:deque of ints (the values), nodes: the resulting tree, children: how many children this level of recursion has
def parse_rec(tree, nodes, children):
    node = []
    nodes.append(node)
    
    #parse header
    children = tree.popleft()
    metadata_num = tree.popleft()
    node.append([children, metadata_num])

    for x in range(children):
        #parse nodes
        if children > 0:
            parse_rec(tree, nodes, children)
        
    #parse metadata
    metadata = []
    node.append(metadata)
    for i in range(metadata_num):
        metadata.append(tree.popleft())

##calculates the value of the tree's root node. i.e. the first node in the deque
##nodes:deque of nodes
def calculateValue_rec(nodes):
    value = 0

    if len(nodes) == 0: return 0
    node = nodes.popleft()
    numOfChildren = node[0][0]
    
    if(numOfChildren == 0):
        metadataSum = sum(node[1])
        value = metadataSum
    else:
        #calculate value of children
        nodeValues = {}        
        
        for child in range (numOfChildren):
            multiplier = 1            
            nodeValue = calculateValue_rec(nodes)
            nodeValues[child+1] = nodeValue

        metadata = [x for x in node[1] if x<=numOfChildren]
        #calculate the value of this node
        for child in metadata:
            value += nodeValues[child]
            
    return value
parse_rec(tree, nodes, 1)
value = calculateValue_rec(deque(nodes))

print (value)
