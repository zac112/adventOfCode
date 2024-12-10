with open('data.txt') as f:
    data = f.read()
    graph = [[-1]+[int(c) for c in line]+[-1] for line in data.split("\n")]
graph.append([-1]*len(graph[0]))
graph.insert(0,[-1]*len(graph[0]))

def DFS(x,y, steps):
    curr = graph[y][x]
        
    if curr == -1: return 0
    if steps[-1][2]+1 != curr: return 0
    if curr == 9 :
        peaks.add((x,y))
        return 1

    res = 0
    res += DFS(x+1,y,steps+[(x,y,curr)])
    res += DFS(x-1,y,steps+[(x,y,curr)])
    res += DFS(x,y+1,steps+[(x,y,curr)])
    res += DFS(x,y-1,steps+[(x,y,curr)])
    return res


P1_trails = 0
P2_rating = 0
for y, line in enumerate(graph):
    for x, c in enumerate(line):
        if c != 0: continue
        peaks = set()
        P2_rating += DFS(x,y,[(x,y,-1)])
        P1_trails += len(peaks)
print("P1",P1_trails)
print("P2",P2_rating)
