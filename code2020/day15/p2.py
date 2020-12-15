data=[2,0,6,12,1,3]

#data=[0,3,6]
lastNum = data[0]
mem = {}
for i,d in enumerate(data):
    lastNum = d
    mem.setdefault(d,[]).append(i+1)
    
    
turns = 30000000
#turns = 2020
def findOccurences(data, val):
    res = []
    for i in range(len(data)-1,-1,-1):
        if data[i] == val:
            res.append(i+1)
        if len(res) >=2:
            break
    return res


for i in range(len(data),turns):
    if lastNum in mem:
        if len(mem[lastNum]) < 2:            
            lastNum = 0
        else:
            lastNum = mem[lastNum][-1]-mem[lastNum][-2]
        mem.setdefault(lastNum,[]).append(i+1)    
    
print(lastNum)
