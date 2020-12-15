data=[2,0,6,12,1,3]

#data=[3,1,2]

turns = 2020
#turns = 11
def findOccurences(data, val):
    return [(i+1,v) for i,v in enumerate(data) if val == v]


for i in range(len(data),turns):
    oc = findOccurences(data,data[-1])
    #print(data)
    if len(oc)<2:
        data.append(0)
        continue
    data.append(oc[-1][0]-oc[-2][0])    
    
print(data[-1])
