import re

s = ""
with open("../../data/1.txt", "r") as f:
    s = f.readline()

print (len(re.sub("\)","",s))-len(re.sub("\(","",s)))
