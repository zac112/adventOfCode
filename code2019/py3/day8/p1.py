width=25
height=6
#width=3
#height=2
layers=[]
data = []
with open("../../day8.txt", "r") as f:
    for c in f.readlines()[0]:
        data.append(int(c))
#data = [1,2,3,4,5,6,7,8,9,0,1,2,]
        
def fillPicture(data, layers):    
    def fillLayer(x,y, layer):
        if y >= width:
            x += 1
            y = 0
        if x>= height:
            return layer

        layer[x][y]=data.pop(0)
        return fillLayer(x,y+1, layer)

    while len(data) >0:
        layers.append(fillLayer(0,0, [[0 for x in range(width)] for y in range(height)]))        

def count(layer, val):
    return sum([row.count(val) for row in layer])
    
fillPicture(data,layers)
#print(layers)
layer = min(layers, key=lambda a:count(a,0))
print(layer)
print(count(layer,1)*count(layer,2))
    
