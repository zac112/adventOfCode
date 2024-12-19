from functools import cache
with open('data.txt')as file:
    lines = file.readlines()
    stripes = lines[0].replace("\n","").split(", ")
    designs = [line.replace("\n","") for line in lines[2:]]

@cache
def matchStripe(design):    
    if design=="": return 1
    
    for s in stripes:
        if not design.startswith(s): continue
        if matchStripe(design[len(s):]): return 1
    return 0

matches = 0
for d in designs:
    matches += matchStripe(d)
print("P1:",matches)

#P2
@cache
def matchAllStripes(design):
    if design=="": return 1
    
    matches = 0
    for s in stripes:
        if not design.startswith(s): continue
        matches += matchAllStripes(design[len(s):])
    return matches

matches = 0
for d in designs:
    matches += matchAllStripes(d)
print("P2:",matches)
