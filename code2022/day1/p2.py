with open("data.txt") as f:
    data = f.read()

i=0
elf = []
elves = [elf]
for line in data.split("\n"):
    if line == "":
        i+=1
        elf = []
        elves.append(elf)
        continue
    elf.append(int(line))
    
print(sum(sorted([sum(e) for e in elves])[-3:]))
    
