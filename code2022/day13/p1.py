from itertools import zip_longest

def isLeftSmaller(left, right):
    if left is None: return True
    if right is None: return False
        
    if isinstance(left,int) and isinstance(right,int):
        if left == right: return None
        return left <= right

    elif isinstance(left,int) and isinstance(right,list):
        return isLeftSmaller([left], right)
        
    elif isinstance(right,int) and isinstance(left,list):
        return isLeftSmaller(left, [right])
        
    elif isinstance(right,list) and isinstance(left,list):
        for x,y in zip_longest(left,right, fillvalue=None):
            r = isLeftSmaller(x,y)            
            if r is not None:
                return r
    
        return None
        
    
i = 1
correct = 0
with open("data.txt") as f:
    while True:
        print("    ",i)
        p1 = f.readline()
        
        if len(p1)==0: break
        p1 = eval(p1)
        p2 = eval(f.readline())
        
        if isLeftSmaller(p1,p2):
            print("== correct,",i)
            correct += i
        f.readline()
        i += 1

print(correct)
