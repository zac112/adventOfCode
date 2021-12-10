with open('data.txt') as file:
    lines = file.readlines()

print(lines)
    

pairs={'(':')',
       '{':'}',
       '[':']',
       '<':'>'}
def parse(expression, endIndex):
    #print('parse',"".join(expression),endIndex)
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

errors = []
for line in lines:
    print("Starting",line)
    line = list(line.strip())
    while len(line)>0:
        try:
            while line[-1] in pairs:
                line.pop()
        except IndexError:
            print("Parsed successfully")
            break
        error = parse(line,len(line)-1)
        if error:
            print(error)
            errors.append(error)
            break
        #print('parsed',"".join(line))
    print("Parsed successfully")

scoreMapping = {')':3,
                ']':57,
                '}':1197,
                '>':25137}
print("Syntax score:",sum(map(lambda a:scoreMapping[a[1]],errors)))
