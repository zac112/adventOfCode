RIGHT = (0,1)
DOWN  = (1,0)
UP    = (-1,0)
LEFT  = (0,-1)

DIRECTIONS = [UP,RIGHT,DOWN,LEFT]
TURNS = [-1, 0, 1]

LEFTTURN = "\\"
LEFTTURNS = {0:3,1:2,2:1,3:0}
RIGHTTURN = "/"
RIGHTTURNS = {0:1,1:0,2:3,3:2}
INTERSECTION = "+"

area = []
#cart : y,x,direction,nextTurn
carts = []

def printArea(area, carts):    
    areaCopy = list([list(row) for row in area])
    for cart in carts:
        if cart[2] == 0:
            areaCopy[cart[0]][cart[1]] = "^"
        if cart[2] == 2:
            areaCopy[cart[0]][cart[1]] = "v"
        if cart[2] == 3:
            areaCopy[cart[0]][cart[1]] = "<"
        if cart[2] == 1:
            areaCopy[cart[0]][cart[1]] = ">"
    for line in areaCopy:
        print "".join(line)
    
def intersection(cart):
    
    turn((len(DIRECTIONS) + cart[2] + TURNS[cart[3]]) % len(DIRECTIONS), cart)
    cart[3] = (cart[3]+1) % len(TURNS)
    
def turn(direction, cart):
    cart[2] = direction

def checkCollisions(carts):
    positions = [(cart[0],cart[1]) for cart in carts ]
    
    return len([pos for pos in positions if positions.count(pos) > 1])
    
with open("../../data/13.txt", "r") as f:
    y = 0
    for line in f:
        row = []
        area.append(row)
        x = 0
        for c in line[:-1]:
            if c == "^":
                carts.append([y,x,0, 0])
                row.append("s")
            elif c == "<":
                carts.append([y,x,3, 0])
                row.append("s")
            elif c == ">":
                carts.append([y,x,1, 0])
                row.append("s")
            elif c == "v":
                carts.append([y,x,2, 0])
                row.append("s")
            else:
                row.append(c)
            x += 1
        y += 1


collisions = 0

#printArea(area, carts)
while collisions == 0:
    for cart in carts:
        cart[0] += DIRECTIONS[cart[2]][0]
        cart[1] += DIRECTIONS[cart[2]][1]
        if area[cart[0]][cart[1]] == LEFTTURN:
            turn(LEFTTURNS[cart[2]], cart)
        if area[cart[0]][cart[1]] == RIGHTTURN:
            turn(RIGHTTURNS[cart[2]], cart)
        if area[cart[0]][cart[1]] == INTERSECTION:
            intersection(cart)
        if(checkCollisions(carts)):
            collisions += 1
            print "collision at",cart[1],cart[0]
            break
    #printArea(area, carts)
