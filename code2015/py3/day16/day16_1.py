class Sue:
    def __init__(self,stuff):
        self.stuff = stuff
        
#Sue 500: cars: 1, perfumes: 6, vizslas: 1

sues = {}

tape = {
    "children":3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
    }

with open("../../data/16.txt", "r") as f:
    for line in f:
        d = {}
        split = line.split(" ")
        d[split[2][:-1]] = int(split[3][:-1])
        d[split[4][:-1]] = int(split[5][:-1])
        d[split[6][:-1]] = int(split[7])
                               
        sues[int(split[1][:-1])] = Sue(d) 


new = dict(sues)
while len(new) > 1:
    new = dict(sues)
    for sue in sues:
        for t in tape:
            if t in sues[sue].stuff:
                if tape[t] != sues[sue].stuff[t]:
                    del new[sue]
                    break
    sues = new

for i in sues:
    print (i)
