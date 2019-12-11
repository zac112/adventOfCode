import os
import sys
sys.path.append("..")
from IntcodeComputer import Computer

with open("../../day11.txt", "r") as f:
    program = f.readlines()[0].split(",")


class Robot:
    
    def __init__(self, program):
        self.position = (0,0)
        self.directions = [ (0,-1), (1,0), (0,1), (-1,0) ] #URDL
        self.direction =  0
        self.inputNum = 0
        self.brain = Computer(program, onInput=self.readPanel, onOutput=self.handleOutput, program_input=[0])
        self.panels = dict()
        self.brain.run()

    def readPanel(self):
        return self.panels.get(self.position,0)
    
    def handleOutput(self, x):
        #print (x)
        if self.inputNum == 0:
            #print("painted",self.position, "white" if x == 1 else "black")
            self.panels[self.position] = x
        if self.inputNum == 1:
            #print("turned", "left" if x == 0 else "right")
            self.direction = (4+self.direction+(x*2-1))%4
            self.position = self.getNewPosition()
            #self.brain.receiveInput(self.panels.get(self.position,0))
            
        self.inputNum = (self.inputNum+1)%2
        
    def getNewPosition(self):
        newDir = self.directions[self.direction]
        return (self.position[0]+newDir[0], self.position[1]+newDir[1])
    
robo = Robot(program)
print (len(robo.panels))

#wrong: 8149 high
