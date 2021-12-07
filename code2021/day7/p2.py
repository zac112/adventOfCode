with open('data.txt') as file:
    positions = [int(x) for x in file.readline().split(',')]

def findFuelCost(positions, target):
    cost = 0
    for x in positions:
        cost += sum(range(abs(x-target)+1))
    return cost

def findMinimumFuelCost(positions, guess):    
    neighborhood = {guess:findFuelCost(positions, guess),
                    guess+1:findFuelCost(positions, guess+1),
                    guess-1:findFuelCost(positions, guess-1)}
    newValues = sorted(neighborhood, key=lambda a:neighborhood[a])
    #print(guess,":",neighborhood)
    if (guess == newValues[0]):
        return newValues[0]
    else:
        return findMinimumFuelCost(positions, newValues[0])
    

#test data
#positions = [16,1,2,0,4,2,7,1,2,14]
print(findMinimumFuelCost(positions, sum(positions)//len(positions)))
