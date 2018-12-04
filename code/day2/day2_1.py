wantedValues = {2:0, 3:0}

strings = []
with open("../../data/2.txt", "r") as f:
    for line in f:
        strings.append(line)

for s in strings:
    letters = {}
    for c in s:
        if c in letters :
            letters[c] = letters[c]+1
        else:
            letters[c] = 1

    print letters
    
    found2 = False
    found3 = False
    for k in letters:
        if letters[k] == 2 and not found2:
            wantedValues[2] = wantedValues[2]+1
            found2 = True
        if letters[k] == 3 and not found3:
            wantedValues[3] = wantedValues[3]+1
            found3 = True
        
print wantedValues[2]*wantedValues[3]
