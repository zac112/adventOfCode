from functools import reduce

class Cookie:

    def __init__(self,name, cap, dur, fla, tex, cal):
        self.name = name
        self.capacity = cap
        self.durability = dur
        self.flavor = fla
        self.texture = tex
        self.calories = cal

    def score(self, amount, vals):
        vals[0] += self.capacity*amount
        vals[1] += self.durability*amount
        vals[2] += self.flavor*amount
        vals[3] += self.texture*amount
        vals[4] += self.calories*amount
        
cookies = []
with open("../../data/15.txt", "r") as f:
    for line in f:
        split = line.split(" ")
        cookies.append(Cookie(split[0][:-1], int(split[2][:-1]), int(split[4][:-1]), int(split[6][:-1]), int(split[8][:-1]), int(split[10]) ))


total = 101
maxScore = 0

for a in range(total):    
    for b in range (total-a):        
        for c in range (total-a-b):            
            for d in range (total-a-b-c):                                

                vals = [0,0,0,0,0]
                amounts = [a, b, c, d]

                [cookies[i].score(amounts[i], vals) for i in range(len(amounts))]

                if vals[4] != 500 or len([x for x in vals[:-1] if x < 0]) > 0:
                    continue

                maxScore = max(reduce((lambda a,b:a*b),vals[:-1]),maxScore)
print(maxScore)
