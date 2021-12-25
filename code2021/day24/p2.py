from copy import deepcopy

variables = {'x':0,'y':0,'z':0,'w':0}#[0,0,0,0]
digitvalues = [(13,10,1),(11,16,1),(11,0,1),(10,13,1),
 (-14,7,26),(-4,11,26),(11,11,1),(-3,10,26),
 (12,16,1),(-12,8,26),(13,15,1),(-12,2,26),
 (-15,5,26),(-12,10,26)]

def digit(variables, x1,y1,z1):
    variables['x'] = variables['z']%26
    variables['z'] = variables['z']//z1
    variables['x'] += x1
    #variables['x'] = 1 if variables['x']!=variables['w'] else 0
    variables['x'] = 1 if variables['x']==variables['w'] else 0
    variables['x'] = 1 if variables['x']==0 else 0
    variables['y'] = 25*variables['x']+1
    
    variables['z'] *= variables['y']

    variables['y'] = variables['w'] + y1
    variables['y'] *= variables['x']
    variables['z'] += variables['y']
    return variables['w']

def solverec(variables, digits):
    if len(digits) == 14:
        if variables['z']==0:
            print("FOUND SOLUTION",digits)
            print(variables)
            return
        else:
            print("NOPE")
            return

    #if len(digits)==4:
    #    print("number",digits)
    newDigits = list(digits)
    newVariables = deepcopy(variables)
    if len(digits)>0 and digitvalues[len(digits)][0] < 0:
        nextW = newVariables['z']%26+digitvalues[len(digits)][0]
        if nextW > 9 or nextW < 1:                
            return
        
        newVariables['w'] = nextW
        newDigits.append(nextW)
        digit(newVariables, *digitvalues[len(newDigits)-1])
        #if len(newDigits)>2 and newDigits[1]==8:
        #    print(len(newDigits), newDigits, "\n",newVariables)
        solverec(newVariables, newDigits)
    else:
        for nextW in range(1,10):
            newVariables = deepcopy(variables)
            newVariables['w'] = nextW
            newDigits.append(nextW)
            digit(newVariables, *digitvalues[len(newDigits)-1])
            #if len(newDigits)>2 and newDigits[1]==8:
            #    print(len(newDigits), newDigits, "\n",newVariables)
            solverec(newVariables, newDigits)
            newDigits.pop()
        
solverec(variables, [])
