puzzleInput = 890691
recipes = [3,7]
elves = [0,1]

while len(recipes) < puzzleInput+10:
    #print recipes
    score = recipes[elves[0]]+recipes[elves[1]]
    for c in str(score):
        recipes.append(int(c))
        
    elves[0] = (elves[0]+1+recipes[elves[0]])%len(recipes)
    elves[1] = (elves[1]+1+recipes[elves[1]])%len(recipes)    

print "".join(str(recipes[-10:]))
