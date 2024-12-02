reports = []
with open('data.txt') as f:
    for line in f.readlines():
        reports.append([int(x) for x in line.split(" ")])

def monotone(L):
    if len(L)<=1: return False
    if L[0]==L[1]: return False
    for a,b in zip(L,L[1:]):        
        if (a<b) != (L[0]<L[1]): return False
        if abs(a-b)<=0 or abs(a-b)>3 : return False
    return True

safe = []
for report in reports:
    if monotone(report):
        safe.append(report)

print("Safe:",len(safe))

#Part 2
safe = []
for report in reports:
    for i in range(len(report)):
        if monotone(report[:i]+report[i+1:]):
            safe.append(report)
            break
        
print("Safe with dampening:",len(safe))
