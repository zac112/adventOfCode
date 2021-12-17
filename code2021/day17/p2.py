from collections import namedtuple

targetX = [85,145]
targetY = [-163,-108]

#targetX = [20,30]
#targetY = [-10,-5]

targetArea = set((x,y) for x in range(targetX[0],targetX[1]+1) for y in range(targetY[0],targetY[1]+1))
Velocity = namedtuple('Velocity',['x','y'])

def simulate(x,y, vel, path):
    #print(x,y,vel)
    path.add((x,y))
    if (x,y) in targetArea:
        return (True,path)
    if x>targetX[1] or y<targetY[0]:
        return (False,path)
    
    drag = 0
    if vel.x != 0:
        drag = vel.x-(vel.x//abs(vel.x))
        
    return simulate(x+vel.x,y+vel.y,Velocity(drag,vel.y-1),path)
  
def getAllRanges():
    for x in range(0,targetX[1]+1):
        for y in range(targetY[0],abs(targetY[0])+1):
            success, overshot = simulate(0,0,Velocity(x,y),set())
            if success:
                targetArea.add((x,y))
path = set()
getAllRanges()
print(len(targetArea))

