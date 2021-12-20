from itertools import product

with open('data.txt') as f:
    enhancement = f.readline().strip()
    f.readline().strip()
    image = set((y,x) for y,line in enumerate(f.readlines()) for x,cell in enumerate(line) if cell in "#")

def getPixel(image,x,y, enhancementNum):
    minx = min(image, key=lambda a:a[0])[0]-1
    miny = min(image, key=lambda a:a[1])[1]-1
    maxx = max(image, key=lambda a:a[0])[0]+1
    maxy = max(image, key=lambda a:a[1])[1]+1

    newPixels = []
    #print(x,y, '#' if (x,y) in image else '.')
    
    for a,b in product([-1,0,1], repeat=2):
        outside = False
        x1= x+a
        y1= y+b
        if x1 == minx or y1 == minx or x1 == maxx or y1 == maxy:
            outside = (enhancementNum % 2 == 1)
        newCoord = (x+a,y+b)
        #print(newCoord)
        newPixels.append(outside or newCoord in image)
       
    #print(newPixels)
    index=int("".join(map(lambda a:'1' if a else '0', newPixels)),2)
    #¤print(index)
    return enhancement[index]

def enhance(image, enhancementNum):
    
    minx = min(image, key=lambda a:a[0])[0]-1-4
    miny = min(image, key=lambda a:a[1])[1]-1-4
    maxx = max(image, key=lambda a:a[0])[0]+2+4
    maxy = max(image, key=lambda a:a[1])[1]+2+4

    newImage = set()
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            #print("NewPixel",getPixel(image, x,y))
            if getPixel(image, x,y,enhancementNum) == '#':
                newImage.add((x,y))
    return newImage
    
def printImage(image):
    minx = min(image, key=lambda a:a[0])[0]-1
    miny = min(image, key=lambda a:a[1])[1]-1
    maxx = max(image, key=lambda a:a[0])[0]+2
    maxy = max(image, key=lambda a:a[1])[1]+2

    for x in range(minx, maxx):
        l = []
        for y in range(miny, maxy):                
            l.append('#' if (x,y) in image else '.')
        print("".join(l))

printImage(image)
for num in range(50):
    print(num+1)
    image = enhance(image,num)
    #printImage(image)

printImage(image)

#A gold start some manual image manipulation later (removing the infinite border...
