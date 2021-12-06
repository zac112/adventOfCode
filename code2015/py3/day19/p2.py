import re
from functools import lru_cache
translations = {}
maxLength=0
with open("../../data/19.txt") as file:
    *changes, _, molecule = file.readlines()
    for c in changes:
        k,v = c.split(" => ")
        v = re.sub("([A-Z][a-z]?)","\\1,",v).split(',')[:-1]
        maxLength = max(maxLength, len(v))
        translations.setdefault(k,[]).append(v)
    
        
print(maxLength, molecule,translations)

#The actual symbols don't mostly matter, only Rn, Ar and Y are important
key = {a:b for a,b in zip(['Rn','Ar','Y']+list(translations.keys()),'()-'+'.'*len(list(translations.keys())))}

"""
The possible patterns for translate targets are hard coded in the method.
"""
def reduce(molecule, index):
    steps = 0
    #print("Starting",index, "".join(molecule))
    while len(molecule)>1:
        if molecule[index] == '.' and molecule[index+1] == '.':
            molecule.pop(index)
            steps += 1
            print("".join(molecule),index)

        if "".join(molecule[index:index+8]) == '.(.-.-.)':
            for _ in range(7):
                molecule.pop(index+1)
            steps += 1
            print("".join(molecule),index)
                
        if "".join(molecule[index:index+6]) == '.(.-.)':
            for _ in range(5):
                molecule.pop(index+1)
            steps += 1
            print("".join(molecule),index)

        if "".join(molecule[index:index+4]) ==  '.(.)':
            for _ in range(3):
                molecule.pop(index+1)
            steps += 1
            print("".join(molecule),index)
        
        if len(molecule) <= 1 or molecule[index+1] == ')':            
            break

        if molecule[index+1] == '(':
            steps += reduce(molecule,index+2)

        if molecule[index+1] == '-':
            steps += reduce(molecule,index+2)
            return steps

    return steps

molecule = re.sub("([A-Z][a-z]?)","\\1,",molecule).split(',')[:-1]
molecule = list(map(lambda a:key[a],molecule))
print(molecule)
print(reduce(molecule,0))
