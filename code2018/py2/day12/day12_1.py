PLANT = "#"
EMPTY = "."

class Pot:
    
    ##hasPlant: boolean

    ##c: # sets plant to pot
    def __init__(self, c, num):
        if c == PLANT:
            self.plant = True
        else:
            self.plant = False
        self.number = num

    def hasPlant(self):
        return self.plant

    def getSymbol(self):
        if self.plant:
            return PLANT
        else:
            return EMPTY

    def getNumber(self):
        return self.number

    def setNumber(self, num):
        self.number = num
        
class Pots:
    
    def __init__(self):
        self.pots  = []
        
    def getPot(self, index, distance):
        if index + distance < 0 or index + distance >= len(self.pots):
            return Pot(EMPTY, index+distance)


        return Pot(self.pots[index+distance].getSymbol(), index+distance)

    def addPot(self, pot):
        self.pots.append(pot)

    def __str__(self):
        result = ""
        for pot in self.pots:
            result += pot.getSymbol()
        return result

    def __iter__(self):
        for p in self.pots:
            yield p

    def __len__(self):
        return len(self.pots)

    def __getitem__(self, i):
        return self.pots[i]
    
class Rule:

    #rule : list of booleans if hasPlant
    #result: boolean the successful application of this rule 
    
    ##rule: string, e.g. ##.##
    ##result: PLANT or EMPTY
    def __init__(self, rule, result):
        self.rule = []
        for c in rule:
            if c == PLANT:
                self.rule.append(True)
            else:
                self.rule.append(False)

        self.result = result


    def ruleMatches(self, pots, index):
        res = True
        for i in range(len(self.rule)):
            pot = pots.getPot(index, i-len(self.rule)/2)
            if pot.hasPlant() <> self.rule[i]:
                res = False
                break        
        return res

    ##Tries to
    def applyRule(self, pots, index):
        if self.ruleMatches(pots, index):
            return Pot(self.result, index)
        else:
            raise Exception()
        
    def __str__(self):
        return str(self.rule)+"->"+str(self.result)

class Cave:
    
    def __init__(self, pots, rules):        
        self.pots = pots
        self.rules = rules

    def doGeneration(self):
        newPots = Pots()
        for i in range(len(self.pots)+3):
            pot = self.pots.getPot(i,0)
            for rule in self.rules:
                try:
                    newPots.addPot(rule.applyRule(self.pots, i))

                    break
                except:
                    pass
                    #print "no mathcing rule"
            else:
                newPots.addPot(pot)

        self.pots = newPots
        
    def __str__(self):
        return str(self.pots)
    
cave = None
generations = 20

with open("../../data/12.txt","r") as f:
    pots = Pots()    
    rules = []
    num = 0
    for line in f:
        if "initial state: " in line:
            print "initial:"
            print line[15:]
            for c in line[15:]:
                pots.addPot(Pot(c,num))
        if " => " in line:
            split = line.split(" => ")
            newRule = Rule(split[0].strip(), split[1].strip())
            rules.append( newRule )
        num +=1
    cave = Cave(pots, rules)

        
print cave
for i in range(generations):
    cave.doGeneration()
print cave

print sum([ pot.getNumber() for pot in cave.pots if pot.hasPlant()])

