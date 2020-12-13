import math

class Material:

    def __init__(self, s):
        self.amount = int(s.split(" ")[0].strip())
        self.chem = s.split(" ")[1].strip()

    def __add__(self, other):
        if(self.chem == other.chem):
            return Material(str(self.amount+other.amount)+" "+self.chem)
        return Material(str(self.amount)+" "+self.chem)

    def __sub__(self, other):
        if(self.chem == other.chem):
            return Material(str(self.amount-other.amount)+" "+self.chem)
        return Material(str(self.amount)+" "+self.chem)

    def __mul__(self, multi):
        return Material(str(self.amount*multi)+" "+self.chem)
    
    def __str__(self):
        return str(self.amount)+" "+self.chem

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.chem == other.chem

    def __hash__(self):
        return sum ( ord(s) for s in self.chem)

def topologicalSort(formulas):
    sortedList = []
    def visit(n):
        if(n in sortedList):
            return
        if(n.chem=="ORE"):
            return

        for newNode in formulas[n]:
            visit(newNode)
            
        sortedList.append(n)

    l = list(filter(lambda a: a not in sortedList, formulas.keys() ))
    while(len(l) > 0):
        visit(l[0])
        l = list(filter(lambda a: a not in sortedList, formulas.keys() ))
        
    return sortedList
    
def combineMats(reqs):
    result = []
    #print(reqs, "combined to", end=" ")
    while(len(reqs) > 0):
        newMat = reqs.pop()
        #print("got",newMat)
        for m in reqs:
            newMat = newMat+m
        result.append(newMat)
        reqs = list(filter(lambda a: a != newMat, reqs))
        reqs = list(filter(lambda a: a.amount > 0, reqs))

    #print(result)
    return result

formula = {}
mats = []

with open("../../day14.txt", "r") as f:
    lines = f.readlines()
    for r in lines:
        d = r.strip('\n').split(" => ")
        #print(d)
        formula[Material(d[1].strip())] = [Material(s.strip()) for s in d[0].split(",")]

print(formula)
print("----")

sortedList =topologicalSort(formula)
print(topologicalSort(formula))

def countOre(fuel):
    req = [Material(fuel)]
    ore = Material("0 ORE")
    while(req):
        matList = []
        for m in sortedList[::-1]:
            for x in req:
                if(m.chem == x.chem):                
                    matList.append(x)
                    req.pop(req.index(m))
                    break
        req = matList
        #print("req",req)    

        nextMat = list(filter(lambda a:a.chem==req[0].chem, formula.keys()))[0]

        multiplier = math.ceil(req[0].amount / nextMat.amount)
        req.extend([a*multiplier for a in formula[req[0]]])

        req.pop(0)
        req = combineMats(req)
        #print("newReq",req)    
        for o in filter(lambda a: a.chem=="ORE", req):
            ore = ore + o
        req = list(filter(lambda a: a.chem!="ORE", req))
    return ore

print(1000000000000- countOre("998536 FUEL").amount)
#for i in range(360664,460664):    
    #o = countOre(str(i)+" FUEL")
    #if(o.amount > 1000000000000):
    #    print(str(i-1)+" FUEL")
#print("formula:",formula)
#print("reqs:",req)
#print("ore:",ore)
