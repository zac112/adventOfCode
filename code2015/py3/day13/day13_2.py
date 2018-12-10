def collectCombinations(people, currentSelection, result):
    if len(currentSelection) == len(people):
        result.append(currentSelection)
        return

    for i in range(len(people)):
        selection = list(currentSelection)
        if people[i] not in selection:
            selection.append(people[i])
            collectCombinations(people, selection, result)
    

#[name, happiness change, other name]
data = []
with open("../../data/13.txt") as f:
    for line in f:
        line = line[:-2]
        split = line.split(" ");
        multiplier = 1
        if "lose" in line:
            multiplier = -1
        data.append( [split[0], multiplier*int(split[3]), split[10] ] )

people = list(set([x[0] for x in data]))

for p in people:
    data.append(["me",0,p])
    data.append([p,0,"me"])

people.append("me")

combinations = []
collectCombinations(people, [], combinations)
maxHappiness = None

print("combinations:",len(combinations))
seatingOrder = 0
for combination in combinations:
    totalHappiness = 0
    #emulate the circular table    
    combination.insert(0, combination[len(combination)-1])
    combination.append(combination[1])
    if seatingOrder % 10000 == 1:
        print("seating order #",seatingOrder,"with happiness",maxHappiness)
            
    for i in range(1, len(combination)-1):            
        previousPerson = combination[i-1]
        person = combination[i]
        nextPerson = combination[i+1]
        for d in data:
            if d[0] == person and d[2] == nextPerson:
                totalHappiness += d[1]
            if d[0] == person and d[2] == previousPerson:
                totalHappiness += d[1]
        if maxHappiness != None and totalHappiness > maxHappiness:
            break
        
    if maxHappiness == None:
        maxHappiness = totalHappiness
    else:
        maxHappiness = max(maxHappiness, totalHappiness)
    seatingOrder += 1
        
print("max happiness:",maxHappiness)
