from itertools import batched

data = []
with open('data.txt') as f:
    d = f.read()+'0'
    for i,file in enumerate(batched(d,n=2)):
        data.append((i,*file))

disk = []
for d in data:
    for f in range(int(d[1])):
        disk.append(d[0])
    for f in range(int(d[2])):
        disk.append(None)

print("OK",len(disk))

right = len(disk)-1
left = 0
while left < right:
    if disk[left] == None:
        while disk[right] == None:
            right -= 1
        if left >= right: break
        disk[left] = disk[right]
        disk[right] = None
    left += 1

checksum = 0
for i,f in enumerate(disk):
    if f == None: break
    checksum += i*f
print("P1",checksum)

#P2
disk = []
for d in data:
    disk.append([int(d[0]), int(d[1])])
    disk.append([None, int(d[2])])
    

right = len(disk)-1
while right > 0:
    if disk[right][0]==None:
        right -=1
        continue
    for i,span in enumerate(disk[:right]):
        if span[0]==None and span[1]>=disk[right][1]:
            newSpan = list(disk[right])
            disk[right][0] = None
            disk.insert(i,newSpan)
            span[1] -= newSpan[1]
            break
    right -= 1

checksum = 0
index = 0
for span in disk:
    if span[0]==None:
        index += span[1]
        continue
    for i in range(span[1]):
        checksum += (index+i)*span[0]
    index += span[1]
print("P2",checksum)
