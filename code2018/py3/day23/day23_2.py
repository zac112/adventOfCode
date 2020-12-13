import re

class Bot:

    def __init__(self, posx, posy, posz, r):
        self.posx=int(posx)
        self.posy=int(posy)
        self.posz=int(posz)
        self.r=int(r)

    def getPos(self):
        return [self.posx, self.posy, self.posz]

    def getRelativePos(self, other):
        return [abs(other.posx-self.posx), abs(other.posy-self.posy), abs(other.posz-self.posz)]

    def __str__(self):
        return "bot at pos:"+str(self.posx)+","+str(self.posy)+","+str(self.posz)+", r:"+str(self.r)
    
#pos=<60235614,-20031762,40509437>, r=53224897
bots = []
with open("../../data/23.txt", "r") as f:
        #f= ["pos=<0,0,0>, r=4","pos=<1,0,0>, r=1","pos=<4,0,0>, r=3","pos=<0,2,0>, r=1","pos=<0,5,0>, r=3","pos=<0,0,3>, r=1","pos=<1,1,1>, r=1","pos=<1,1,2>, r=1","pos=<1,3,1>, r=1"]
        f= [
            "pos=<10,12,12>, r=2",
"pos=<12,14,12>, r=2",
"pos=<16,12,12>, r=4",
"pos=<14,14,14>, r=6",
"pos=<50,50,50>, r=200",
"pos=<10,10,10>, r=5"]
        for line in f:
            split = line.split(",")            
            bots.append(Bot(re.sub("[^\d-]", "", split[0]), re.sub("[^\d-]", "", split[1]), re.sub("[^\d-]", "", split[2]), re.sub("[^\d-]", "", split[3]) ))

inRange = {}
for i in range(len(bots)):
    inRange.setdefault(bots[i],0)
    for j in range(len(bots)):
        inRange.setdefault(bots[j],0)
        if sum(bots[i].getRelativePos(bots[j])) <= bots[i].r:
            inRange[bots[i]] += 1
            if i != j:
                inRange[bots[j]] += 1

