expressions = []
with open('data.txt') as f:
    for line in f.readlines():
        solution,exp = line.split(": ")        
        expressions.append([int(x) for x in exp.split(" ")] + [int(solution)])
        

def solve(operands, operations, result, concat=False):
    if result > operands[-1]: return False
    if len(operands) == 1: return result == operands[0]
    
    for op in operations:        
        if solve(operands[1:], operations, op(result,operands[0]), concat):
            return True
    return False

ops_P1 = [lambda a,b:a+b, lambda a,b: a*b]
ops_P2 = [lambda a,b:a+b, lambda a,b: a*b, lambda a,b: int(str(a)+str(b))]
correct_P1 = 0
correct_P2 = 0

for expression in expressions:
    first = expression.pop(0)
    if solve(expression,ops_P1,first):
        correct_P1 += expression[-1]        
    if solve(expression,ops_P2,first):
        correct_P2 += expression[-1]
        
print("p1:",correct_P1)
print("p2:",correct_P2)
