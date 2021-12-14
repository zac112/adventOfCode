from collections import Counter
from collections import deque
from functools import lru_cache

with open('data.txt') as f:
    molecule,_,*rules = f.readlines()
    molecule = molecule.strip()

rules = {a:b.strip() for a,b in map(lambda a:a.split(' -> '),rules)}
print(rules)

@lru_cache(maxsize=None)
def expand(molecule, steps):
    if steps == 0:
        return Counter(molecule[1])

    new = rules[molecule[0]+molecule[1]]
    if steps == 1:
        c = Counter(molecule[0])
        c.update(expand(molecule[0]+new,steps-1))
    else:
        c = Counter()               
        c.update(expand(molecule[0]+new,steps-1))    
        c.update(expand(new+molecule[1],steps-1))
    
    return c
    

print(molecule)
counts = Counter()
steps = 40
for a,b in zip(molecule,molecule[1:]):
    counts.update(expand(a+b,steps))
counts.update(Counter(molecule[-1]))

print(counts)
print(counts.most_common()[0][1]-counts.most_common()[-1][1])
