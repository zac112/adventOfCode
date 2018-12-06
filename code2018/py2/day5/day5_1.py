from string import ascii_lowercase
import re

polymer =""
with open("../../data/5.txt", "r") as f:
    for line in f:
        polymer = line

length = len(polymer)
newLength = 0
while length <> newLength:
    length = len(polymer)
    for x in ascii_lowercase:
        polymer = re.sub("("+x+x.upper()+"|"+x.upper()+x+")", "", polymer)
    newLength = len(polymer)
        
print len(polymer)

