import string

with open("data.txt") as f:
    data = f.read()

def score(character):
    return string.ascii_letters.index(character)+1

s = 0
for rs in data.split("\n"):
    r1,r2 = rs[:len(rs)//2],rs[len(rs)//2:]
    shared = [c for c in r1 if c in r2]
    s += score(shared[0])

print(s)
