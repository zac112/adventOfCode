monkeys = {}
ops = {'+':lambda a,b:a+b,
       '-':lambda a,b:a-b,
       '*':lambda a,b:a*b,
       '/':lambda a,b:a//b}
with open("data.txt") as f:
    for line in f.read().splitlines():
        match line.split(" "):
            case [o, e1,op,e2]:
                monkeys[o[:-1]] = [e1,ops[op],e2]
            case [o, e1]:
                monkeys[o[:-1]] = int(e1)

def solve(monkey):
    match monkeys[monkey]:
        case int(exp):
            return exp
        case l,op,r:
            return op(solve(l),solve(r))


print(solve("root"))
