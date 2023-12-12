from functools import cache
import re

with open('data.txt') as f:
    data = f.read().splitlines()
    rows = []
    for line in data:
        springs, groups = line.split(" ")
        springs = springs+("?"+springs)*4
        springs = springs.strip(".")
        groups = [int(x) for x in groups.split(",")]*5
        rows.append((springs, groups))

def hasAllGroups(springs:str, groups:list):    
    pat = ""
    for g in groups:
        pat += "[\\.?]*[#?]{"+f"{g}"+"}"
    pat += "[\\.?]*"

    return re.match(pat,"".join(springs)) is not None
    
def hasMatchingBroken(orig, curr):
    return all(sorted(pair) != sorted(('.','#')) 
               for pair in zip(orig, curr))
    
def usesAllBrokenSprings(springs_orig, springs):
    for i in [i for i,c in enumerate(springs_orig) if c=="#"]:
        if i >= len(springs) or springs[i]!="#" : 
            return False
    return True

def fit(springs_orig, groups_orig, springs, s_i, groups):
    remaining = "".join(springs_orig[len(springs)-1:])
    cache_entry = (remaining, groups)
    options = 0
    
    if len(groups)==0 and hasAllGroups(springs, groups_orig): 
        if not usesAllBrokenSprings(springs_orig, springs): 
            cache[cache_entry] = 0
            return 0        
        cache[cache_entry] = 1
        return 1
    
    if cache_entry in cache:
        return cache[cache_entry]
    
    for i, c in enumerate(springs_orig[s_i:]):
        g = groups[0]
        springs = list(springs)
        realStart = s_i+i
        springs[s_i:realStart] = ['.']*(i)
        springs[realStart : realStart+g+1] = ['#']*g+['.']*(0 if len(groups)==1 else 1)
        if s_i+sum(groups)+len(groups)-1 > len(springs_orig): continue
        if not hasMatchingBroken(springs_orig, springs): continue
        if len(springs)<=len(springs_orig):
            options += fit(springs_orig, groups_orig, springs, realStart+g+1, groups[1:])

    cache[cache_entry] = options
    return options

options = 0
for springs, groups in rows:
    print("Start;:",springs, groups)
    cache = {}
    fits = fit(springs, tuple(groups), [], 0, tuple(groups))
    print(fits)
    options += fits
print("Final:",options)

