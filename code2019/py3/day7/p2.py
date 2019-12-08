import os
import sys
sys.path.append("..")
from IntcodeComputer import Computer

program = []
with open("../../day7.txt", "r") as f:
    for line in f:
        program = program + line.split(",")

def sample(length):
    for x in range(length**length):
        l = [(x//length**y)%length+length for y in range(length-1,-1,-1)]
        if len(set(l)) == length:
            yield l

numAmplifiers = 5
#(inputs, output)
max_output = [[],0]

def checkMaxOutput(l, output, old_output):
    old_output[:] = [i,output] if old_output[1] < output else old_output
    print(l,"Output:",output)

for i in sample(numAmplifiers):
    computers = {}
    for x in range(numAmplifiers):
        l = []
        computers[x] = [Computer(list(program), l),l]
        
    for x in range(numAmplifiers):
        computers[x][0].onOutput = computers[(x+1)%numAmplifiers][0].receiveInput
        computers[x][1].append(i[x])
        
    computers[numAmplifiers-1][0].onFinished = lambda a: checkMaxOutput(i,a,max_output)                
    computers[0][1].append(0)
    computers[0][0].run()

print (max_output)
