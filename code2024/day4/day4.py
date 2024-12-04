with open("data.txt") as f:
    letters = [[c for c in line] for line in f.readlines()]

def inside(x,y):
    if x<0 or y<0: return False
    if x>=len(letters) or y>=len(letters[x]): return False
    return True

def followWord(x,y,direction,word):
    if len(word)==1 and letters[x][y]==word[0]: return 1

    if letters[x][y]==word[0]:
        a,b = direction
        if not inside(x+a,y+b): return 0
        return followWord(x+a,y+b,direction,word[1:])
    return 0

def tryDirections(x,y,word):
    found = 0    
    for a in range(-1,2):
        for b in range(-1,2):
            if a==0 and b==0: continue
            if not inside(x+a,y+b): continue                
            found += followWord(x+a,y+b,(a,b),word[1:])    
    return found

found = 0
for x,line in enumerate(letters):
    for y,c in enumerate(line):
        if letters[x][y]=='X':
            found += tryDirections(x,y,"XMAS")

print("XMAS:",found)

#part2
found = 0
for x,line in enumerate(letters):
    for y,c in enumerate(line):
        if c == 'A':
            if all((
                inside(x-1,y-1),
                inside(x+1,y+1),
                inside(x-1,y+1),
                inside(x+1,y-1))):
                mas1 = sorted([letters[x-1][y-1],'A',letters[x+1][y+1]])
                mas2 = sorted([letters[x-1][y+1],'A',letters[x+1][y-1]])
                if mas1 == mas2 and mas1==sorted(['M','A','S']):
                    found += 1
            
print("X-MAS:",found)
