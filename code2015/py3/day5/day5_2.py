import re

lines = []
with open("../../data/5.txt", "r") as f:
    for line in f:
        lines.append(line)


niceLines = 0
for line in lines:

    p = re.compile(r"(..).*\1")
    if p.search(line) == None:
        continue
     
    p = re.compile(r"(.).\1")
    if p.search(line) == None:
        continue

    niceLines += 1

print (niceLines)
