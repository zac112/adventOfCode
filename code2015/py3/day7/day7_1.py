def doEval(index, instruction):
    print (instruction)
    result = str(eval(instruction[1]+instruction[2][0]))
    instruction[3].append(result)
    instructions.pop(index)    
    
lines = []
with open("../../data/7.txt", "r") as f:
    for line in f:
        lines.append(line.replace("\n",""))

#0 value
#1 NOT
#2 AND
#3 OR
#4 LSHIFT
#5 RSHIFT
#[1st operand, instruction, 2nd operand, [output]]
#2nd operand is not present if (instruction < 2). Output is the list reference from wires

instructions = []
wires = {}
#first collect all outputs
for line in lines:
    split = line.split("-> ")
    wires[split[1]] = []

#then connect them to the gates and build the instruction
for line in lines:
    split = line.split(" ")

    operand1 = []
    operand2 = []
    instruction = ""
    
    if "NOT" in line:
        instruction = "~"
    if "AND" in line:
        instruction = "&"
    if "OR" in line:
        instruction = "|"
    if "LSHIFT" in line:
        instruction = "<<"
    if "RSHIFT" in line:
        instruction = ">>"

    if instruction == "":
        operand2 = wires.get(split[0],[split[0]])
    elif instruction == "~":
        operand2 = wires.get(split[1],[split[1]])
    else:
        operand1 = wires.get(split[0],[split[0]])
        operand2 = wires.get(split[2],[split[2]])
        
    instructions.append([operand1, instruction, operand2, wires[split[len(split)-1]]]) 

#finally evaluate all instructions
index = 0
while len(instructions) > 0:
    instruction = instructions[index]        

    if instruction[1] == "" or instruction[1] == "~":
        if len(instruction[2]) > 0:
            print (instruction)
            result = str(eval(instruction[1]+instruction[2][0]))
            instruction[3].append(result)
            instructions.pop(index)
            index -= 1
            continue            

    if len(instruction[0]) == 0 or len(instruction[2]) == 0:
        #skip the instructions not done yet
        index = (index+1)%len(instructions)
        continue

    print (instruction)
    result = str(eval(instruction[0][0]+instruction[1]+instruction[2][0]))
    instruction[3].append(result)
    instructions.pop(index)
    index -= 1 
    
    
print(wires["a"])
