with open('data.txt') as file:
    edges = [x.strip().split('-') for x in  file.readlines()]
    graph = {}
    for node1,node2 in edges:
        graph.setdefault(node1,[]).append(node2)
        graph.setdefault(node2,[]).append(node1)

print(graph)
def doubleEntry(path, x):
    return len([i for i in path+[x] if ((path).count(i)==2 and i.islower())])>0

def DFS(startnode, endnode, paths, path=["start"]):    
    for x in graph[startnode]:
        if x in path and x.islower():
            if doubleEntry(path,x) or x in ['start','end']:
                continue
        if x == "end":
            paths[0] += 1
            continue
        
        DFS(x,endnode,paths, path+[x] )

    return

paths = [0]
DFS("start","end",paths)
print(paths)

