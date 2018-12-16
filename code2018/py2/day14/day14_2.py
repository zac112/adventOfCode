puzzleInput = 890691
puzzleInput = [int(c) for c in str(puzzleInput)][::-1]
recipes = [3,7]
elves = [0,1]

found = False
while not found:
    #print recipes
    score = recipes[elves[0]]+recipes[elves[1]]
    for c in str(score):
        recipes.append(int(c))
        for i in range(len(puzzleInput)):
            if(recipes[len(recipes)-i-1] != puzzleInput[i]):
                break
        else:
            print len(recipes)-len(puzzleInput)
            found = True
            break
        
        
    elves[0] = (elves[0]+1+recipes[elves[0]])%len(recipes)
    elves[1] = (elves[1]+1+recipes[elves[1]])%len(recipes)


    

