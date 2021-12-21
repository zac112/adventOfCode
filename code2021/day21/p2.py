from functools import cache

player1={'space':6,'score':0}
player2={'space':2,'score':0}

#test data
#player1={'space':4,'score':0}
#player2={'space':8,'score':0}

die = {'thrown':0 , 'score':1, 'faces':100}

boardsize = 10
#e.g. we get a score of 6 in 7 worlds
worldPossibilities = {6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1}

@cache
def playTurn(playerspace, playerscore,
             opponentspace, opponentscore, diesum, p,startp):
    
    playerspace += diesum%boardsize
    
    if playerspace > boardsize:
        playerspace = max(playerspace % boardsize,1)
    playerscore += playerspace

    #print(playerspace, playerscore, opponentspace, opponentscore, turn, diesum)
    
    if playerscore >= 21:
        if p==startp:
            return [1,1]
        else:
            return [0,1]

    wins = [0,0] 
    for k,v in worldPossibilities.items():
        #print('player',p,' throws',k)
        worlds = playTurn(opponentspace, opponentscore,
                           playerspace, playerscore, k, p%2+1,startp)
        wins[0] += worlds[0]*v
        wins[1] += worlds[1]*v
        
    return wins
    

players = [player1,player2]

#[p1wins, all games]
stats = [0,0] 
for k,v in worldPossibilities.items():
    world = playTurn(player1['space'],player1['score'],
         player2['space'],player2['score'],k,1, 1)
    stats[0] += v*world[0]
    stats[1] += v*world[1]
    
print(stats)
print("Player 1 wins:",stats[0])
print("Player 2 wins:",stats[1]-stats[0])
