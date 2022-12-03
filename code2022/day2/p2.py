scores = {'rock':1,
         'paper':2,
         'scissors':3}

hands = {('A','X'):'rock',
         ('B','Y'):'paper',
         ('C','Z'):'scissors'}

wins = ['rock','paper','scissors']

with open("data.txt") as f:
    data = f.read()

score = 0

for turn in data.split("\n"):
    p1,p2 = turn.split(" ")
    for a,b in hands.items():
        if p1 in a:
            p1 = b

    if p2=="Z":
        #win
        p2 = wins[(wins.index(p1)+1)%len(wins)]
        score += scores[p2]+6
    elif p2=="Y":
        #draw
        p2 = wins[wins.index(p1)]
        score += scores[p2]+3
    else:
        #lost
        p2 = wins[(wins.index(p1)-1+len(wins))%len(wins)]
        score += scores[p2]+0        
    
print(score)
