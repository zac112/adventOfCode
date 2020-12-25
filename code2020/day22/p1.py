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
from collections import deque
decks = [deque(),deque()]

for i, player in enumerate(data.split("!")):
    for deck in player.splitlines()[1:]:
        decks[i].append(int(deck))

print(decks)

while len(decks[0]) > 0 and len(decks[1]) > 0:
    c1,c2 = decks[0].popleft(),decks[1].popleft()
    #print("Plays:",c1,c2)
    if c1 > c2:
        decks[0].append(c1)
        decks[0].append(c2)
    else:
        decks[1].append(c2)
        decks[1].append(c1)
    #print(decks)
print(decks)
winner = decks[0] if len(decks[0])>0 else decks[1]
print("Score:",sum([x*(i+1) for i,x in enumerate(list(winner)[::-1])]))
