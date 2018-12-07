import string

global timeSpent
global taskTime
global workers
#are we practising or doing the real thing?
practiseRun = False

#for the actual question
if not practiseRun:
    taskTime = 60
    workers = 5
else:
    #for the example
    taskTime = 0
    workers = 2

class Work:
    name = ""
    #names of tasks
    prereqs = []
    timeSpent = 0
    tasksize = 0
    
    def __init__(self, name, prereqs):
        self.name = name
        self.prereqs = prereqs
        self.tasksize = taskTime+string.ascii_uppercase.index(name)+1
        
    def isDone(self):
        return self.timeSpent >= self.tasksize

    def work(self):
        self.timeSpent += 1

    def canStart(self, completedWork):
        canStart = self.timeSpent == 0
        
        for req in self.prereqs:
            canStart = canStart and req in [w.name for w in completedWork]            
        #print self.name,"prereqs",self.prereqs,"given completed work",[w.name for w in completedWork], canStart
        return canStart
        
class WorkDispenser:

    work = 0
    workLeft = []
    workDone = set([])

    #the machine requires time to process work submitted by the workers.
    #New work will be available the next second
    workToProcess = []
    
    def __init__(self, steps):
        units = set()
        left = set()
        right = set()
        
        for step in steps:
            left.add(step[0])
            right.add(step[1])

        units = left.union(right)
        self.work = len(units)
        
        print units
        for unit in units:
            prereqs = []            
            for step in steps:
                if unit == step[1]:
                    prereqs.append(step[0])
            self.workLeft.append( Work(unit, prereqs) )
        
    #The dispenser needs one second to process all completed work    
    def finishWork(self, work):
        self.workToProcess.append(work)

    #This is called every second to allow the dispenser to calculate new available work
    def process(self):
        for w in self.workToProcess:
            self.workDone.add(w)
        
    def getWork(self):
        nextWork = None
        assignableWork = [w for w in self.workLeft if not w.isDone() and w.canStart(self.workDone) and w not in self.workDone]
        if assignableWork == None or len(assignableWork) == 0:
            return None
        
        nextWork = assignableWork.pop(0)
        self.workLeft.remove(nextWork)
        if practiseRun:
            if nextWork == None:
                print "Got no work"
            else:
                print "Got work:",nextWork.name
        return nextWork
    
    def isAllDone(self):
        return self.work == len(self.workDone)
    
class Elf:
    currentWork = None
    num = 0
    dispenser = None
    
    def __init__(self, num, dispenser):
        self.num = num
        self.dispenser = dispenser

    def work(self):
        if self.currentWork == None:
            if practiseRun: print "Elf",self.num,"asks for work at",timeSpent
            self.currentWork = dispenser.getWork()
            if self.currentWork != None: print "Elf",self.num,"started work on",self.currentWork.name,"at",timeSpent
            
        if self.currentWork != None:            
            if practiseRun: print "Elf",self.num,"works on",self.currentWork.name,"at",timeSpent
            self.currentWork.work()
            if self.currentWork.isDone():
                self.dispenser.finishWork(self.currentWork)
                print "Elf",self.num,"finished work on",self.currentWork.name,"at",timeSpent
                self.currentWork = None              

    
allSteps = []
with open("../../data/7.txt", "r") as f:
    if practiseRun:
        f = ["Step C must be finished before step A can begin.","Step C must be finished before step F can begin.","Step A must be finished before step B can begin.","Step A must be finished before step D can begin.","Step B must be finished before step E can begin.","Step D must be finished before step E can begin.","Step F must be finished before step E can begin.",]
    for line in f:
        split = line.split(" ")
        allSteps.append((split[1],split[7]))

dispenser = WorkDispenser(allSteps)

elves = [Elf(x, dispenser) for x in range(workers)]

timeSpent = 0
while not dispenser.isAllDone():
    [elf.work() for elf in elves]
    timeSpent += 1
    dispenser.process()

print timeSpent
