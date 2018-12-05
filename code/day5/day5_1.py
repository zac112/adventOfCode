#[1518-11-01 00:00] Guard #10 begins shift
#[1518-11-01 00:05] falls asleep
#[1518-11-01 00:25] wakes up
molecules = []
with open("../../data/5.txt", "r") as f:
    for line in f:
        for c in line:
            molecules.append(c)

x = 0
while x < len(molecules)-1:
    if molecules[x].lower() == molecules[x+1].lower() and molecules[x] <> molecules[x+1]:
        molecules.pop(x)
        molecules.pop(x)
        x = -1
    x += 1
        
print len(molecules)

