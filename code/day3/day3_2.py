area = []

claims = []
with open("../../data/3.txt", "r") as f:
    for line in f:
        claims.append(line)

for x in range(1000):
    area.append([0 for x in range(1000)])

# #1 @ 1,3: 4x4
for claim in claims:
    parts = claim.split(" ")
    claimId = parts[0][1:]
    start = [int(x) for x in parts[2][:-1].split(",")]
    size = [int(x) for x in parts[3].split("x")]

    for x in range(size[0]):
        for y in range(size[1]):
            area[start[0]+x][start[1]+y] += 1
            
for claim in claims:
    parts = claim.split(" ")
    claimId = parts[0][1:]
    start = [int(x) for x in parts[2][:-1].split(",")]
    size = [int(x) for x in parts[3].split("x")]

    found = True
    
    for x in range(size[0]):
        for y in range(size[1]):
            if area[start[0]+x][start[1]+y] > 1:
                found = False

    if found:
        print claimId
        
