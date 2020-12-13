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
#pos=<60235614,-20031762,40509437>, r=53224897
bots = []
with open("../../data/23.txt", "r") as f:
        #f=["pos=<0,0,0>, r=4","pos=<1,0,0>, r=1","pos=<4,0,0>, r=3","pos=<0,2,0>, r=1","pos=<0,5,0>, r=3","pos=<0,0,3>, r=1","pos=<1,1,1>, r=1","pos=<1,1,2>, r=1","pos=<1,3,1>, r=1"]
        for line in f:

            split = line.split(",")
            
            bots.append(Bot(re.sub("[^\d-]", "", split[0]), re.sub("[^\d-]", "", split[1]), re.sub("[^\d-]", "", split[2]), re.sub("[^\d-]", "", split[3]) ))

bigR = sorted(bots, key=lambda b: b.r, reverse=True)[0]
print (len([b for b in bots if sum(b.getRelativePos(bigR)) <= bigR.r]))
