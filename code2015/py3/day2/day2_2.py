dims = []
with open("../../data/2.txt", "r") as f:
    for line in f:
        dims.append([int(x) for x in line.split("x")])

totalLength = 0
for dim in dims:
    dim.sort()
    totalLength += 2*(dim[0]+dim[1])+dim[0]*dim[1]*dim[2]
    
print (totalLength)

