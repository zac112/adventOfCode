from string import ascii_lowercase
import re

polymer = ""
with open("../../data/5.txt", "r") as f:
    for line in f:
        polymer = line

lengths = []

def react(polymer):
    length = len(polymer)
    newLength = 0
    while length <> newLength:
        length = len(polymer)
        for x in ascii_lowercase:
            polymer = re.sub("("+x+x.upper()+"|"+x.upper()+x+")", "", polymer)
        newLength = len(polymer)
    return polymer

for x in ascii_lowercase:    
    molecules = re.sub(x+"|"+x.upper(), "", polymer)
    molecules = react(molecules)
    lengths.append((x,len(molecules)))
    print x, len(molecules)
        
lengths.sort(key=lambda a : a[1], reverse=False)

print lengths
print lengths[0]

