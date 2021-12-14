from collections import Counter

with open('data.txt') as f:
    molecule,_,*rules = f.readlines()
    molecule = molecule.strip()

rules = {a:b.strip() for a,b in map(lambda a:a.split(' -> '),rules)}

print(rules)
for step in range(10):
    newMolecule = []
    for a,b in zip(molecule,molecule[1:]):
        newMolecule.append(a)
        newMolecule.append(rules[a+b])
    newMolecule.append(molecule[-1])
    molecule = newMolecule

print(molecule)
counts = Counter(molecule)
print(counts)
print(counts.most_common()[0][1]-counts.most_common()[-1][1])
