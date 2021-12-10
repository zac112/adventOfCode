from functools import reduce

with open('data.txt') as file:
    lines = file.readlines()

print(lines)
    

pairs={'(':')',
       '{':'}',
       '[':']',
       '<':'>'}

def parse(expression, endIndex):
    if expression[endIndex-1] in pairs and expression[endIndex] != pairs.get(expression[endIndex-1],""):
        print("Syntax error: expected",pairs.get(expression[endIndex-1],""),"got",expression[endIndex])
        return [pairs.get(expression[endIndex-1]), expression[endIndex]]
        
    if expression[endIndex] == pairs.get(expression[endIndex-1],""):
        expression.pop(endIndex)
        expression.pop(endIndex-1)
        return None
    else:
        error = parse(expression, endIndex-1)
        if error:
            return error

def autocompleteScore(symbols):
    scoreMapping = {
        ')':1,
        ']':2,
        '}':3,
        '>':4}
    res = []
    for row in symbols:
        scores = [scoreMapping[symbol] for symbol in row]        
        score = reduce(lambda a,b: a*5+b,scores)
        res.append(score)
    
    return res
     
errors = []
incompleteLines = []
autocompleteScores = []
for line in lines:
    print("Starting",line[:-1])
    autocompleted = []
    line = list(line.strip())
    incompleteLines.append(line)
    while len(line)>0:
        try:
            while line[-1] in pairs:
                autocompleted.append(pairs[line.pop()])
        except IndexError:
            break
        error = parse(line,len(line)-1)
        if error:            
            errors.append(error)
            incompleteLines.pop()
            break
    if not error:
        autocompleteScores.append("".join(autocompleted))
        print("Parsed successfully. Autocomplete:","".join(autocompleted))


scores = autocompleteScore(autocompleteScores)
print("AC scores:",scores)
print("Winner:",sorted(scores)[len(scores)//2])
