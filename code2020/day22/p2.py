data = """Player 1:
17
19
30
45
25
48
8
6
39
36
28
5
47
26
46
20
18
13
7
49
34
23
43
22
4
!Player 2:
44
10
27
9
14
15
24
16
3
33
21
29
11
38
1
31
50
41
40
32
42
35
37
2
12"""

test="""Player 1:
9
2
6
3
1
!Player 2:
5
8
4
7
10"""

test1="""Player 1:
43
19
!Player 2:
2
29
14"""
from collections import deque
decks = [deque(),deque()]

for i, player in enumerate(data.split("!")):
    for deck in player.splitlines()[1:]:
        decks[i].append(int(deck))

print(decks)
nextGame = [1]
def game(decks):
    gameInd = nextGame[0]
    nextGame[0] += 1
    #print("Starting game",gameInd)
    history = {0:set(),
               1:set()}
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        d1, d2 = tuple(decks[0]), tuple(decks[1])
        #print(decks)
        if d1 in history[0]:
            return ((0, decks[0]), sum([x*(i+1) for i,x in enumerate(list(decks[0])[::-1])]))
        else:
            history[0].add(d1)
        if d2 in history[1]:
            return ((0, decks[0]), sum([x*(i+1) for i,x in enumerate(list(decks[0])[::-1])]))
        else:
            history[1].add(d2)
            
        c1,c2 = decks[0].popleft(),decks[1].popleft()
        #print("Plays:",c1,c2)
        if len(decks[0])>=c1 and len(decks[1])>=c2:
            winnerdeck,score = game([deque(list(decks[0])[:c1]), deque(list(decks[1])[:c2])])            
            winner, deck = winnerdeck
            #print("Sub-game won by",winner)
        else:
            #print("Plays:",c1,c2)
            if c1 > c2:
                winner = 0
            else:
                winner = 1
                
        if winner == 0:
            decks[0].append(c1)
            decks[0].append(c2)
        else:
            decks[1].append(c2)
            decks[1].append(c1)
        
    winner = (0, decks[0]) if len(decks[0])>0 else (1, decks[1])
    return (winner, sum([x*(i+1) for i,x in enumerate(list(winner[1])[::-1])]))

winner,score = game(decks)
print("Winner",winner,score)

#High 35320
