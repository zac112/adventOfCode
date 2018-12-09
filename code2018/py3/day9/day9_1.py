#puzzle input: 430 players; last marble is worth 71588 points
demoInput = False

if demoInput:
    players = 13
    marbles = 7999
else:
    players = 430
    marbles = 71588

currentMarble = 0
currentPosition = 0
board = [0]
newMarblePos = 2
scoringMarble = 23

scores = {}

for marble in range(1, marbles+1):
    player = ((marble-1)%players)+1

    if marble > 1 and marble % scoringMarble == 0:
        turnScore = marble + scores.setdefault(player, 0)
        marbleToRemove = (currentPosition+len(board) - 7)%len(board)
        scores[player] = turnScore + board.pop(marbleToRemove)
        currentPosition = marbleToRemove
        #print ("*[",player,"]",board, "; scored",scores[player])
        continue
    
    currentPosition = (currentPosition+newMarblePos)%len(board)
    board.insert(currentPosition, marble)
    #print ("[",player,"]",board)

tally = sorted([x for x in scores.items()], key=lambda a : a[1], reverse=True)
print(tally[0])
