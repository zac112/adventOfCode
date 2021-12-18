from math import floor, ceil

with open('data.txt') as f:
    numbers = [eval(x.strip()) for x in f.readlines()]

[print(x) for x in numbers]

class Literal():    
    
    def __init__(self, val):
        self.val = val

    def reduce(self):
        pass

    def canExplode(self,parents, level, explosions=0):
        return False
    
    def explode(self,parents, level, explosions):
        return 0

    def canSplit(self,parent):
        return self.val >= 10
    
    def split(self,parent):
        if self.val >= 10:
            parent.setChild(self, Number(floor(self.val/2), ceil(self.val/2)))
            return True
        return False
        

    def magnitude(self):
        return self.val
    
    def __add__(self, val):        
        if type(val) == Literal:
            val = val.val
        return Literal(self.val + val)

    def leafNodes(self,parent):
        return [(self,parent)]

    def printTree(self, depth):
        return f"{self.val}"
    
    def __repr__(self):
        return f"{self.val}"

    
    
    
class Number(Literal):
    values = [Literal(x) for x in range(10)]

    def __init__(self, left, right):
        if type(left) == int:
            left = Literal(left)
        if type(right) == int:
            right = Literal(right)

        if type(left) == list:
            left = Number(left[0], left[1])
        if type(right) == list:
            right = Number(right[0], right[1])

        self.left = left
        self.right = right
    
    def leafNodes(self,parent):
        return [*self.left.leafNodes(self), *self.right.leafNodes(self)]
            
    def setChild(self, child, val):
        if self.left == child:
            self.left = val
        else:
            self.right = val
            
    def reduce(self):
        while changed := self.canExplode([self],0,0) or self.canSplit(self):  
            while self.canExplode([self],0,0):
                self.explode([self],0,0)                
            self.split(self)

    def terminal(self):
        return type(self.left) == Literal and type(self.right)==Literal

    def canExplode(self,parents, level, explosions=0):        
        if self.terminal() and level >= 4:
            return True
        return self.left.canExplode(parents, level+1, explosions) or self.right.canExplode(parents, level+1, explosions)
        
    def explode(self,parents, level, explosions=0):
        explosions += self.left.explode(parents+[self], level+1,explosions)
        if explosions>0:
            return explosions
        if self.terminal() and level >= 4:            
            neighborhood = parents[0].leafNodes(parents[0])
            me = self.leafNodes(self)
            for i,v in enumerate(zip(neighborhood,neighborhood[1:])):
                if me[0] == v[0] and me[1] == v[1]:
                    index = i
                    break
            
            if index > 0:
                val,p = neighborhood[index-1]
                p.setChild(val, val+self.left)
            if index < len(neighborhood)-2:
                val,p = neighborhood[index+2]
                p.setChild(val, val+self.right)
            
            parents[-1].setChild(self, Literal(0))
            return explosions+1

        return self.right.explode(parents+[self], level+1,explosions)
        
        

    def canSplit(self,parent):
        change = self.left.canSplit(self)
        change = change or self.right.canSplit(self)
        return change
        
    def split(self,parent):
        if self.left.split(self): return True
        if self.right.split(self): return True

    def magnitude(self):
        return 3*self.left.magnitude()+2*self.right.magnitude()
    
    def __add__(self, number):
        if type(number) == []:
            number = Number(number[0], number[1])
        
        return Number(self,number)

    def printTree(self, depth=0):
        return f"[{self.left.printTree(depth+1)} {self.right.printTree(depth+1)} ({depth})]"
        
    def __repr__(self):
        return f"[{repr(self.left)} {repr(self.right)}]"


def sumNumbers(num1,num2):
    result = Number(num1[0], num1[1])+Number(num2[0], num2[1]) 
    result.reduce()
    return result.magnitude()

magnitudes = set()
for i,num1 in enumerate(numbers):
    for j,num2 in enumerate(numbers):
        if i==j: continue
        magnitudes.add(sumNumbers(num1,num2))
        magnitudes.add(sumNumbers(num2,num1))
                

print(max(magnitudes))

