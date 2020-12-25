from collections import deque
data = "318946572"
test = "389125467"
cups = list(map(int,data))
turns = 100
current = cups[0]

numCups = 3

allCups = [cups]
def getIndex(i):
    cuplist = i//len(cups)
    index = i%len(cups)
    while cuplist >= len(allCups):
        allCups.append(cups)
    return cuplist, index    
    
for i in range(turns):
    print(cups)
    cuplist, index = getIndex(i)        
    turnCups = allCups[cuplist]

    removed = []
    for n in range(3):
        l,ii = getIndex(cups.index(current)+1)
        removed.append(allCups[l].pop(ii))

    #print(cups,";",current,removed)
    
    destination = current -1
    while destination <= 0 or destination in removed:
        if destination <= 0:
            destination = len(cups)+len(removed)+destination
            continue
        destination -= 1
                    
    destination = cups.index(destination)

    #print(" cur:",current,"\n rem:",removed,"\n dest:", destination)
    
    for x in removed[::-1]:
        cups.insert(destination+1,x)

    current = cups[(cups.index(current)+1)%len(cups)]

print(cups,";",current)
    
