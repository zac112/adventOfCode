import re

s = ""
with open("../../data/8.txt","r") as f:
    for line in f:
        s += line

characters = len(s)

s = re.sub("\\\\","\\\\\\\\", s)
s = re.sub("\"","\\\\\"", s)
s = re.sub("\n","\"\n\"", s)
s = "\""+s+"\""
print (s)
print (len(s)-characters)
