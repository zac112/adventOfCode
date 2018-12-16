##preparation for part2
def findOpcodes(codes):
    while len(codes) > 0:
        codes.sort(key= lambda a: len(a[1]))
        command = codes[0][1][0]
        
        print(codes[0][0][:2],":",command)
        for c in codes:
            try:
                c[1].remove(command)
            except:
                pass
        codes= [c for c in codes if len(c[1])>0]
        

def decode(code):
    code = code[0].split(" ")
    opcode = int(code[0])
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


opcodes = [addr,addi,mulr,muli,banr,bani,borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

commands = []
opcodeWithMethods = []
with open("../../data/16_1.txt", "r") as f:    
    registersBefore =[]
    registersAfter = []
    for line in f:
        line = line.replace("\n", "")
        matches = []
        if "Before:" in line:
            registersBefore = [int(x) for x in line[line.find("[")+1:line.find("]")].strip().split(",")]
        elif "After:" in line:
            registersAfter = [int(x) for x in line[line.find("[")+1:line.find("]")].split(",")]
            for code in opcodes:
                realRegistersAfter = list(registersBefore)
                try:
                    code(commands[-1:][0], realRegistersAfter)
                    if len([i for i,j in zip(realRegistersAfter, registersAfter) if i == j]) == len(registersAfter): 
                        commands[-1:][0][1] += 1
                        matches.append(code.__name__)                        
                        
                except:
                    pass
            ##used for part2 preparation
            opcodeWithMethods.append([commands[-1:][0][0],matches])
        else:  
            commands.append([line,0])

commands.sort(key=lambda a : a[1])
result = [x for x in commands if x[1] >=3]
print(len(result))
#part2 preparation
findOpcodes(opcodeWithMethods)
