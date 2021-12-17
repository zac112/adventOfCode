from collections import namedtuple

targetX = [85,145]
targetY = [-163,-108]

#targetX = [20,30]
#targetY = [-5,-1]

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
    
def findHighestParabola(xguess, yguess,path):
    success, overshot = simulate(0,0,Velocity(xguess,yguess),path)
    print("simulating",xguess, yguess, success, overshot)

path = set()
"""
162 found by reasoning;
The probe trajectory (=function) always intersects
the x-axis with x_vel=0, if start y_vel>0.
The highest point in the parabola must be reached
when the probe falls the maximum amount the next step.
The maximum the probe can sink is
the deepest point in the target area, i.e. -163,
thus with start y_vel=162 it sinks 163 units.
"""
findHighestParabola(4,162,path)
print(max(path,key=lambda a:a[1]))

