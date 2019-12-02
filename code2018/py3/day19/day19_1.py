def decode(code):
    code = code[0].split(" ")
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
    while registers[ip] < len(program):
        currentLine = program[registers[ip]]
        split = currentLine.split(" ")
        opcode = split[0]
        globals()[opcode]([currentLine], registers)
        registers[ip] += 1
    
registers = [0,0,0,0,0,0]
program = []
ip =0
with open("../../data/19.txt", "r") as f:        
    for line in f:
        if line[0] == "#":
            ip = int(line[4:])
        else:
            line = line.replace("\n", "")
            program.append(line)            

print (ip, program)
run(program, registers, ip)

print(registers)
