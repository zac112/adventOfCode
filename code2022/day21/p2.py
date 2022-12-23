monkeys = {}        
ops = {'+':lambda a,b:a+b,
       '-':lambda a,b:a-b,
       '*':lambda a,b:a*b,
       '/':lambda a,b:a//b}
reverseOp = {'+':ops['-'],
       '-':ops['+'],
       '*':ops['/'],
       '/':ops['*']}

with open("data.txt") as f:
    for line in f.read().splitlines():
        match line.split(" "):
            case [o, e1,op,e2]:
                monkeys[o[:-1]] = [e1,ops[op],reverseOp[op],e2,op]
            case [o, e1]:
                monkeys[o[:-1]] = int(e1)

def solveNoTarget(monkey):
    if monkey == "humn":        
        raise ValueError
    
    match monkeys[monkey]:
        case int(exp):
            return exp
        case l,op,rop,r,sym:
            return op(solveNoTarget(l),solveNoTarget(r))

def solve(monkey, target=None):
    if monkey == "humn":
        if target is None:
            raise ValueError
        print("Human",target)
        return target

    match monkeys[monkey]:        
        case int(exp):
            return exp
        case l,op,rop,r,'/': 
            try:
                a = solveNoTarget(l)
                b = solve(r, op(a,target))
            except ValueError:
                b = solveNoTarget(r)
                a = solve(l, rop(target,b))
        case l,op,rop,r,"-":
            try:
                a = solveNoTarget(l)
                b = solve(r, -op(target,a))
            except ValueError:
                b = solveNoTarget(r)
                a = solve(l, rop(target,b))
        case l,op,rop,r,sym:
            try:
                a = solveNoTarget(l)
                b = solve(r, rop(target,a))
            except ValueError:
                b = solveNoTarget(r)
                a = solve(l, rop(target,b))
    return op(a,b)
        
target = solveNoTarget("njlw")
print("target",target)
print(solve("gvfh", target) == target)
