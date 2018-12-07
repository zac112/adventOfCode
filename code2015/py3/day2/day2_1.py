dims = []
with open("../../data/2.txt", "r") as f:
    for line in f:
        dims.append([int(x) for x in line.split("x")])

totalArea = 0
for dim in dims:
    totalArea += 2 * (dim[0]*dim[1] + dim[1]*dim[2] + dim[0]*dim[2]) + sorted(dim)[0]*sorted(dim)[1]
    
print (totalArea)
