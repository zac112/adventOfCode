width=25
height=6
layers=[]
data = []
with open("../../day8.txt", "r") as f:
    [data.append(int(c)) for c in f.readlines()[0]]

#short versions
def fillPicture(data):
    numLayers = len(data)//(height*width)
    return [[[data[l*height*width + x + y*width] for x in range(width)] for y in range(height)] for l in range(numLayers)]

def combine(layers):
    dive = lambda y,x: next(filter(lambda a: a!=2,[layer[x][y] for layer in layers]))
    return[[ dive(x,y) for x in range(width)] for y in range(height)]

[print ("".join([str(x) if x==1 else " " for x in row])) for row in combine(fillPicture(data))]
    
    
####readable versions below:

##def recursiveFillPicture(data):
##    layers = []
##    def fillLayer(x,y, layer):
##        if y >= width:
##            x += 1
##            y = 0
##        if x>= height:
##            return layer
##
##        layer[x][y]=data.pop(0)
##        return fillLayer(x,y+1, layer)
##
##    while len(data) >0:
##        layers.append(fillLayer(0,0, [[0 for x in range(width)] for y in range(height)]))
##    return layers
##
##def iterativeCombine(layers):
##    combined = [[2 for x in range(width)] for y in range(height)]
##    for layer in layers:
##        for x in range(width):
##            for y in range(height):            
##                if(combined[y][x] == 2):
##                    combined[y][x] = layer[y][x]
##    return combined
##                    
##
##layers = fillPicture(data)
##for row in combine(layers):    
##    print ("".join([str(x) if x==1 else " " for x in row]))
    
