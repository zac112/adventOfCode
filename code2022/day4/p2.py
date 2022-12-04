
with open("data.txt") as f:
    data = f.read()

result = 0
for ids in data.split("\n"):
    if ids == "":continue
    id1,id2 = ids.split(",")
    r1s,r1e= [int(r) for r in id1.split("-")]
    r2s,r2e= [int(r) for r in id2.split("-")]
    r1 = list(range(r1s,r1e+1))
    r2 = list(range(r2s,r2e+1))
    overlap = [x for x in r1 if x in r2]
    if len(overlap)>0:
        result += 1

print(result)

#567 wrong
