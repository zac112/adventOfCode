
with open("data.txt") as f:
    data = f.read()

fullyContained = 0
for ids in data.split("\n"):
    if ids == "":continue
    id1,id2 = ids.split(",")
    r1s,r1e= [int(r) for r in id1.split("-")]
    r2s,r2e= [int(r) for r in id2.split("-")]
    if (r1s <= r2s and r1e >= r2e) or (r2s <= r1s and r2e >= r1e):
        fullyContained += 1

print(fullyContained)

#567 wrong
