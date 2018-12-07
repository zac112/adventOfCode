import re

s = ""
with open("../../data/1.txt", "r") as f:
    s = f.readline()

floor = 0
pos = 1
for c in s:
    if c == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print (pos)
        break
    pos += 1

