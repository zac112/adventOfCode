from itertools import pairwise

with open("data.txt") as f:
    lines = [a.replace("\n","") for a in f.readlines()]
    pages = [tuple(p.split(",")) for p in lines[lines.index("")+1:]]
    order = {}
    for x in lines[:lines.index("")]:
        a,b = x.split("|")
        order.setdefault(a,[]).append(b)
    

#for test data
order.setdefault('13',[])

middleSum = 0
wrongOrder = []
for page in pages:
    for p1,p2 in zip(page,page[1:]):
        if p2 not in order[p1]:
            wrongOrder.append(page)
            break
    else:
        middleSum += int(page[len(page)//2])
print("Middlesum of correct pages",middleSum)

#Part2
middleSum = 0
for page in wrongOrder:
    correctOrder = [page[0]]
    for p in page[1:]:
        ordered = [a in order[p] for a in correctOrder]
        index = ordered.index(True) if (True in ordered) else len(ordered)
        correctOrder.insert(index,p)
        
    middleSum += int(correctOrder[len(correctOrder)//2])
print("Middlesum of incorrect pages",middleSum)
