from collections import deque
from functools import reduce
import operator

class Monkey:
    def __init__(self):
        self.items = deque()
        self.inspections = 0

    def setTest(self, divisibility, truemonkey, falsemonkey):
        def test(item):
            self.inspections += 1            
            worrylevel = eval(self.operation)%self.lcm
            nextMonkey = truemonkey if worrylevel%divisibility==0 else falsemonkey
            return (worrylevel,nextMonkey)
        self.test = test
        self.divisibility = divisibility

    def setOperation(self, oper):
        self.operation = oper.split("= ")[1].replace("old","item")
        
    def getItem(self, item):
        self.items.append(item)

    def giveItem(self):
        return self.items.popleft()

    def hasItems(self):
        return len(self.items)>0

    def setLCM(self, lcm):
        self.lcm = lcm
        
monkeys = []
with open("data.txt") as f:
    while "Monkey" in f.readline():
        monkeys.append(Monkey())
        line = f.readline().split(":")[1]
        for item in line.split(","):
            monkeys[-1].getItem(int(item))

        monkeys[-1].setOperation(f.readline())
        
        div = int(f.readline().split(" ")[-1])
        truemonkey = int(f.readline().split(" ")[-1])
        falsemonkey = int(f.readline().split(" ")[-1])
        monkeys[-1].setTest(div,truemonkey,falsemonkey)
        f.readline()

monkey_lcm = reduce(operator.mul,[m.divisibility for m in monkeys],1)
for m in monkeys:
    m.setLCM(monkey_lcm)
    
for r in range(20):
    for monkey in monkeys:
        while monkey.hasItems():
            item = monkey.giveItem()
            item,newMonkey = monkey.test(item)
            monkeys[newMonkey].getItem(item)

print([monkey.inspections for monkey in monkeys])
best_monkeys = sorted([monkey.inspections for monkey in monkeys])[-2:]
result = reduce(operator.mul,best_monkeys,1)
print(result)
