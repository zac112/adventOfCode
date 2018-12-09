from collections import deque
data = []
with open("../../data/8.txt", "r") as f:    
    for line in f:
        #line = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        data[len(data):] = [int(x) for x in line.split(" ")]

tree = deque(data)
#nodes: list of triples: [([header], [metadata])]
nodes = []
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

parse_rec(tree, nodes, 1)
metadataSum = 0
for node in nodes:
    metadataSum += sum(node[1])


print (metadataSum)
