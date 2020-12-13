MAX = 6504
maze = ""
with open("../../day18.txt", "r") as f:
    maze = f.readlines()

maze = [a.replace("\n","") for a in maze]
[print(m) for m in maze]

def BFS(maze, start, end, path, visited):
    if start in visited:
        return False
    queue = []    
    visited.add(start)
    if start == end:
        return True

    if maze[start[0]][start[1]] != ".":
        return False

    path.append( start )    
    queue.append( (start[0]-1,start[1]) )
    queue.append( (start[0]+1,start[1]) )
    queue.append( (start[0],start[1]-1) )
    queue.append( (start[0],start[1]+1) )

    while(queue):
        node = queue.pop(0)
        if(BFS(maze, node, end, path, visited)):
            return True
        
    path.pop()        
    return False
    
def findLocs(maze):
    result = {}
    #for c in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@":
    for c in "qwertyuiopasdfghjklzxcvbnm@":
        for y,row in enumerate(maze):
            for x,char in enumerate(row):
                if char == c:
                    result[c] = (y,x)
    return result

def findAvailableKeys(maze, start, locs):
    #maze, start, end, depth, maxDepth, path, visited
    #print("Available locs in findkeys:",locs)
    keys = []
    for key in locs.keys():
        path = []
        if BFS(maze, start, locs[key], path, set()):
            #print("From",start,"found",key)
            keys.append(key)
    return keys

def solve(maze):
    locs = findLocs(maze)
    start = locs["@"]
    del locs["@"]
    maze = [a.replace("@",".") for a in maze]
    allKeys = set(filter(lambda a:a in "qwertyuiopasdfghjklzxcvbnm", locs.keys()))    

    #print(start)
    global counter
    counter = 0
    orderings = []
    def solveRec(maze, start, endKey, path, locs, keys, result):

        global best
        newLocs = dict(locs)
        del newLocs[endKey]        
        
        path = list(path)
        nextPath = []
        BFS(maze, start, locs[endKey], nextPath, set())
        #print("route",nextPath)
        path.extend(nextPath)
        if len(path) > best[1]:
            return False
        keys.add(endKey.lower())
        
        lpos=locs[endKey.lower()]
        try:
            upos=locs[endKey.upper()]        
            maze[upos[0]][upos[1]] = "."
        except:
            pass
        maze[lpos[0]][lpos[1]] = "."
                
        availables = findAvailableKeys(newMaze, locs[endKey], newLocs)
        availables = sorted([k for k in availables if k.islower() or (k.isupper() and k.lower() in keys)],reverse=True)

        #print("Availables:",availables,"from endkey",endKey)
        if len(availables) == 0:           
            #print(locs)
            if len(path) < best[1]:
                best = (path,len(path))
                print("Found sequence",len(path))
            return True
        
        #print("Availables:",availables,"from endkey",endKey)
        for available in availables:
            #[print(m) for m in maze]
            #print("Searching",available)
            solveRec(newMaze, locs[endKey], available, path, newLocs, set(keys), result)
        keys.remove(endKey.lower())
        try:
            maze[upos[0]][upos[1]] = endKey.upper()
        except:
            pass
        maze[lpos[0]][lpos[1]] = endKey.lower()

        return False

    global best
    best = [0,MAX]
    for key in [x for x in findAvailableKeys(maze, start, locs) if x.islower()]:
        print("Starting search from",key,locs[key])
        #result: [[sequence], steps]
        result = []
        solveRec(maze, start, key, [], locs, set(), result)
        
        print("Best:",best,len(best))
    


solve(maze)

    
