from string import ascii_lowercase

#[1518-11-01 00:00] Guard #10 begins shift
#[1518-11-01 00:05] falls asleep
#[1518-11-01 00:25] wakes up
molecules_orig = []
with open("../../data/5.txt", "r") as f:
    for line in f:
        for c in line:
            molecules_orig.append(c)

removables = [x for x in ascii_lowercase]
lengths = []
molecules = []

def react(molecules):
    x = 0
    while x < len(molecules)-1:
        if molecules[x].lower() == molecules[x+1].lower() and molecules[x] <> molecules[x+1]:
            molecules.pop(x)
            molecules.pop(x)
            x = -1
        x += 1

for removable in removables:    
    molecules = [x for x in molecules_orig if x.lower() <> removable]
    react(molecules)
    lengths.append((removable,len(molecules)))
    print removable, len(molecules)
        
lengths.sort(key=lambda a : a[1], reverse=False)

print lengths
print lengths[0]

