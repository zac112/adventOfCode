changes = []
with open("../../data/1.txt", "r") as f:
    for line in f:
        changes.append(int(line))

s = 0
freqs = set([0])
ok = True
while ok:
    for val in range(len(changes)):        
        s = s + changes[val]
        if s in freqs:
            ok = False
            break
        else:            
            freqs.add(s)
           
print s
