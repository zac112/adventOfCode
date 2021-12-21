
player1={'space':6,'score':0}
player2={'space':2,'score':0}

#test data
#player1={'space':4,'score':0}
#player2={'space':8,'score':0}

die = {'thrown':0 , 'score':1, 'faces':100}

boardsize = 10

def playTurn(player,die):
    #print("rolls", die['score'], die['score']+1, die['score']+2)
    diesum = (die['score']+1)*3
    die['thrown']+=3    
    #die['score']= max((die['score']+3)%(die['faces']+1),1)
    die['score']= (die['score']+3)
    player['space'] += diesum%boardsize
    
    if die['score'] > die['faces']:
        die['score']= max(die['score']%die['faces'],1)
    
    if player['space'] > boardsize:
        player['space'] = max(player['space'] % boardsize,1)
    player['score'] += player['space']

players = [player1,player2]
turn = 0
while (player := players[(turn)%2])['score'] < 1000:
    turn += 1

    playTurn(player, die)
    if turn%100 ==0:
        print("Player",(turn%2+1))
        print(turn)
        print(player1)
        print(player2)
    if player['score'] >= 1000:
        break
    
    

winnerIndex = players.index(player)
loser = players[winnerIndex-1]
print("End:")
print("P1:",player1)
print("P2:",player2)
print("Die:",die)
print(loser['score']*die['thrown'])
