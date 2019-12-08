import os
import sys
sys.path.append("..")
from IntcodeComputer import Computer

program = []
with open("../../day7.txt", "r") as f:
    for line in f:
        program = program + line.split(",")

#program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
#print (program)
def sample(length):
    for x in range(length**length):
        l = [(x//length**y)%length for y in range(length-1,-1,-1)]
        if len(set(l)) == length:
            yield l

sampler = sample(5)
#(inputs, output)
max_output = ([],0)
for i in sampler:
    print (i)
    input_value = 0
    for x in range(5):
        c = Computer(list(program), [i[x], input_value])
        input_value = c.run()
        
    if input_value > max_output[1]:
        max_output = (list(i), input_value)

print (max_output)
