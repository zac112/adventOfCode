def findReadySteps(allSteps, currentSteps, finishedSteps):
    ready = set()
    for step in allSteps:
        if step[0] in finishedSteps:
            continue
        found = False
        for value in currentSteps:
            if step[0] == value[1]:
                found = True
                break
        if not found:
            ready.add(step[0])
    return list(ready)

def findLastStep(allSteps):
    left = set()
    right = set()
    for step in allSteps:
        left.add(step[0])
        right.add(step[1])
        right = right.difference(left)
    return right.pop()

allSteps = []
with open("../../data/7.txt", "r") as f:
    for line in f:
        split = line.split(" ")
        allSteps.append((split[1],split[7]))

incompleteSteps = []
incompleteSteps[:] = allSteps
finishedSteps = set()
result = ""
lastStep = findLastStep(allSteps)
    
while len(incompleteSteps) > 0:
    ready = findReadySteps(allSteps, incompleteSteps, finishedSteps)
    ready.sort(key=lambda a : a[0])
    result += ready[0]
    finishedSteps.add(ready[0])
    incompleteSteps = [x for x in incompleteSteps if x[0] != ready[0]]

print result+lastStep
