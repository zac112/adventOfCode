def HASH(step):
    curval = 0
    for c in step:
        curval = (curval+ord(c))*17%256
    return curval
        
with open('data.txt') as f:
    data = f.read().split(",")

curval = 0
for step in data:
    curval += HASH(step)

print(curval)