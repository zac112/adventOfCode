def decode(code):
    r1 = int(code[1])
    r2 = int(code[2])
    r3 = int(code[3])
    return r1,r2,r3

def addr(code, registers):
    r1,r2,r3 = decode(code)
    registers[r3] = registers[r1]+registers[r2]

def addi(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = registers[r1]+r2

def mulr(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = registers[r1]*registers[r2]

def muli(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = registers[r1]*r2

def banr(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = registers[r1]&registers[r2]

def bani(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = registers[r1]&r2

def borr(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = registers[r1]|registers[r2]

def bori(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = registers[r1] | r2

def setr(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = registers[r1]

def seti(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = r1

def gtir(code, registers):
    r1,r2,r3 = decode(code)
    if r1 > registers[r2]:
        registers[r3] = 1
    else:
        registers[r3] = 0

def gtri(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = 1 if registers[r1] > r2 else 0

def gtrr(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = 1 if registers[r1] > registers[r2] else 0

def eqir(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = 1 if r1 == registers[r2] else 0

def eqri(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = 1 if registers[r1] == r2 else 0

def eqrr(code, registers):
    r1,r2,r3 = decode(code)    
    registers[r3] = 1 if registers[r1] == registers[r2] else 0

def run(program, registers, ip):
    lines = 0
    while registers[ip] < len(program):
        #print (registers)
        currentLine = program[registers[ip]]
        opcode = currentLine[0]
        #if lines % 100000 == 0 or (lines > 6290000 and lines%1 == 0):
        #print("line",lines, currentLine, registers)
        globals()[opcode](currentLine, registers)
        registers[ip] += 1
        lines += 1
    print (lines)
    
registers = [0,0,0,0,0,0]
program = []
ip =0
with open("../../data/19t.txt", "r") as f:        
    for line in f:
        if line[0] == "#":
            ip = int(line[4:])
        else:
            line = line.replace("\n", "")
            split = line.split(" ")
            loc = [split[0], int(split[1]), int(split[2]), int(split[3])]
            program.append(loc)            

print (ip, program)
run(program, registers, ip)

print(registers)
