with open ('data.txt') as f:
    L1,L2=[],[]
    for line in f.readlines():
        v1,*_,v2 = line.split(" ")
        L1.append(int(v1))
        L2.append(int(v2))

L1.sort()
L2.sort()
distance = sum(map(lambda a:abs(a[0]-a[1]),zip(L1,L2)))
print("Distance:",distance)

#Part 2
S = {a: L2.count(a) for a in L2}
print ("Similarity",sum(map(lambda a:a*S.get(a,0),L1)))
