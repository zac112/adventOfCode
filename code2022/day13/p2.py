from itertools import zip_longest

def isLeftSmaller(left, right):
    if left is None: return True
    if right is None: return False
        
    if isinstance(left,int) and isinstance(right,int):
        if left == right: return None
        return left <= right

    elif isinstance(left,int) and isinstance(right,list):
        return isLeftSmaller([left], right)
        
    elif isinstance(right,int) and isinstance(left,list):
        return isLeftSmaller(left, [right])        

    elif isinstance(right,list) and isinstance(left,list):
        for x,y in zip_longest(left,right, fillvalue=None):
            r = isLeftSmaller(x,y)            
            if r is not None:
                return r
    
        return None
        
    
i = 1
correct = 0
packets = []
with open("data.txt") as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:continue
        packets.append(eval(line))

divider1 = [[2]]
divider2 = [[6]]
packets.append(divider1)
packets.append(divider2)

victories = {}
for i, p1 in enumerate(packets):
    for j, p2 in enumerate(packets):
        if i == j:continue
        if isLeftSmaller(p1,p2):
            winner,loser = p1,p2
        else:
            winner,loser = p2,p1
        victories[str(winner)] = victories.setdefault(str(winner),0)+1

result = sorted([(p,v) for p,v in victories.items()], key=lambda a:a[1])[::-1]
result = [a for a,b in result]
print((result.index(str(divider1))+1)*(result.index(str(divider2))+1))
