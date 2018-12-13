PLANT = "#"
EMPTY = "."

class Plants:
    #startIndex
    #plants = set()

    def __init__(self):
        self.plants = set()
    
    def get(self, index, distance):
        if index+distance in self.plants:
            return PLANT
        else:
            return EMPTY

    def add(self, index, plant):        
        if plant == PLANT:
            self.plants.add(index)

    def minPlant(self):
        return min(self.plants)

    def maxPlant(self):
        return max(self.plants)
        
    def __iter__(self):
        for p in self.plants:
            yield p

    def __len__(self):
        return len(self.plants)

    def __str__(self):
        return str(self.plants)
    
def ruleMatches(plants, plantIndex, rule, newPlants):
    #for i in range(len(rule[0])):
    plant = plants.get(plantIndex, 0)
    if rule[0][2] == plant:
        for j in range(len(rule[0])):
            if rule[0][j] != plants.get(plantIndex, j-2):
                #rule did not match
                break
                
        else:
            newPlants.add(plantIndex, rule[1])
            return True

    return False
    
    
def doGeneration(plants, rules):
    newPlants = Plants()
    for plantIndex in range(plants.minPlant()-15,plants.maxPlant()+60):
        for rule in rules:
            ruleMatches(plants, plantIndex, rule, newPlants)
            
    return newPlants

    
generations = 10 001
plants = Plants()
rules = []
with open("../../data/12.txt","r") as f:
    for line in f:
        if "initial state: " in line:
            print "initial:"
            print line[15:]
            ind = 0
            for c in line[15:]:
                plants.add(ind, c)
                ind += 1
                
        if " => " in line:
            split = line.split(" => ")
            newRule = (split[0].strip(), split[1].strip())
            #if split[1].strip() != split[0].strip()[2]:
            if split[1].strip() == PLANT:
                rules.append( newRule )
            else:
                print "skipped rule:",str(newRule)

    for rule in rules:
        print str(rule)

        
print plants
gen = 0
while gen < generations:
    if gen % 1000 == 0:
        print "Generation",gen, "length", len(plants), "sum", sum(plants.plants)
        ##plants converge at some point (before gen 1000), so simulation up to 10 000 is plenty.
        ##now we notice that for every 1000 gen after the 1st 1000, the plants increase by 55 000.
        ##solution is thus: sum of gen_1000 + sum of the rest i.e. ((50 000 000 000)/1000 -1)*55 000
    plants = doGeneration(plants, rules)
    gen += 1
print plants

print sum(plants)

