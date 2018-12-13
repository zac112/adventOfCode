#x and y inversed
RIGHT = (0,1, ">")
DOWN  = (1,0, "v")
UP    = (-1,0, "^")
LEFT  = (0,-1, "<")

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
        areaCopy[cart[0]][cart[1]] = DIRECTIONS[cart[2]][2]
        
    for line in areaCopy:
        print "".join(line)
    
def intersection(cart):
    
    turn((len(DIRECTIONS) + cart[2] + TURNS[cart[3]]) % len(DIRECTIONS), cart)
    cart[3] = (cart[3]+1) % len(TURNS)
    
def turn(direction, cart):
    cart[2] = direction

def getCollisions(carts):
    positions = [(cart[0],cart[1]) for cart in carts ]
    
    return [pos for pos in positions if positions.count(pos) > 1]
    
with open("../../data/13t.txt", "r") as f:
    y = 0
    for line in f:
        row = []
        area.append(row)
        x = 0
        for c in line[:-1]:
            for i in range(len(DIRECTIONS)):
                if c == DIRECTIONS[i][2]:                    
                    carts.append([y,x,i, 0])
                    row.append("s")
                    break
            else:
                row.append(c)
            x += 1
        y += 1

printArea(area, carts)
seconds = 0
while len(carts) > 1:
    carts.sort(key=lambda cart : str(cart[0])+str(cart[1]))

    i = 0    
    while i < len(carts):
        cart = carts[i]
        cart[0] += DIRECTIONS[cart[2]][0]
        cart[1] += DIRECTIONS[cart[2]][1]
        if area[cart[0]][cart[1]] == LEFTTURN:
            turn(LEFTTURNS[cart[2]], cart)
        if area[cart[0]][cart[1]] == RIGHTTURN:
            turn(RIGHTTURNS[cart[2]], cart)
        if area[cart[0]][cart[1]] == INTERSECTION:
            intersection(cart)
        
        cols = getCollisions(carts)
        if(len(cols) > 1):
            cs = [cart for cart in carts if (cart[0],cart[1]) in cols]
            #keeps order
            for c in cs:
                print "collision at",c[1],c[0], "on second",seconds                
                if carts.index(c) <= i:
                    i -= 1
                carts.remove(c)

        i += 1
    printArea(area, carts)
    seconds += 1


print str(carts[0][1])+","+str(carts[0][0])
