import string

with open("data.txt") as f:
    data = f.read()

def score(character):
    return string.ascii_letters.index(character)+1

s = 0
data = data.split("\n")
for r1,r2,r3 in zip(data[::3],data[1::3],data[2::3]):
    shared = [c for c in r1 if c in r2 and c in r3]
    s += score(shared[0])   
print(s)
