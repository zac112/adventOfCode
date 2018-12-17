def findSum(containers, usedContainers, targetSum, currIndex, result):
    currentSum = sum([u[0] for u in usedContainers])
    if currentSum == targetSum:
        oldLen = len(result)
        result.add(tuple(sorted(usedContainers, key=lambda a:a[1])))
        if len(result) != oldLen: print(len(result))
        return
    if currentSum > targetSum:
        return
    if len(containers) == 0:
        return
    
    for i in range(currIndex, len(containers)):
        c = containers[i]
        used = list(usedContainers)
        used.append(c)
        findSum(containers, used, targetSum, i+1, result)

containers = []
target = 150

with open("../../data/17.txt", "r") as f:
    #f = [20,15,10,5,5]
    i = 0
    for line in f:
        containers.append((int(line),i))
        i += 1

containers.sort()

result = set()
findSum(containers, [], target, 0, result)
print (len(result))
