with open('data.txt') as f:
    data = f.read().splitlines()
    rows = []
    for line in data:
        springs, groups = line.split(" ")
        groups = [int(x) for x in groups.split(",")]
        rows.append((springs, groups))

def isOK(springs:str, groups:list):
    springs = list(springs)
    for g in groups[::-1]:
        while springs and springs[-1]==".": springs.pop()
        for _ in range(g):
            if len(springs)==0 or springs[-1] != "#": return False
            springs.pop()
        if springs:
            if springs[-1] != ".": return False
            springs.pop()
    
    while springs and springs[-1]==".": springs.pop()
    return len(springs)==0

def bruteForce(springs_orig, groups):
    qm = [i for i,c in enumerate(springs_orig) if c=='?']
    options = 2**len(qm)
    correct = 0
    for i in range(options):
        opts = list(bin(i)[2:].rjust(len(qm)))
        springs = list(springs_orig)
        for a,c in enumerate(springs):
            if c == '?': 
                springs[a] = ("#" if opts.pop(0)=='1' else '.')
        if isOK(springs, groups):
            correct += 1

    return correct

options = 0
for springs, groups in rows:
    options += bruteForce(springs, groups)
print(options)






