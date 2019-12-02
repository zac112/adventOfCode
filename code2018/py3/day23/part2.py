import re

class Bot:
    def __init__(self, x,y,z,r):
        self.x=int(x)
        self.y=int(y)
        self.z=int(z)
        self.r=int(r)
        self.inRange=[]

    def checkInRange(self, otherBot):
        if self.countDistance(otherBot) <= self.r:
            self.inRange.append(otherBot)        

    def getPos(self):
        return [self.x,self.y,self.z]
    
    def countDistance(self, otherBot):
        return sum( [ abs(self.getPos()[i]-otherBot.getPos()[i]) for i in range(3)])
        
    def getBotsInRange(self):
        return self.inRange
    
    def __str__(self):
        return "["+str(self.x)+","+str(self.y)+","+str(self.z)+","+str(self.r)+"]"
    
bots = []        
with open("data.txt", "r") as f:
    for line in f:
        m = re.match("pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(-?\d+)",line)
        bots.append(Bot(m.group(1),m.group(2),m.group(3),m.group(4)))


for bot in bots:
    for bot2 in bots:
        bot.checkInRange(bot2)

closestBot = sorted(bots, key=lambda a:len(a.inRange), reverse=True)[0]


