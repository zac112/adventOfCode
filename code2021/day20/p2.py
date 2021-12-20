from itertools import product
from collections import deque
        
with open('data.txt') as f:
    enhancement = f.readline().strip()
    f.readline().strip()
    image = deque([deque([cell for cell in line if cell in ".#" ]) for line in f.readlines() ])    

def pad(image, symbol,times):
    for i in range(times):
        for y, line in enumerate(image):
            line.appendleft(symbol)
            line.append(symbol)

        image.appendleft(deque([symbol])*len(line))
        image.append(deque([symbol])*len(line))
        
def getNewPixel(image,x,y, enhancementNum):
    newPixels = []

    for a,b in product([-1,0,1], repeat=2):
        newPixels.append('1' if image[y+a][x+b]=='#' else '0')       
    
    index=int("".join(newPixels),2)
    return enhancement[index]

def enhance(image, enhancementNum):
    newImage = deque([])
    for y,line in enumerate(image):
        if y<1 or y >= len(image)-1:
            continue
        newrow = deque()
        newImage.append(newrow)
        for x,cell in enumerate(line):
            if x<1 or x >= len(image[y])-1:
                continue
            newrow.append(getNewPixel(image, x,y,0))

    
    return newImage
    
def printImage(image):
    [print("".join(line)) for line in image]


steps = 50

for num in range(steps):
    pad(image,("."+enhancement[0])[num%2],2)
    print(num+1,"with empty",("."+enhancement[0])[num%2])
    image = enhance(image,num)
    #printImage(image)

printImage(image)

print(len([cell for line in image for cell in line if cell == "#"]))
print(len(image))
