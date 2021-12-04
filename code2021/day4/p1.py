with open('data.txt') as file:
    numbers = [int(x) for x in file.readline().split(',')]
    boards = []
    for line in file.readlines():
        if line == "\n":
            board = []
            boards.append(board)
            continue
        board.append([int(x) for x in line.split(" ") if x != ""])

#print(numbers)
#print(boards)

def transpose(board):
    return [[board[j][i] for j in range(len(board[i]))] for i in range(len(board))]

def checkWin(board, marked):
    for line in board:
        if len([cell for cell in line if cell not in marked])==0:
            return True        
    return False
    
def play(board, numbers, drawnNumbers):
    drawnNumbers.append(numbers[0])
    if checkWin(board, drawnNumbers):
        return True
    if checkWin(transpose(board), drawnNumbers):
        return True

    return play(board, numbers[1:], drawnNumbers)

movesRequired = {}
for index, board in enumerate(boards):
    drawnNumbers = []
    if play(board, numbers, drawnNumbers):
        movesRequired.setdefault(index, drawnNumbers)        

best = min(movesRequired,key=lambda a:len(movesRequired[a]))
bestBoard = boards[best]
flatBestBoard = [cell for line in bestBoard for cell in line]
score = sum([x for x in flatBestBoard if x not in movesRequired[best]])*movesRequired[best][-1]
print("Score",score)
