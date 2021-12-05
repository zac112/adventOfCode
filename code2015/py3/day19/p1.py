import re

translations = {}
with open("../../data/19.txt") as file:
    *changes, _, molecule = file.readlines()
    for c in changes:
        k,v = c.split(" => ")
        translations.setdefault(k,[]).append(v[:-1])
        
print(molecule,translations)

replacements = []
molecule = re.sub("([A-Z][a-z]?)","\\1,",molecule).split(',')[:-1]
print(len(molecule))
for i, mol in enumerate(molecule):
    for rep in translations.get(mol,[]):
        replacements.append("".join(molecule[:i]+[rep]+molecule[i+1:]))

print(len(set(replacements)))

#low 556
#577 wrong
