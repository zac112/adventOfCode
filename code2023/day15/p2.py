import re

def HASH(step, val=0):
    if not step: return val
    return HASH(step[1:],(val+ord(step[0]))*17%256)
        
with open('data.txt') as f:
    data = f.read().split(",")

def eq(a,b,box):
    for i,lens in enumerate(box):
        if lens[0]==a:
            box[i] = (a,b)
            return
    else:
        box.append((a,b))

def dash(a,b,box):
    for i,lens in enumerate(box):
        if lens[0]==a:
            box.pop(i)

hashmap = {}
for step in data:    
    match re.findall("(\\D+)([-=])(\\d+)?",step):
        case [(a,'=',b)]:    
            box = hashmap.setdefault(HASH(a) ,[])
            eq(a,b,box)            

        case [(a, '-','')]: 
            box = hashmap.get(HASH(a) ,[])
            dash(a,b,box)
            
result = 0
for box, lenses in hashmap.items():
    for i, lens in enumerate(lenses):
        result += (box+1)*(i+1)*int(lens[1])

print(result)