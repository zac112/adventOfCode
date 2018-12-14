#Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds
class Raindeer:

    def __init__(self, name, speed, time, rest):
        
        self.name = name
        self.speed = speed
        self.time = time
        self.rest = rest
        self.ableToFly = time
        self.mustRestFor = 0
        self.distance = 0

    def fly(self):        
        if self.ableToFly > 0:
            self.ableToFly -= 1
            self.distance += self.speed
            if self.ableToFly == 0:
                self.mustRestFor = self.rest
        else:
            self.mustRestFor -= 1
            if self.mustRestFor == 0:
                self.ableToFly = self.time
            
raindeer = []
with open("../../data/14.txt","r") as f:
    #f = ["Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.","Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."]
    for line in f:
        split = line.split(" ")
        raindeer.append(Raindeer(split[0],int(split[3]), int(split[6]), int(split[13])))

seconds = 2503
for i in range(seconds):
    for rd in raindeer:
        rd.fly()
        
raindeer.sort(key = lambda a : a.distance, reverse = True)
print (raindeer[0].distance)
