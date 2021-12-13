data = 33100000
houses={}
p=0
print(data)
for i in range(1,data//10):
    for x in range(i,data//10,i):
        houses[x] = houses.get(x,0)+i*10

print("Finished")
print(sorted([(a,b) for a,b in houses.items() if b >=data and b <= data*10],key=lambda a:a[0])[0])
